from django.shortcuts import render

# Create your views here.

def post_view(request):
    x = 'none'
    if request.method == 'POST':
        g = request.POST   
        print(g)
        print(g['nume-post'])
        print(len(g['nume-post']))
        if len(g['nume-post']) > 0:
            x = ", ".join([_[1] for _ in [_ for _ in g.items()] if len(_[1])>0][1:])
    response = {
        'response_from': f'post_main = {x}'
    }
    return render(request, "index.html", response)