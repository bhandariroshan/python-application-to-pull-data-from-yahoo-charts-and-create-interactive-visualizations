"""Class for views."""

from dataplot.models import ChartData
from dataplot.serializers import ChartDataSerializer

import pandas as pd

from rest_framework import generics
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

# import datetime


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
        chart_type = self.kwargs['chart_type'].replace('/', '')

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
        elif time == 'max':
            filter_number = 365 * 30

        data = ChartData.objects.filter(
            ticker__icontains=ticker
        ).order_by('-date')[0:filter_number]

        list_data = []
        for each_data in data:
            list_data.append({
                'date': each_data.date,
                # 'open_value': each_data.open_value,
                # 'close_value': each_data.close_value,
                # 'high_value': each_data.high_value,
                # 'low_value': each_data.low_value,
                'ticker': each_data.ticker,
                'adj_close': each_data.adj_close,
            })

        list_data = sorted(list_data, key=lambda k: k['date'])
        df = pd.DataFrame(list_data)
        df = df.set_index("date")
        df.fillna(method="ffill", inplace="True")
        df.fillna(method="bfill", inplace="True")

        if chart_type == 'sma':
            roling_mean_df = self.get_rolling_mean(df['adj_close'], 10)
            roling_sd_df = self.get_rolling_std(df['adj_close'], 10)
            roling_mean_df = roling_mean_df.dropna()
            roling_mean_df.rename('adj_close')
            data = roling_mean_df.to_dict()
            return_data = [
                {'date': d.strftime("%Y-%m-%d"), 'adj_close': v}
                for d, v in data.items()
            ]
            newlist = sorted(return_data, key=lambda k: k['date'])
            return Response(newlist)

        elif chart_type == "bollinger":
            roling_mean_df = self.get_rolling_mean(df['adj_close'], 10)
            roling_sd_df = self.get_rolling_std(df['adj_close'], 10)
            bollinger_band_upper_df, bollinger_band_lower_df = self.get_bollinger_bands(
                roling_mean_df, roling_sd_df
            )

            bollinger_band_upper_df = roling_mean_df.dropna()
            bollinger_band_upper_df.rename('adj_close')
            bfu_data = bollinger_band_upper_df.to_dict()

            bollinger_band_lower_df = bollinger_band_lower_df.dropna()
            bollinger_band_lower_df.rename('adj_close')
            bfl_data = bollinger_band_lower_df.to_dict()

            b_upper = [
                {'date': d.strftime("%Y-%m-%d"), 'adj_close': v}
                for d, v in bfu_data.items()
            ]

            b_lower = [
                {'date': d.strftime("%Y-%m-%d"), 'adj_close': v}
                for d, v in bfl_data.items()
            ]

            b_upper_sorted = sorted(b_upper, key=lambda k: k['date'])
            b_lower_sorted = sorted(b_lower, key=lambda k: k['date'])

            return Response({'upper': b_upper_sorted, 'lower': b_lower_sorted})


class ChartMultiTickerViewSet(APIView):
    """docstring for ChartMultiTickerViewSet"""
    serializer_class = ChartDataSerializer

    def get(self, request):
        """Return a list of all the data."""
        tickers = self.request.GET['tickers'].split(',')
        time = self.request.GET['time'].replace('/', '')
        tickers = [item.lower() for item in tickers]
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
        elif time == 'max':
            filter_number = 365 * 30

        returndata = {}
        for each_ticker in tickers:
            data = ChartData.objects.filter(
                ticker__icontains=each_ticker
            ).order_by('-date')

            for each_data in data:
                if each_data.ticker in returndata.keys():
                    if len(returndata[each_data.ticker]) < filter_number:
                        returndata[each_data.ticker].append({
                            'adj_close': each_data.adj_close,
                            'date': str(each_data.date)
                        })
                else:
                    returndata[each_data.ticker] = [{
                        'adj_close': each_data.adj_close,
                        'date': str(each_data.date)
                    }]

        return Response(returndata)


class ChartDataViewSet(generics.ListAPIView):
    """Chart Data view set."""

    serializer_class = ChartDataSerializer

    def get_queryset(self):
        """Return a list of all the data."""
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
        elif time == 'max':
            filter_number = 365 * 30
        data = ChartData.objects.filter(
            ticker__icontains=ticker
        ).order_by('-date')[0:filter_number]
        return data
