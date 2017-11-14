
$('.slides').slick({
    asNavFor: '.captions',
    infinite: true,
    speed: 300,
    autoplay: false,
    autoplaySpeed: 3000,
    arrows: false,
}); 

$(".captions").slick({
    asNavFor: '.slides',
    infinite: true,
    speed: 300,
    fade: true,
    appendArrows: $('.pagination'),
    prevArrow: '<div class="pagination__button"><i class="material-icons">keyboard_arrow_left</i></div>',
    nextArrow: '<div class="pagination__button"><i class="material-icons">keyboard_arrow_right</i></div>'
});