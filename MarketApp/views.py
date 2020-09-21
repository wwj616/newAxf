from django.shortcuts import render

# Create your views here.
from MarketApp.models import AxfFoodType, AxfGoods


def market(request):
    foodtypes = AxfFoodType.objects.all()

    typeid = request.GET.get('typeid','104749')

    goods_list = AxfGoods.objects.filter(categoryid=typeid)
# ['全部分类:0', '酸奶乳酸菌:103537', '牛奶豆浆:103538', '面包蛋糕:103540']

    # 找到当前点击对象的那个商品类别
    foodtype = AxfFoodType.objects.filter(typeid=typeid)[0]
    childtypenames = foodtype.childtypenames
    # 全部分类:0#饮用水:103550#茶饮/咖啡:103554#
    # 功能饮料:103553#酒类:103555#果汁饮料:103551
    # #碳酸饮料:103552#整箱购:104503#植物蛋白:104489
    # #进口饮料:103556
    child_list_split = childtypenames.split('#')

    child_name_list = []
    for child in child_list_split:
        # ['功能饮料', '103553']
        child_name = child.split(':')
        # [['abc',103232]]
        child_name_list.append(child_name)

    childcid = request.GET.get('childcid','0')

    if childcid == '0':
        pass
    else:
        goods_list = goods_list.filter(childcid=childcid)


    # 三级联动  综合排序
    sort_rule_list = [
        ['综合排序','0'],
        ['价格升序','1'],
        ['价格降序','2'],
        ['销量升序','3'],
        ['效率降序','4'],
    ]

    s_rule = request.GET.get('s_rule','0')

    if s_rule == '0':
        pass
    elif s_rule == '1':
        goods_list = goods_list.order_by('price')
    elif s_rule == '2':
        goods_list = goods_list.order_by('-price')
    elif s_rule == '3':
        goods_list = goods_list.order_by('productnum')
    elif s_rule == '4':
        goods_list = goods_list.order_by('-productnum')

    context = {
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'typeid':typeid,
        'child_name_list':child_name_list,
        'childcid':childcid,
        'sort_rule_list':sort_rule_list,
        's_rule':s_rule
    }
    return render(request,'axf/main/market/market.html',context=context)