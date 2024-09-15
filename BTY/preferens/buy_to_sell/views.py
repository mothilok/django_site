from django.shortcuts import render
from .models import Poster

def home(request):
    request_bd = Poster.objects.order_by('-date_published')[:5]
    context = {
        'data':request_bd
    }
    return render(request, "buy_to_sell/home.html", context)

def post(request, post_id):
    request_bd = Poster.objects.get(pk=post_id)
    context = {
        'data':request_bd
    }
    return render(request, "buy_to_sell/post.html", context)


def create_poster(request):
    request_post = request.POST
    if request.method == "POST":
        create_poster = Poster()
        create_poster.title = request_post['create_title']
        create_poster.description = request_post['create_description']
        create_poster.price = request_post['create_price']
        create_poster.image = request.FILES['create_image']
        create_poster.phone_number = request_post['create_number']
        create_poster.miniature = request.FILES['create_image']
        create_poster.save()
    return render(request, 'buy_to_sell/create_poster.html')
