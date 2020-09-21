from django.shortcuts import render

# Create your views here.
from HomeApp.models import AxfWheel, AxfNav, AxfMustbuy, AxfMainShow


def home(request):
    wheels = AxfWheel.objects.all()
    navs = AxfNav.objects.all()
    mustBuys = AxfMustbuy.objects.all()

    mainShows = AxfMainShow.objects.all()

    return render(request,'axf/main/home/home.html',context=locals())