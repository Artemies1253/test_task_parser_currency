from enum import Enum


class PeriodInvestingComEnum(Enum):
    one_minute = "1"
    five_minutes = "5"
    quarter = "15"
    half_hour = "30"
    quarter_to_hour = "45"
    hour = "60"
    two_hours = "120"
    four_hours = "240"
    five_hour = "300"
    day = "D"
    week = "W"
    mouth = "M"

    @staticmethod
    def get_list_value():
        return [name.value for name in PeriodInvestingComEnum]


class ValueInvestingComEnum(Enum):
    USD_RUB = "2186"
    USD_JPY = "3"
    USD_CHF = "4"
    USD_CAD = "7"
    NZD_USD = "8"
    JPY_RUB = "9785"
    GBP_USD = "2"
    EUR_USD = "1"
    EUR_RUB = "1691"
    EUR_JPY = "9"
    EUR_GBP = "6"
    EUR_CHF = "10"
    EUR_AUD = "15"
    DX = "8827"
    BTC_USD = "945629"
    AUD_USD = "5"

    @staticmethod
    def get_list_value():
        return [name.value for name in ValueInvestingComEnum]

    @staticmethod
    def get_list_name():
        return [name.name for name in ValueInvestingComEnum]

    @staticmethod
    def get_list():
        return [name.value for name in ValueInvestingComEnum]
