$(function () {
    var nameflag = false;
    var passwordflag = false;

    $('#exampleInputName').blur(function () {
        var name = $(this).val();

        var reg = /^\w{6,18}$/;

        if(!reg.test(name)){
            $('#nameinfo').text('用户名字格式不正确').css('color','red');
            nameflag=false;
        }else{
        //    $.getJSON   $.get   $.post  $.ajax
            $.getJSON(
                '/axfuser/checkName/',
                {'name':name},
                function (data) {
                    if (data['status'] == 200){
                        $('#nameinfo').text(data['msg']).css('color','green');
                        nameflag = true;
                    }else{
                        $('#nameinfo').text(data['msg']).css('color','red');
                        nameflag = false;
                    }
                }
            )
        }
    })

    $('#exampleInputPassword2').blur(function () {
        var password1 = $('#exampleInputPassword1').val();
        var password2 = $('#exampleInputPassword2').val();
        if(password1 == password2){
            $('#passwordInfo').text('密码一致').css('color','green');
            passwordflag = true;
        }else{
            $('#passwordInfo').text('密码不一致').css('color','red');
            passwordflag = false;
        }

    })

    // 表单的submit事件的返回值 只有为true的时候 才可以提交表单
    $('form').submit(function () {
        var nflag = nameflag;
        var pflag = passwordflag;
        //true  true  1
        //false true  0
        //false false 0
        var b = nflag & pflag;

        var password1 = $('#exampleInputPassword1').val();
        var password2 = md5(password1);
        $('#exampleInputPassword1').val(password2);

        if(b==1){
            return true;
        }else{
            return false;
        }

    })


})