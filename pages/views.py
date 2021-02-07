import logging
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.cache import cache

from .forms import NameForm
from . import plots

logger = logging.getLogger(__name__)



class HeatmapView(TemplateView):
    template_name = "base.html"

    def __init__(self):
        super().__init__()
        self.data = None

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HeatmapView, self).get_context_data(**kwargs)
        # print('self.data (get_context_data):\n{}\n\n'.format(self.data))
        print('cache:\n{}\n\n'.format(cache.get('data')))
        imdb_url = cache.get('data')
        context['form'] = NameForm()
        context['plot'] = plots.heatmap(imdb_url)
        return context

    def post(self,request, *args, **kwargs):
        form = NameForm(request.POST)
        cache.set('data', form.data.get("forms_url"),3000)
        print('self.data (post) before assingment:\n{}\n\n'.format(self.data))
        # self.data = form.data.get("forms_url")
        # context = self.get_context_data()
        print('self.data (post) after assingment:\n{}\n\n'.format(self.data))
        return HttpResponseRedirect('/')
        # return render(request, 'base.html', {'form': form})



# class HeatmapView(TemplateView):
#     template_name = "plot.html"

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(HeatmapView, self).get_context_data(**kwargs)
#         context['plot'] = plots.heatmap()
#         return context