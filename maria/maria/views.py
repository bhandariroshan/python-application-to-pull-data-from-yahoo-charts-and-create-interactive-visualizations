"""View for dashboard."""

from django.shortcuts import render
# from django.http import HttpResponseRedirect, Http404
from django.views.generic import TemplateView
from dataplot.models import ChartData


class HomeView(TemplateView):
    """Home page for students."""

    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        """Method for get request of home page."""
        t = ChartData.objects.values('ticker').distinct()
        selected_ticker = 'IVZ'
        tickers = []
        for each_t in t:
            if len(each_t['ticker']) <= 1:
                tickers.append(each_t['ticker'])

        tickers = sorted(tickers)
        return render(
            request,
            self.template_name,
            {
                'tickers': tickers,
                'selected': selected_ticker
            }
        )
