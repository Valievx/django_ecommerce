let dataTransfer = new DataTransfer(),
    form = document.querySelector('form'),
    container = document.querySelector('.container-form'),
    upload = document.querySelector('.select'),
    input = document.querySelector('input[type="file"]');


upload.addEventListener('click', () => input.click());

input.addEventListener('change', () => {
    let file = input.files;

    if (dataTransfer.items.length + file.length > 10) {
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

const showImages = () => {
    let images = '';
    Array.from(dataTransfer.files).forEach((e, i) => {
        images += `<div class="image">
                       <img src="${URL.createObjectURL(e)}" alt="image">
                       <span onclick="delImage(${i})">&times;</span>
                   </div>`;
    })
    container.innerHTML = images;
}


function submitItem(event) {
    console.log(dataTransfer.items.length)
    if (dataTransfer.items.length < 1) {
        event.preventDefault();
        alert("Должно быть загружено хотя бы одно изображение");
    }

}

const submitBtn = document.querySelector('#save_btn');
submitBtn.addEventListener('click', submitItem);
