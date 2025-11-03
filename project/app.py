import os
from sqlmodel import SQLModel, Session, Field, create_engine, select
from sqlalchemy import URL
from typing import Annotated
from loguru import logger
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse


class Record(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    value: int



app = FastAPI()
db_url = URL.create(
    "postgresql+psycopg2",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
    database=os.environ["DB_DATABASE"],
)
engine = create_engine(db_url)
SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

session_dependency  = Annotated[Session, Depends(get_session)]


@app.post("/save")
async def save_value(db_session: session_dependency , value: int):
    existing_record = db_session.exec(
        select(Record).where(Record.value == value)
    ).first()
    if existing_record is not None:
        logger.info(f"Duplicate: [{value}] already exists in database")
        raise HTTPException(
            status_code=400,
            detail=f"Value [{value}] was already processed",
        )

    next_value_record = db_session.exec(
        select(Record).where(Record.value == (value + 1))
    ).first()
    if next_value_record is not None:
        logger.info(f"Incremented value [{next_value_record.value}] "
                    "already exists in database")
        raise HTTPException(
            status_code=400,
            detail=f"Incremented value [{next_value_record.value}] "
                    "was already processed",
        )

    new_record = Record(value=value)
    db_session.add(new_record)
    db_session.commit()

    logger.info(f"Success: processed number [{value}]")
    inc_value = value + 1
    return JSONResponse(status_code=200, content={"result": inc_value})
