//到了夫  圆括号  芳珂神   圆括号  大括号
$(function(){
    init_newSwiper();
    init_newSwiper1();
})

//轮播
function init_newSwiper(){
    var newSwiper = new Swiper('#topSwiper',
                           {
                                loop:true,
                                autoplay:3000,
                                pagination:'.swiper-pagination',
                                autoplayDisableOnInteraction:false
                           })
}

//滑动
function init_newSwiper1(){
    var newSwiper1 = new Swiper('#swiperMenu',{
        slidesPerView :3
    })
}