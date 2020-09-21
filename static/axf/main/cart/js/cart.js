$(function () {
    $('.addToCart').click(function () {
        //    将商品添加到购物车中都需要哪些字段呢？
        //    u_id--》session   g_id
        var $button = $(this);

        var g_id = $button.attr('goodsid');

        $.get('/axfcart/addToCart/',
            {'g_id': g_id},
            function (data) {
                $button.prev().html(data['c_goods_num']);
            })
    })
    $('.subToCart').click(function () {
        var $button = $(this)
        var g_id = $button.attr('goodsid')
        $.get(
            '/axfcart/subToCart/',
            {'g_id': g_id},
            function (data) {
                $button.next().html(data['c_good_num'])


            }
        )
    })
//     修改单选的状态
    $('.confirm').click(function () {
        var $div = $(this);
        var cartid = $div.parent().attr('cartid');
        $.post(
            '/axfcart/changeStatus/',
            {'cartid': cartid},
            function (data) {
                if (data['c_is_select']) {
                    $div.find('span').find('span').html('✔');
                } else {
                    $div.find('span').find('span').html('');
                }
                if (data['is_all_select']) {
                    $('.all_select').find('span').find('span').html('✔');
                } else {
                    $('.all_select').find('span').find('span').html('');
                }
            }
        )
    })


    $('.all_select').click(function () {

        var select_list = [];
        var unselect_list = [];


        $('.confirm').each(function () {
            var cartid = $(this).parent().attr('cartid');
            if ($(this).find('span').find('span').html()) {
                select_list.push(cartid);
            } else {
                unselect_list.push(cartid);
            }
        })

        if (unselect_list.length === 0) {
            $.ajax({
                url: '/axfcart/allSelect/',
                data: {'cartid_list': select_list.join('#')},
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    $('.confirm').find('span').find('span').html('');
                    $('.all_select').find('span').find('span').html('');
                }
            })
        } else {
            $.ajax({
                url: '/axfcart/allSelect/',
                data: {'cartid_list': unselect_list.join('#')},
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    $('.confirm').find('span').find('span').html('✔');
                    $('.all_select').find('span').find('span').html('✔');
                }
            })
        }
    })


//    获取标签的属性
//    prop只能获取标签自带的属性  如果是自己编写属性就获取不到
//    所以企业级开发使用attr
//     var g_id = $(this).attr('goodsid');
//     alert(g_id);
// var g = $(this).prop('goodsid');
// alert(g);

})