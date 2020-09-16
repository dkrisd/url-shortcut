from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Url
# from django.core import serializers


def all_url_shortcuts(request):
    # data = serializers.serialize('json', Url.objects.all())
    items = Url.objects.all()
    template = loader.get_template('index.html')
    context = {
        'item_list': items,
    }
    return HttpResponse(template.render(context, request))


def redirect_shortcut(request, shortcut):
    print(shortcut)
    try:
        item = Url.objects.get(url_shortcut=shortcut)
        return HttpResponseRedirect(item.url)
    except Url.DoesNotExist:
        raise Http404
