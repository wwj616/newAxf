from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from CartApp.models import AxfCart


def cart(request):
    u_id = request.session.get('user_id')

    if u_id:
        carts = AxfCart.objects.filter(c_user_id=u_id)
        # AxfCart.objects.filter(c_is_select=False).exists()
        #  true  没有全被选中
        #  false 全被选择中

        # not AxfCart.objects.filter(c_is_select=False).exists()
        # true   全被选中
        # false  没有全被选中
        is_all_select = not carts.filter(c_is_select=False).exists()
        # 分析出for循环遍历的数据参数
        context = {
            'carts': carts,
            'is_all_select': is_all_select
        }

        return render(request, 'axf/main/cart/cart.html', context=context)
    else:
        return redirect(reverse('axfuser:toLogin'))


def subToCart(request):
    g_id = request.GET.get('g_id')

    u_id = request.session['user_id']
    carts = AxfCart.objects.filter(c_goods_id=g_id).filter(c_user_id=u_id)

    if carts.count() > 1:
        cart = AxfCart()
        cart.c_user_id = u_id
        cart.c_goods_id = g_id
    else:
        cart = carts.first()
        cart.c_goods_num = cart.c_goods_num - 1

    cart.delete()

    data = {
        'status': 200,
        'msg': 'ok',
        'c_goods_num': cart.c_goods_num
    }
    return JsonResponse(data=data)


def addToCart(request):
    g_id = request.GET.get('g_id')

    u_id = request.session.get('user_id')

    carts = AxfCart.objects.filter(c_goods_id=g_id).filter(c_user_id=u_id)

    if carts.count() == 0:
        cart = AxfCart()
        cart.c_user_id = u_id
        cart.c_goods_id = g_id
    else:
        cart = carts.first()
        cart.c_goods_num = cart.c_goods_num + 1

    cart.save()

    data = {
        'status': 200,
        'msg': 'ok',
        'c_goods_num': cart.c_goods_num
    }
    return JsonResponse(data=data)


@csrf_exempt
def changeStatus(request):
    cartid = request.POST.get('cartid')

    cart = AxfCart.objects.get(pk=cartid)

    cart.c_is_select = not cart.c_is_select

    cart.save()

    user_id = request.session.get('user_id')

    is_all_select = not AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=False).exists()

    data = {
        'status': 200,
        'msg': 'ok',
        'c_is_select': cart.c_is_select,
        'is_all_select': is_all_select
    }
    return JsonResponse(data=data)


def all_Select(request):
    # ajax的参数不能传递列表
    cartid_list = request.GET.get('cartid_list')

    id_list = cartid_list.split('#')

    cart_list = AxfCart.objects.filter(id__in=id_list)

    for cart in cart_list:
        cart.c_is_select = not cart.c_is_select
        cart.save()

    data = {
        'msg': 'ok',
        'status': 200
    }
    return JsonResponse(data=data)
