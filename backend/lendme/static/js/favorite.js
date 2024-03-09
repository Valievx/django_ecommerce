// Adding to favorite
// Remove from favorite

$(document).on("click", ".add-to-favorite", function(){
    let item_id = $(this).attr("data-product-item")
    let this_btn = $(this)

    $.ajax({
        url: "/add-to-favorite",
        data: {
            "id": item_id
        },
        dataType: "json",
        success: function(response){
            if (response.added) {
                this_btn.addClass('active');
                localStorage.setItem('favorite_' + item_id, true); // Сохраняем в локальное хранилище
                console.log(item_id, "Added to favorite...");
            } else {
                this_btn.removeClass('active');
                localStorage.removeItem('favorite_' + item_id); // Удаляем из локального хранилища
                console.log(item_id, "Removed from favorite...");
            }
        }
    })
});