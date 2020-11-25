from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# def index(request):
#     context = {
#     	"name": "Noelle",
#     	"favorite_color": "turquoise",
#     	"pets": ["Bruce", "Fitz", "Georgie"]
#     }
#     return render(request, "index.html", context)

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)