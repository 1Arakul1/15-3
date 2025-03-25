# Создание базы данных NorthWind и заполнение таблиц данными из CSV с использованием Python

## Описание проекта

Этот проект содержит Python-скрипт (`northwind_db.py`), который автоматизирует создание базы данных `NorthWind` в Microsoft SQL Server и заполнение трех таблиц (`customers_data`, `employees_data`, `orders_data`) данными, полученными из CSV-файлов.

## Файлы проекта

*   `northwind_db.py`: Основной Python-скрипт для создания базы данных, таблиц и импорта данных.
*   `requirements.txt`: Список зависимостей Python, необходимых для работы скрипта.
*   `customers_data.csv`: CSV-файл с данными о клиентах.
*   `employees_data.csv`: CSV-файл с данными о сотрудниках.
*   `orders_data.csv`: CSV-файл с данными о заказах.
*   `screenshots/`: Папка, содержащая скриншоты таблиц в SQL Server Management Studio, подтверждающие успешную загрузку данных.

## Зависимости

Для запуска скрипта необходимы следующие библиотеки Python:

*   `pyodbc`
*   `pandas`

## Инструкция по установке и запуску

1.  Установите зависимости Python:

    ```bash
    pip install -r requirements.txt
    ```

2.  Отредактируйте файл `northwind_db.py` и укажите свои параметры подключения к SQL Server:

    ```python
    SERVER = 'DESKTOP-AM0MSA0\\SQLEXPRESS'  # Замените на свой сервер
    DATABASE = 'NorthWind'
    USERNAME = 'Hakimov'  # Замените на своё имя пользователя
    PASSWORD = 'NIAZrezeda12'  # Замените на свой пароль
    ```

3.  Запустите скрипт:

    ```bash
    python northwind_db.py
    ```

## Скриншоты

В папке `screenshots/` находятся скриншоты, демонстрирующие успешно заполненные таблицы в базе данных `NorthWind`.

## Информация об авторе

[Здесь можно указать ваше имя]