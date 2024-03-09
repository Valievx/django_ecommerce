$(document).ready(function () {
    let offset = 0;
    let empty = false;

    function getItems() {
        $.ajax({
            url: '/get_items/',
            data: {offset: offset},
            success: function (data) {
                if (data?.message === "empty") {
                    empty = true;
                    return;
                }
                data.forEach(function (item) {
                    let date = new Date(item.pub_date);
                    let today = new Date();
                    let itemDate;
                    if (date.getDate() === today.getDate() && date.getMonth() === today.getMonth() && date.getFullYear() === today.getFullYear()) {
                        itemDate = 'Сегодня ' + date.getHours() + ':' + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes();
                    } else if (date.getDate() === today.getDate() - 1 && date.getMonth() === today.getMonth() && date.getFullYear() === today.getFullYear()) {
                        itemDate = 'Вчера ' + date.getHours() + ':' + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes();
                    } else {
                        itemDate = date.toLocaleDateString() + ' ' + date.getHours() + ':' + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes();
                    }

                    let isFavorite = localStorage.getItem('favorite_' + item.id); // Проверяем, сохранен ли товар в избранном

                    let itemHtml = `
                        <div class="product-card">
                          <div class="product-item">
                            <div class="product-img">
                              <a href="catalog/product/${item.slug}">
                                  <img src="${item.image}" alt="${item.name}" />
                              </a>
                            </div>
                            <div class="product-list">
                              <a class="product-name" href="catalog/product/${item.slug}">
                                <h3>${item.name}</h3>
                              </a>
                              <button
                                class="add-to-favorite ${isFavorite ? 'active' : ''}"
                                data-product-item="${item.id}">
                                <i class="heart-icon">
                                    <svg class="heart-icon" xmlns="http://www.w3.org/2000/svg"
                                    width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#000000"
                                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z">
                                    </path>
                                    </svg>
                                </i>
                              </button>
                            </div>
                            <div class="product-data">
                              <p class="price">${item.price}₽/${item.time_period}</p>
                              <p class="data">${itemDate}</p>
                            </div>
                          </div>
                        </div>
                    `;
                    $('.items-list').append(itemHtml);
                });
                offset += 30
            },
        });
    }

    let canSendRequest = true;
    $(window).scroll(function () {
        if (empty) {
            return;
        }

        if (!canSendRequest) {
            return;
        }

        canSendRequest = false;
        setTimeout(function () {
            canSendRequest = true;
        }, 100);

        if (window.innerHeight + window.scrollY + 250 >= document.body.offsetHeight) {
            getItems();
        }
    });

    getItems();

});