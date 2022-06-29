from datetime import datetime, timedelta
import pytz

from django.core.management.base import BaseCommand

from src.parsers.investing_com import Parser
from src.parsers.enums import ValueInvestingComEnum, PeriodInvestingComEnum
from src.parsers.models import Money, Quotation


class Command(BaseCommand):
    """Заполняет базу данных за последний полгода c сайта investing_com, период заполнения 1 час"""

    def handle(self, *args, **kwargs):
        date_to = datetime.utcnow()
        date_from = date_to - timedelta(weeks=1*4*6)
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
                if quotation_model[1]:
                    count_quotation += 1
            print(f"У валюты {money.name} записано {count_quotation} котировок")
