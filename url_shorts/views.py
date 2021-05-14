from django.shortcuts import render, redirect
import uuid

import url_shorts
from url_shorts.models import Input, Urls
from .forms import InputForm


# Create your views here.
def index(request):

    context = {}
    site = '127.0.0.1:8000/'

    # return blank form if its a GET or other request
    if request.method != 'POST':
        form = InputForm()
        context['form'] = form
        return render(request, 'index.html', context)
    # if its a POST
    else:
        form = InputForm(data=request.POST)
        url_info = request.POST['url']
        print('url info: ' + url_info)
        if Input.objects.filter(url=url_info).exists():
            urls_obj = Urls.objects.get(url=url_info)
            print('exists - uuid: ' + urls_obj.uuid)
            context['data'] = site + urls_obj.uuid
        elif form.is_valid():
            print('is valid')
            uid = str(uuid.uuid4())[:5]
            new_url = Urls(url=url_info, uuid=uid)
            new_url.save()
            form.save()
            context['data'] = site + uid
        else:
            print('URL is not valid')
    context['form'] = form
    return render(request, 'index.html', context)


def is_website(url: str) -> bool:
    website_regex_pattern = r"^(https?\:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})(\/[\w]*)*$"
    pass


def shorten(request):
    pass


def go(request, url_hash):
    url_details = Urls.objects.get(uuid=url_hash)
    return redirect('http://' + url_details.url)

