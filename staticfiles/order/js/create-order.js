$('.add-to-cart').click(function(){
    product_id = $(this).attr('data-id')
    $.ajax({
        type: "POST",
        url: `/order/api/add-to-cart/${product_id}/`,
        data: {
            'quantity': product_quantity,
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        },
        success: function () {
            alert('Your product is added to cart');
        }
    })
    console.log(product_id)
})