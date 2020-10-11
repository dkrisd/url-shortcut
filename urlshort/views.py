from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Url
from .forms import LoginForm, CreateUrlForm
# from django.core import serializers


def all_url_shortcuts(request):
    # data = serializers.serialize('json', Url.objects.all())
    items = Url.objects.all()
    template = loader.get_template('index.html')
    context = {
        'item_list': items,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "index.html", context)


def redirect_shortcut(request, shortcut):
    print(shortcut)
    try:
        item = Url.objects.get(url_shortcut=shortcut)
        return HttpResponseRedirect(item.url)
    except Url.DoesNotExist:
        raise Http404

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                context = {
                    'auth_result': "success",
                }
                return render(request, "login.html", context)
                
            else:
                # Return an 'invalid login' error message.
                context = {
                    'auth_result': "invalid",
                }
                return render(request, "login.html", context)
    else:
        if request.user.is_authenticated:
            # Redirect to a success page.
            context = {
                'auth_result': "already_logged",
            }
            return render(request, "login.html", context)
        else:
            # Show login form for AnonymousUser.
            # context = {
            #     'auth_result': "",
            # }
            # return render(request, "login.html", context)
            form = LoginForm()
            return render(request, 'login.html', {'form': form})


def create_url(request):
    form = CreateUrlForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateUrlForm()

    context = {
        'form' : form
    }
    return render(request, "create-url.html", context)