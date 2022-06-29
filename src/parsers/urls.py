from django.urls import path

from src.parsers.api import QuotationMinMaxAPIView, ListQuotationAPIView, ListMoneyAPIView

urlpatterns = [
    path("minmax", QuotationMinMaxAPIView.as_view()),
    path("list", ListQuotationAPIView.as_view()),
    path("money_list", ListMoneyAPIView.as_view())
]
