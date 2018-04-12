from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
# Create your views here.

port = 10085


def main(request):
    context = {}
    return render(request, 'crawl_app/main.html', context)


def insert(request):
    seed = request.POST.get('data')
    ack = requests.post('http://127.0.0.1:%s/insert' % port, data={'data': seed}).text
    return JsonResponse({"data": ack})


def check(request):
    seed = json.loads(request.POST.get('data'))
    mode = {
        'url': seed['url'],
        'mode_data': seed['temp_parent']['model']
    }
    context = {'data': json.dumps(dict(mode))}
    res = requests.post('http://127.0.0.1:%s/parse' % port, data=context).text
    res = json.loads(res)
    return JsonResponse({'data': res})
