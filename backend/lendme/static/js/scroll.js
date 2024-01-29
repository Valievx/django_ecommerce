<script>
  $(document).ready(function () {
    var offset = 0;

    function getItems() {
      $.ajax({
        url: '/get_items/',
        data: { offset: offset },
        success: function (data) {
          data.forEach(function (item) {
            var itemHtml = `
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
          offset += 30;
        },
      });
    }

    $(window).scroll(function () {
      if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
        getItems();
      }
    });

    getItems();
  });
</script>
