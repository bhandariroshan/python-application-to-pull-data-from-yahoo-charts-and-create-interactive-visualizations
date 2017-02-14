"""View for dashboard."""

from django.shortcuts import render
# from django.http import HttpResponseRedirect, Http404
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page for students."""

    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        """Method for get request of home page."""
        return render(
            request,
            self.template_name,
            {}
        )
