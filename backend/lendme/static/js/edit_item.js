let dataTransfer = new DataTransfer(),
    old_images = document.querySelectorAll('input[name="delete_images"]'),
    old_images_counter = old_images.length
    input = document.querySelector('input[type="file"]'),
    form = document.querySelector('form'),
    container = document.querySelector('.container-form'),
    upload = document.querySelector('.select');



upload.addEventListener('click', () => input.click());

input.addEventListener('change', () => {
    let file = input.files;

    if (dataTransfer.items.length + file.length + old_images_counter > 10) {
        alert("Максимальное количество изображений для загрузки - 10");
        return;
    }

    for (let i = 0; i < file.length; i++) {
        dataTransfer.items.add(file[i])
    }

    input.files = dataTransfer.files
    showImages();
})

form.addEventListener('submit', (event) => {
    input.files = dataTransfer.files
})

function delImage(index) {
    let items = dataTransfer.items
    items.remove(index)
    dataTransfer.items = items
    showImages();
}

function delOldImage(index) {
    old_images_counter -= 1

    let old_img = old_images[index].parentNode
    old_img.style.display = 'none'
    old_img.style.visibility = 'hidden'

    let checkbox = old_img.querySelector('input[type="checkbox"]')
    checkbox.setAttribute('checked', 'checked');

    showImages();
}

const showImages = () => {
    let images = '';

    old_images.forEach((e) => {
        images += e.parentNode.outerHTML
    })


    Array.from(dataTransfer.files).forEach((e, i) => {
        images += `<div class="image">
                       <img src="${URL.createObjectURL(e)}" alt="image">
                       <span onclick="delImage(${i})">&times;</span>
                   </div>`;
    })
    container.innerHTML = images;
}


function submitItem(event) {
    if (dataTransfer.items.length + old_images_counter < 1) {
        event.preventDefault();
        alert("Должно быть загружено хотя бы одно изображение");
    }
}

const submitBtn = document.querySelector('#save_btn');
submitBtn.addEventListener('click', submitItem);