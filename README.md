# Система учета компьютерного клуба

Flask приложение для учета клиентов, договоров и оборудования компьютерного клуба.

## Технологии
- Backend: Python, Flask
- База данных: SQLite
- Интерфейс: HTML шаблоны (Jinja2)
- Документы: генерация DOCX чеков

## Функциональность
- Управление клиентами, сотрудниками, филиалами
- Учет сеансов и договоров  
- Генерация чеков в формате DOCX
- Просмотр истории сеансов

## Запуск
```bash
# Создание виртуального окружения
python -m venv venv


# Активация
# (Linux/Mac)
source venv/bin/activate
# (Windows)
venv\Scripts\activate


# Зависимости
pip install -r requirements.txt


python init_db.py
python app.py
