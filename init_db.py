import sqlite3

connection = sqlite3.connect('database.db')
cur = connection.cursor()

# Создание таблиц
cur.execute("""CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone_number TEXT,
    position TEXT,
    chief_id INTEGER,
    branch_id INTEGER,
    FOREIGN KEY (branch_id) REFERENCES branch(id)
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone_number TEXT
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS branch (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT,
    branch_name TEXT
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS contracts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numbers TEXT,
    dates TEXT,
    price INTEGER,
    discount INTEGER,
    device_status TEXT,
    device_id INTEGER,
    client_id INTEGER,
    employee_id INTEGER,
    finish_price INTEGER,
    FOREIGN KEY (client_id) REFERENCES client(id),
    FOREIGN KEY (employee_id) REFERENCES employee(id),
    FOREIGN KEY (device_id) REFERENCES device(id)
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS device (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT,
    branch_id INTEGER,
    client_id INTEGER,
    FOREIGN KEY (branch_id) REFERENCES branch(id),
    FOREIGN KEY (client_id) REFERENCES client(id)
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    date TEXT,
    report_type TEXT,
    description TEXT,
    employee_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employee(id)
)""")


# Филиалы
cur.execute("INSERT INTO branch (address, branch_name) VALUES (?, ?)",
            ('г. Москва, ул. Солнечная, д.13б', 'COLIZEUM Солнечная'))

# Сотрудники
cur.execute("INSERT INTO employee (name, email, phone_number, position, chief_id, branch_id) VALUES (?, ?, ?, ?, ?, ?)",
            ('Петрова Полина Сергеевна', 'petrova@adminka.ru', '80001234567', 'администратор', None, 1))

# Клиенты
cur.execute("INSERT INTO client (name, email, phone_number) VALUES (?, ?, ?)",
            ('Второй Марк Тайетович', 'markII@ya.ru', '89151234567'))

cur.execute("INSERT INTO client (name, email, phone_number) VALUES (?, ?, ?)",
            ('Михайлов Владимир Степанович', 'mvs2020@ya.ru', '89170001234'))

# Устройства
cur.execute("INSERT INTO device (address, branch_id, client_id) VALUES (?, ?, ?)",
            ('Зал A, место 1', 1, None))  # client_id может быть NULL

# Контракты
cur.execute("INSERT INTO contracts (numbers, dates, price, discount, device_status, device_id, client_id, employee_id, finish_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('COL-001', '01.04.2024', 180, 10, 'Норма', 1, 1, 1, 162))

cur.execute("INSERT INTO contracts (numbers, dates, price, discount, device_status, device_id, client_id, employee_id, finish_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('COL-002', '01.06.2024', 220, 20, 'Норма', 1, 2, 1, 176))

connection.commit()
connection.close()

print("База данных успешно создана и заполнена тестовыми данными!")
print("Теперь можно запускать Flask приложение")