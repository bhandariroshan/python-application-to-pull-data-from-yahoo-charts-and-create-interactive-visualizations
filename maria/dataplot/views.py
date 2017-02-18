"""Class for views."""

from dataplot.models import ChartData
from dataplot.serializers import ChartDataSerializer
from rest_framework import generics
import datetime


class ChartDataViewSet(generics.ListAPIView):
    serializer_class = ChartDataSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        ticker = self.kwargs['ticker']
        time = self.kwargs['time'].replace('/', '')

        filter_number = 365
        print(time)
        if time == '1m':
            filter_number = 30
        elif time == '2m':
            filter_number = 60
        elif time == '3m':
            filter_number = 90
        elif time == '6m':
            filter_number = 180
        elif time == '1Y':
            filter_number = 365
        elif time == '2Y':
            filter_number = 365 * 2
        elif time == '5Y':
            filter_number = 365 * 5
        elif time == '10Y':
            filter_number = 365 * 10
        data = ChartData.objects.filter(
            ticker=ticker,
            date__lte=datetime.datetime.today()
        ).order_by('-date')[0:filter_number]
        print(len(data))
        return data
