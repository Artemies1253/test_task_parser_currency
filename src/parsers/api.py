from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Max, Min

from src.parsers.serializers import MinMaxQuotationSerializer, DetailQuotationSerializer, DetailMoneySerializer
from src.parsers.models import Quotation, Money


class QuotationMinMaxAPIView(generics.GenericAPIView):
    serializer_class = MinMaxQuotationSerializer

    def get(self, request):
        serializer = self.serializer_class(data=request.GET)
        if serializer.is_valid(raise_exception=True):
            queryset = Quotation.objects.filter(
                money__name=serializer.validated_data.get("money_name"),
                date__lt=serializer.validated_data.get("date_to"),
                date__gt=serializer.validated_data.get("date_from"),
            )
            result = queryset.aggregate(
                max=Max("high_value"),
                min=Min("low_value")
            )
            result["min"] = round(result.get("min"), 2)
            result["max"] = round(result.get("max"), 2)

            return Response(result)


class ListQuotationAPIView(generics.GenericAPIView):
    serializer_class = DetailQuotationSerializer

    def get(self, request):
        queryset = self.get_queryset()
        serializer = DetailQuotationSerializer(queryset, many=True)

        return Response(
            {
                "count": len(queryset),
                "data": serializer.data
            }
        )

    def get_queryset(self):
        serializer = MinMaxQuotationSerializer(data=self.request.GET)
        if serializer.is_valid(raise_exception=True):
            queryset = Quotation.objects.filter(
                money__name=serializer.validated_data.get("money_name"),
                date__lt=serializer.validated_data.get("date_to"),
                date__gt=serializer.validated_data.get("date_from"),
            ).select_related("money")
            return queryset


class ListMoneyAPIView(generics.ListAPIView):
    serializer_class = DetailMoneySerializer
    queryset = Money.objects.all()
