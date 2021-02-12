import logging
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.cache import cache
from django.core.exceptions import ValidationError

from urllib.parse import urlparse

from .forms import NameForm
from pages.scripts.plots import heatmap

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
        imdb_url = cache.get('imdb_url')
        result = heatmap(imdb_url)
        if result.error == True:
            pass
        else:
            result.error = cache.get('Error')
            result.error_message = "Please enter a valid IMDB TV show link (example: https://www.imdb.com/title/tt5753856/?ref_=nv_sr_srsg_3)"
        print("\n\nresult.error:\n{}\nresult.error_message:\n{}\n\n".format(result.error, result.error_message))
        context['Error_Bool'] = result.error
        context['Error_Message'] = result.error_message
        context['form'] = NameForm()
        context['plot'] = result.Plot
        return context

    def post(self,request, *args, **kwargs):
        form = NameForm(request.POST)
        url_link = form.data.get("forms_url")
        print(url_link)
        if form.is_valid() and (url_link.find("https://www.imdb.com/title/tt") == 0 or url_link.find("imdb.com/title/tt") == 0 or url_link.find("https://m.imdb.com/title/tt") == 0 or url_link.find("m.imdb.com/title/tt") == 0):
            cache.set('imdb_url', url_link,3000)
            cache.set('Error', False, 3000)
            return HttpResponseRedirect('/')
        else:
            form = NameForm()
            cache.set('imdb_url', None,3000)
            cache.set('Error', True, 3000)
            # return render(request, 'base.html', {'form': form})
            return HttpResponseRedirect('/')

