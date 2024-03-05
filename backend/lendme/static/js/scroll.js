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
