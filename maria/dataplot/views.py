"""Class for views."""

from dataplot.models import ChartData
from dataplot.serializers import ChartDataSerializer

import pandas as pd

from rest_framework import generics
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

import datetime


class ChartDataMathsViewSet(APIView):
    """docstring for ExamRedirectAPI."""

    renderer_classes = (JSONRenderer, )
    url_name = 'entrance:api:question_stats'

    def get_rolling_mean(self, values, window):
        """Return rolling mean of given values, using specified window size."""
        return values.rolling(window=window).mean()

    def get_rolling_std(self, values, window):
        """Return rolling SD of given values, for specified window size."""
        return values.rolling(window=window).std()

    def get_bollinger_bands(self, rm, rstd):
        """Return upper and lower Bollinger Bands."""
        upper_band = rm + 2 * rstd
        lower_band = rm - 2 * rstd
        return upper_band, lower_band

    def get(self, request, chart_type, ticker, time, *args, **kwargs):
        """Return Question Stats."""
        ticker = self.kwargs['ticker']
        time = self.kwargs['time'].replace('/', '')

        filter_number = 365
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
            ticker__icontains=ticker,
            date__lte=datetime.datetime.today()
        ).order_by('-date')[0:filter_number]

        list_data = []
        for each_data in data:
            list_data.append({
                'date': each_data.date,
                'open_value': each_data.open_value,
                'close_value': each_data.close_value,
                'high_value': each_data.high_value,
                'low_value': each_data.low_value,
                'ticker': each_data.ticker,
                'adj_close': each_data.adj_close,
            })

        df = pd.DataFrame(list_data)
        new_df = self.get_rolling_mean(df, 10)
        new_df = new_df.fillna(0)
        new_df = new_df.to_json()

        return Response(new_df)


class ChartDataViewSet(generics.ListAPIView):
    """Chart Data view set."""

    serializer_class = ChartDataSerializer

    def get_queryset(self):
        """Return a list of all the data."""
        print("GETTTTTTTrrrrrrrrrrrrrrr")
        ticker = self.kwargs['ticker']
        time = self.kwargs['time'].replace('/', '')

        filter_number = 365
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
            ticker__icontains=ticker,
            date__lte=datetime.datetime.today()
        ).order_by('-date')[0:filter_number]
        return data
