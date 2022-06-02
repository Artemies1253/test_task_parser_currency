from datetime import datetime
from pprint import pprint

from django.core.management.base import BaseCommand
import pytz

from src.parsers.investing_com import Parser
from src.parsers.enums import ValueInvestingComEnum, PeriodInvestingComEnum
from src.parsers.models import Money, Quotation


class Command(BaseCommand):
    """Заполняет базу данных от 1 января 2022 года до текущей даты с сайта investing_com, переод заполнения 1 час"""

    def handle(self, *args, **kwargs):
        date_from = datetime(2022, 1, 1)
        date_to = datetime.utcnow()
        moneys = ValueInvestingComEnum

        for money in moneys:
            money_model = Money.objects.get_or_create(name=money.name)
            parser = Parser(
                data_from=date_from,
                data_to=date_to,
                period=PeriodInvestingComEnum.hour.value,
                value=money.value
            )
            result = parser.run()
            count_quotation = 0
            for quotation in result:
                quotation_model = Quotation.objects.get_or_create(
                    money=money_model[0],
                    **quotation
                )
                count_quotation += 1
            print(f"У валюты {money.name} записано {count_quotation} котировок")
