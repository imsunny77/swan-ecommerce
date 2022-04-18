$('.add-to-cart').click(function(){
    product_id = $(this).attr('data-id')
    $.ajax({
        type: "POST",
        url: `/api/add-to-cart/${product_id}/`,
        data: {
            'quantity': 1,
            csrfmiddlewaretoken: csrftoken,
        },
        success: function () {
            alert('Your product is added to cart');
        }
    })
})

// $.post(`/order/check-out/installment-payment/{{enrolment_obj.id}}/`, {'paying_amount':paying})
