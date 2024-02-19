const stars = document.querySelectorAll('.rating .star');

stars.forEach((star, index) => {
    star.addEventListener('mouseover', function() {
        stars.forEach((s, i) => {
            if (i <= index) {
                s.classList.add('hovered');
            } else {
                s.classList.remove('hovered');
            }
        });
    });

    star.addEventListener('click', function() {
        document.querySelector('input[name="rating"]').value = index + 1;

        stars.forEach((s, i) => {
            if (i <= index) {
                s.classList.add('selected');
            } else {
                s.classList.remove('selected');
            }
        });
    });

    star.addEventListener('mouseout', function() {
        stars.forEach(s => {
            s.classList.remove('hovered');
        });
    });
});


function submitReview() {
    const selectedStars = document.querySelectorAll('.star.selected');
    if (selectedStars.length === 0) {
        alert('Пожалуйста, выберите рейтинг.');
        return;
    }

    const commentInput = document.querySelector('textarea[name="comment"]');
    if (commentInput.value.trim() === '') {
        alert('Пожалуйста, введите текст отзыва.');
        return;
    }
}

const submitButton = document.querySelector('#submit-review-button');
submitButton.addEventListener('click', submitReview);