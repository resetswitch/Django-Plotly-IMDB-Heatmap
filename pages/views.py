import logging
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.cache import cache
from django.core.exceptions import ValidationError

from urllib.parse import urlparse

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
        print('cache:\n{}\n\n'.format(cache.get('data')))
        imdb_url = cache.get('data')
        context['form'] = NameForm()
        context['plot'] = plots.heatmap(imdb_url)
        return context

    def post(self,request, *args, **kwargs):
        form = NameForm(request.POST)
        url_data = form.data.get("forms_url")
        print(url_data)
        if form.is_valid() and bool('imdb.com/title/tt' in url_data):
            cache.set('data', url_data,3000)
            return HttpResponseRedirect('/')
        else:
            form = NameForm()
            cache.set('data', None,3000)
            # return render(request, 'base.html', {'form': form})
            return HttpResponseRedirect('/')


    def validate_url(self, value):
        obj = urlparse(value)
        if not obj.hostname in ('imdb.com/title/tt'):
            raise ValidationError('Only urls from YouTube or SoundCloud allowed')
        else:
            return True

# class HeatmapView(TemplateView):
#     template_name = "plot.html"

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(HeatmapView, self).get_context_data(**kwargs)
#         context['plot'] = plots.heatmap()
#         return context