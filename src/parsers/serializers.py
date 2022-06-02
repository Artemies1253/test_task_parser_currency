from rest_framework import serializers

from src.parsers.enums import ValueInvestingComEnum
from src.parsers.models import Quotation, Money


class MinMaxQuotationSerializer(serializers.Serializer):
    money_name = serializers.ChoiceField(ValueInvestingComEnum.get_list_name())
    date_from = serializers.DateTimeField()
    date_to = serializers.DateTimeField()


class DetailMoneySerializer(serializers.ModelSerializer):

    class Meta:
        model = Money
        fields = "__all__"


class DetailQuotationSerializer(serializers.ModelSerializer):
    money = DetailMoneySerializer()

    class Meta:
        model = Quotation
        fields = "__all__"
