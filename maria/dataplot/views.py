"""Class for views."""

from dataplot.models import ChartData
from dataplot.serializers import ChartDataSerializer
from rest_framework import generics


class ChartDataViewSet(generics.ListAPIView):
    serializer_class = ChartDataSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        ticker = self.kwargs['ticker']
        return ChartData.objects.filter(ticker=ticker).order_by('date')
