from django.shortcuts import render
from .models import Advertisement
from .forms import AdvertisementForm
# Create your views here.

def example(request):
    advertisements = Advertisement.objects.all() # получаем все элементы из БД
    # по такой схеме будем работать в index.html:
    # for i in advertisements:
    #     print(i.id, i.title, i.price)
    context = {"advertisement": advertisements}
    return render(request, "index.html", context)

def top_sellers(request):
    return render(request, "top-sellers.html")


def advertisement_post(request):
    # создаем новую форму
    form = AdvertisementForm()
    # отправляем форму в шаблон через контекст
    context = {'form': form}
    return render(request, "advertisement-post.html", context)