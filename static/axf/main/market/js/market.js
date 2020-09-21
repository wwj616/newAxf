$(function () {
    $('#all_type').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down');
        $('#all_type_container').toggle();
    })

    $('#sort_rule').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down');
        $('#sort_rule_container').toggle();
    })
})