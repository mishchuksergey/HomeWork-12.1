# Домашняя работа 12.1 «Библиотеки для Python-разработчика»

## Цель проекта

* Рассмотреть, что такое JSON.
* Рассмотреть методы loads и dumps.
* Познакомиться с библиотекой requests. 
* Познакомитесь с библиотекой datetime.
* Разобраться в тестировании Mock и patch.

## Инструкция по установке

1. Клонируйте репозиторий:

   git@github.com:mishchuksergey/HomeWork-12.1.git

2. Установите зависимости:

    pip install -r requirements.txt

### Новые функции

   В домашнем задании добавлен новый модуль *utils.py*, в котором 
   реализованы новые функции:

    - convert_transactions - Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    - transaction_amount - Функция возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    
   В домашнем задании добавлен новый модуль *external_api.py*, в котором 
   реализована новая функция:
     - convert_current - Функция обращается к внешнему API и производит конвертацию валюты.


##Тестирование

Тестирование функций проводится с помощью фреймворка ***pytest***.
Для установки наберите в консоли:

    pip install pytest


*Добавлены следующие модули для тестирования функций:*
- *test_log*


Тесты используют фикстуры из модуля ***conftest.py***, а также параметризацию.
В докстрингах тестов приведены краткие описания их работы.

### **Покрытие тестами (coverage) составляет 94%**.
Более подробная информация по покрытию каждого модуля представлена в директории ***htmlcov***.

## Лицензия