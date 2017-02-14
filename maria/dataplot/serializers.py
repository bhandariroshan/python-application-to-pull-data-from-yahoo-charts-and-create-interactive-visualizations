"""Serializers for Chart Data."""
from rest_framework import serializers
from dataplot.models import ChartData


class ChartDataSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for chart data."""

    class Meta:
        """Meta class."""

        model = ChartData
        fields = (
            'ticker',
            'date',
            'open_value',
            'close_value',
            'high_value',
            'low_value',
            'volume',
            'adj_close'
        )
