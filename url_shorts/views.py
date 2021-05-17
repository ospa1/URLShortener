from django.shortcuts import render, redirect
import uuid
from django.http import Http404
import url_shorts
from url_shorts.models import Input, Urls
from .forms import InputForm


# Create your views here.
def index(request):

    context = {}
    local_site = '127.0.0.1:8000/'
    site = 'url-short2.herokuapp.com/'

    # return blank form if its a GET or other request
    if request.method != 'POST':
        form = InputForm()
        context['form'] = form
        return render(request, 'index.html', context)
    # if its a POST, process data
    else:
        form = InputForm(data=request.POST)
        url_info = request.POST['url']
        print('url info: ' + url_info)

        # check if url already exists
        if Input.objects.filter(url=url_info).exists():
            urls_obj = Urls.objects.get(url=url_info)
            print('exists - uuid: ' + urls_obj.uuid)
            context['data'] = site + urls_obj.uuid

        # if url does not exist save it if valid
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
    print('request.method: ' + request.method)  # has to be GET
    print('url_hash: ' + url_hash)
    try:
        url_details = Urls.objects.get(uuid=url_hash)
    except url_shorts.models.Urls.DoesNotExist:
        msg = "Page Not Found"
        raise Http404(msg)
    return redirect('http://' + url_details.url)

