import sqlite3
from pprint import pprint
import sys
import argparse


def convert_date_by_sql(date_from, date_to):
    """Конвертирует дату, для того что бы её можно было использовать в SQL запросе
    Дата должна передаваться в формате dd.mm.yyyy
    """
    try:
        day_from, month_from, year_from = date_from.split(".")
        day_to, month_to, year_to = date_to.split(".")
        date_from = f"{year_from}-{month_from}-{day_from}"
        date_to = f"{year_to}-{month_to}-{day_to}"
        return date_from, date_to
    except Exception as ex:
        print("Дата должна передаваться в формате dd.mm.yyyy")
        print(ex)
        return False


def minmax(kind_currency, date_from, date_to):
    sql_date = convert_date_by_sql(date_from, date_to)
    if sql_date:
        date_from, date_to = sql_date
    else:
        return False

    connect = sqlite3.connect("db.sqlite3")
    cursor = connect.cursor()
    try:
        sql = f"SELECT MAX(quotation.high_value), MIN(quotation.low_value) " \
              f"FROM parsers_quotation as quotation " \
              f"WHERE quotation.date >= '{date_from}' AND quotation.date <= '{date_to}' AND " \
              f"money_id = (SELECT money.id FROM parsers_money as money WHERE money.name = '{kind_currency}')"
        response = cursor.execute(sql)
        values = response.fetchall()
        max_currency, min_currency = values[0]
        print(f"MIN = {min_currency}")
        print(f"MAX = {max_currency}")
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()


def list(kind_currency, date_from, date_to, limit=None):
    """Выводит количество и список значений закрытий свечей
    Дата должна передаваться в формате dd.mm.yyyy
    """
    print("start")
    print(date_from)
    print(type(date_from))

    print(date_to)
    print(type(date_to))
    sql_date = convert_date_by_sql(date_from, date_to)
    if sql_date:
        date_from, date_to = sql_date
    else:
        return False

    connect = sqlite3.connect("db.sqlite3")
    cursor = connect.cursor()
    try:
        sql = f"SELECT quotation.close_value " \
              f"FROM parsers_quotation as quotation " \
              f"WHERE quotation.date >= '{date_from}' AND quotation.date <= '{date_to}' AND " \
              f"money_id = (SELECT money.id FROM parsers_money as money WHERE money.name = '{kind_currency}')"
        response = cursor.execute(sql)
        values = response.fetchall()

        if limit:
            count_value = 0
            for value in values:
                count_value += 1
                print(f"{count_value}. {round(value[0], 2)}")
                if count_value == limit:
                    break
        else:
            for i, value in enumerate(values):
                pass
                print(f"{i+1}. {round(value[0], 2)}")

    except Exception as ex:
        print(ex)
    finally:
        cursor.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('func', type=str)
    parser.add_argument('currency', type=str)
    parser.add_argument('date_from', type=str)
    parser.add_argument('date_to', type=str)
    parser.add_argument('--limit', type=int)
    arguments = parser.parse_args()
    globals()[arguments.func](arguments.currency, arguments.date_from, arguments.date_to, arguments.limit)
