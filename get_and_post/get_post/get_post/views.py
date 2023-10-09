from django.shortcuts import render


def index_view(request):
    # if request.method == 'POST':
    #     g = request.POST   
    #     print(g)
    #     print(g['nume-post'])
    response = {
        'response_from': 'project_main'
    }
    return render(request, "index.html", response)