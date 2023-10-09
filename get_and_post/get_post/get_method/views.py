from django.shortcuts import render

# Create your views here.


def get_view(request):
    x = 'none'
    if request.method == 'GET':
        g = request.GET
        print(g)
        print(g['nume-get'])
        if len(g['nume-get']) > 0:
            x = len(g['nume-get'])
    response = {
        'response_from': f'get_main = {x}'
    }
    return render(request, "index.html", response)