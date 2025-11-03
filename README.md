# Построение распределенных систем и облачных вычислений
## Ачивка 2
### Запустить:
```
docker compose up --build -d
```
### Проверка работы
Сохранение числа, в ответе 131
```
curl -X POST "http://localhost:80/save?value=130"
```
Исключение: число уже поступало
```
curl -X POST "http://localhost:80/save?value=130"
```
Исключение: число, увеличенное на 1 уже поступало
```
curl -X POST "http://localhost:80/save?value=129"
```
### Завершение работы
```
docker compose down
```
