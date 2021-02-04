import logging
from django.views.generic import TemplateView
from . import plots

logger = logging.getLogger(__name__)



class HeatmapView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HeatmapView, self).get_context_data(**kwargs)
        context['plot'] = plots.heatmap()
        return context