# Построение распределенных систем и облачных вычислений
## Ачивка 2
### Диаграмма компонентов
![Component_diagram](https://github.com/user-attachments/assets/48e765bc-9d93-4206-866e-623ed111ecc9)
### Диаграмма последовательностей
![Sequence_diagram](https://github.com/user-attachments/assets/9b6cf696-0bd8-49e4-8ba7-e25bfc15b179)
### Использование
#### Запустить
```
docker compose up --build -d
```
#### Проверка работы
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
#### Завершение работы
```
docker compose down
```
