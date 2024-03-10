$('.carousel-1').owlCarousel({
    loop:true,
    stagePadding: 70,
    nav:true,
    dots: false,
    navText: ['&lsaquo;', '&rsaquo;'],
    responsive:{
        0:{items:1},
        500:{items:2},
        992:{items:3},
        1200:{items:4},
        1600:{items:5}
    }
});


function showPhoneNumber() {
    var button = document.getElementById('showPhoneNumberButton');
    var phoneNumber = document.getElementById('phoneNumber');

    // Изменяем текст кнопки на номер телефона
    button.innerHTML = phoneNumber.innerHTML;

    // Показываем номер телефона и скрываем кнопку
    phoneNumber.style.display = 'block';
    button.style.display = 'none';
}