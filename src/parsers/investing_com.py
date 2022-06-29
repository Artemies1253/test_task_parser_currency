from datetime import datetime

import requests

from src.parsers.enums import PeriodInvestingComEnum, ValueInvestingComEnum
from services import utc_to_local

class Parser:
    def __init__(
            self, data_from: datetime, data_to: datetime, period: PeriodInvestingComEnum, value: ValueInvestingComEnum
    ):
        """
        :param data_from: Дата от которой нужно парсить
        :param data_to: Дато по которую нужно парсить
        :param period: Детализация парсера
        :param value: Валюта какую нужно парсить
        """
        self.data_from = data_from
        self.data_to = data_to
        self.period = period
        self.value = value
        self.date = []

    def run(self):
        response = self.get_response()
        if response:
            self.extract_data(response)
        return self.date


    def get_response(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
        }
        url = f"https://tvc4.investing.com/ecb21e46c4492fa8a869ca2c7a435905/1654103361/7/7/18/history?"\
              f"symbol={self.value}&"\
              f"from={int(self.data_from.timestamp())}&"\
              f"to={int(self.data_to.timestamp())}&" \
              f"resolution={self.period}"
        response = requests.get(
            url=url,
            headers=headers
        )
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def extract_data(self, response: dict):
        for i, close_value in enumerate(response.get("c")):
            self.date.append(
                {
                    "close_value": close_value,
                    "date": utc_to_local(datetime.utcfromtimestamp(float(response.get("t")[i]))),
                    "open_value": response.get("o")[i],
                    "high_value": response.get("h")[i],
                    "low_value": response.get("l")[i]
                }
            )
