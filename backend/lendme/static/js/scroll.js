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
                      <p class="price">${item.price}₽/${item.time_period} ${item.time_period_unit}</p>
                      <p class="data">${item.pub_date}</p>
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
            // После задержки в 1 секунду, разрешаем отправку запроса
            canSendRequest = true;
        }, 100);

        if (window.innerHeight + window.scrollY + 250 >= document.body.offsetHeight) {
            getItems();
        }
    });

    getItems();
});
