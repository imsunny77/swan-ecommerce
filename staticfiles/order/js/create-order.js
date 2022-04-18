$('.add-to-cart').click(function(){
    var product_id = $(this).attr('data-id')
    var quantity = $('.quantity').val()
    var product_quantity = 1
    if (quantity){
        product_quantity = quantity
    }
    console.log(product_quantity)

    $.ajax({
        type: "POST",
        url: `/api/add-to-cart/${product_id}/`,
        data: {
            'quantity': product_quantity,
            csrfmiddlewaretoken: csrftoken,
        },
        success: function () {
            alert('Your product is added to cart');
        }
    })
})

// $.post(`/order/check-out/installment-payment/{{enrolment_obj.id}}/`, {'paying_amount':paying})
