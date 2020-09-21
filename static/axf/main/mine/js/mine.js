$(function () {
    $('#toLogin').click(function () {
        // window.open('/axfuser/toLogin/',target='_self');
        window.location.href = '/axfuser/toLogin/';
    })


    $('#regis').click(function () {
        window.open('/axfuser/toRegister/',target='_self');
    })
})