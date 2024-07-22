from django.http import JsonResponse
import json
import  pro


def api_home(request, *args, **kwargs):
    body = request.body
    print(body)
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['headers'] = dict(request.headers)
    print(request.headers)
    return JsonResponse(data)
