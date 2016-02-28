$(document).ready(function () {
    $('#body_right').on('scroll', function () {
        $('#body_left').scrollTop($(this).scrollTop());
        $('#bar_time').scrollLeft($(this).scrollLeft());
    });
    
    $('#body_left').on('scroll', function () {
        $('#body_right').scrollTop($(this).scrollTop());
    });
    
    $('#bar_time').on('scroll', function () {
        $('#body_right').scrollLeft($(this).scrollLeft());
    });
});