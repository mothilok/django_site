from django.shortcuts import render
from .models import Poster
from PIL import Image

def home(request):
    request_bd = Poster.objects.order_by('-date_published')[:5]
    context = {
        'data':request_bd
    }
    return render(request, "buy_to_sell/home.html", context)


def post(request, post_id):
    request_bd = Poster.objects.get(pk=post_id)
    print(f'путьььььььььььььььььььььььььььььььь: {request_bd.image.path}')
    print(request_bd.miniature)

    context = {
        'data':request_bd
    }
    return render(request, "buy_to_sell/post.html", context)


def create_poster(request):
    request_post = request.POST
    if request.method == "POST":
        print(f'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa: {type(request.FILES["create_image"])}')
        create_poster = Poster()
        create_poster.title = request_post['create_title']
        create_poster.description = request_post['create_description']
        create_poster.price = request_post['create_price']
        print(f"request image{request.FILES['create_image']}")
        create_poster.image = request.FILES['create_image']
        create_poster.phone_number = request_post['create_number']
        print(f'last crea_numb{create_poster.phone_number}')

        create_poster.miniature = request.FILES['create_image']
        print(f'kast creat_miniat{type(request.FILES["create_image"])}')
        print(f'kast creat_miniat{type(create_poster.miniature)}')

        print(f"reque.FILES{request.FILES}")
        print(f"reque.FILES[image]{request.FILES['create_image']}")

        # image = Image.open(create_poster.image)
        # image.show()
        print(f'creaaaaaaaaaaate alllllllllllllllllllll: {create_poster}')
        create_poster.save()




# что такое Meta, как декодировать файл из байтов
# я кажется понял в чем дело когда происходит сохранение метод save сначало проходится по  image потом по miniature уже по измененному изобр
# проблема так же остается в типах мне нужно чтобвъы img было типа путь байты или объект файла я не помню где это видел

    return render(request, 'buy_to_sell/create_poster.html')





    #
    # if request.method == "POST":
    #     print(request_post['create_image'])
    #     if request_post['create_image']:
    #         resize = Image.open(request_post['create_image'])
    #         if resize.size[0] > 420 and resize.size[1] > 420:
    #             resize = resize.resize((resize.width // 2, resize.height // 2))
    #             request_post['create_image'] = resize
    #         resize.show()
