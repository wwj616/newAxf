from django.shortcuts import render

# Create your views here.
from UserApp.models import AxfUser


def mine(request):

    user_id = request.session.get('user_id')
    print(user_id)

    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        context = {
            'user1':user
        }
        return render(request,'axf/main/mine/mine.html',context=context)
    else:
        return render(request,'axf/main/mine/mine.html')