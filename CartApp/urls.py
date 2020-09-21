from django.conf.urls import url

from CartApp import views

urlpatterns = [
    url(r'^cart/', views.cart, name='cart'),
    #     添加到购物车
    url(r'^addToCart/', views.addToCart),
    url(r'^subToCart/', views.subToCart),
    #     修改单选状态
    url(r'^changeStatus/', views.changeStatus),
    #     全选
    url(r'^allSelect/', views.all_Select),
]
