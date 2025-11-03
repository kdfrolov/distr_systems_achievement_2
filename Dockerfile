FROM python:3.13-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt;
COPY project ./project
CMD ["fastapi", "run", "project/app.py"]
