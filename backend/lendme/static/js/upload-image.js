let files = [],
form = document.querySelector('form'),
container = document.querySelector('.container-form'),
upload = document.querySelector('.select'),
input = document.querySelector('input[type="file"]');

upload.addEventListener('click', () => input.click());

input.addEventListener('change', () => {
    let file = input.files;

    for (let i = 0; i < file.length; i++) {
        if (files.every(e => e.name != file[i].name)) files.push(file[i])
    }

    form.reset();
    showImages();
})

const showImages = () => {
    let images = '';
    files.forEach((e, i) => {
    images += `<div class="image">
                    <img src="${URL.createObjectURL(e)}" alt="image">
                    <span onclick="delImage(${i})">&times;</span>
                </div>`;
    })

    container.innerHTML = images;
}

const delImage = index => {
    files.splice(index, 1)
    showImages()
}
