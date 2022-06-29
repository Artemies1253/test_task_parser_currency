from contextlib import contextmanager
from datetime import timezone, datetime

import sqlite3


@contextmanager
def open_cursor_sqlite3():
    connect = sqlite3.connect("db.sqlite3")
    cursor = connect.cursor()
    yield cursor
    cursor.close()


def utc_to_local(utc_dt: datetime):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
