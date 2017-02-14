"""Data Storage."""

import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from dataplot.managers import ChartDataManager


class ChartData(models.Model):
    """Exam Evaluation criteria for terminal exams."""

    # Attributes
    date = models.DateField(auto_now=False, auto_now_add=False)
    ticker = models.CharField(max_length=50, null=True, blank=True)
    sector = models.CharField(max_length=50, null=True, blank=True)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    open_value = models.CharField(max_length=50)
    high_value = models.FloatField()
    low_value = models.FloatField()
    close_value = models.FloatField()
    volume = models.FloatField()
    adj_close = models.FloatField()

    # Object Manager
    objects = ChartDataManager()

    # Meta and Strings
    class Meta:
        """Meta Data and String."""

        verbose_name = _("Data")
        verbose_name_plural = _("Data")

    def __str__(self):
        """Default function."""
        return ""
