from contextlib import contextmanager

import sqlite3


@contextmanager
def open_cursor():
    connect = sqlite3.connect("db.sqlite3")
    cursor = connect.cursor()
    yield cursor
    cursor.close()
