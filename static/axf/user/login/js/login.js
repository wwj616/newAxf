$(function () {
    $('#icode').click(function () {
        var i = document.getElementById('icode');
        //ie浏览器的内核的缓存问题  当有重复的请求 执行的时候 不会在发送请求
        //所以我们需要加一个不能重复的值 来告诉服务器我是一个不同的请求
        i.src = '/axfuser/get_code/'+Math.random();
    })
    
    
    $('form').submit(function () {
        var password1 = $('#exampleInputPassword1').val();
        var password2 = md5(password1);
        $('#exampleInputPassword1').val(password2);
        return true;
    })
    
})