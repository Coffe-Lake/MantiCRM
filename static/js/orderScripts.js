$(document).ready(function () {


        $('#id_phone').on('change', function getClientData() {
                let phone = $(this).val();
                const csrfToken = $("input[name=csrfmiddlewaretoken]").val();
                $.ajax({
                        url: '/validate_client',
                        data: {
                            'phone': phone,
                            'csrfmiddlewaretoken': csrfToken,
                        },
                        method: 'POST',
                        mode: 'same-origin',
                        success: function (response) {
                            if (response.is_taken === true) {
                                $('#id_name').val(response.name);
                                $('#id_address').val(response.address);
                                $('#id_home').val(response.home);
                                $('#id_building').val(response.building);
                                $('#id_room').val(response.room);
                                $('#id_entrance').val(response.entrance);
                                $('#id_floor').val(response.floor);
                                $('#id_code').val(response.code);
                                $('#id_mark').val(response.mark);
                                document.getElementById('count_orders')
                                    .innerHTML = response.count_orders
                            } else {
                                $('#id_name').val(null);
                                $('#id_address').val(null);
                                $('#id_home').val(null);
                                $('#id_building').val(null);
                                $('#id_room').val(null);
                                $('#id_entrance').val(null);
                                $('#id_floor').val(null);
                                $('#id_code').val(null);
                                $('#id_mark').val(null);
                            }
                        },
                    }
                )
            }
        )


        $(document).on('change', '#id_order_status', function setOrderStatus() {
                let order_status = $(this).val();
                const order_id = $(this).attr('data-order-id')
                const csrfToken = $("input[name=csrfmiddlewaretoken]").val();
                $.ajax({
                        url: '/set_status',
                        data: {
                            'order_status': order_status,
                            'order_id': order_id,
                            'csrfmiddlewaretoken': csrfToken,
                        },
                        method: 'POST',
                        success: function (taken_status) {
                            document.getElementById('stat')
                                .innerHTML = taken_status.new_status
                            alert(taken_status.new_status)
                        }
                    }
                )
            }
        )
        //
        // $(document).on('change', function setOrderStatus() {
        //         let courier_id = $('#list_order_courier').val();
        //         const order_id = $('#hide_id').val();
        //         const csrfToken = $("input[name=csrfmiddlewaretoken]").val();
        //         $.ajax({
        //                 url: '/set_courier',
        //                 data: {
        //                     'courier_id': courier_id,
        //                     'order_id': order_id,
        //                     'csrfmiddlewaretoken': csrfToken,
        //
        //                 },
        //                 method: 'POST',
        //                 success: function (taken_courier) {
        //                     alert("Заказ доставит " + taken_courier.courier)
        //                 }
        //             }
        //         )
        //     }
        // )

        $('#order').keydown(function (event) {
            if (event.keyCode === 13) {
                event.preventDefault();
                return false;
            }
        });

        setInterval(function () {
            let page = document.location.pathname
            $('#order_list_block').load(page + " #order_list_block > *")
        }, 377700);


        // $('#orders_nav a').click(function () {
        //         let page = $(this).attr('href')
        //         $("#content").load(page)
        //         return false
        //     }
        // )

        // Убавляем кол-во по клику
        $('.quantity_inner .bt_minus').click(function () {
            let $input = $(this).parent().find('.quantity');
            let count = parseInt($input.val()) - 1;
            count = count < 0 ? 0 : count;
            $input.val(count);
        });
        // Прибавляем кол-во по клику
        $('.quantity_inner .bt_plus').click(function () {
            let $input = $(this).parent().find('.quantity');
            let count = parseInt($input.val()) + 1;
            count = count > parseInt($input.data('max-count')) ? parseInt($input.data('max-count')) : count;
            $input.val(parseInt(count));
        });
        // Убираем все лишнее и невозможное при изменении поля
        $('.quantity_inner .quantity').bind("change keyup input click", function () {
            if (this.value.match(/[^0-9]/g)) {
                this.value = this.value.replace(/[^0-9]/g, '');
            }
            if (this.value === "") {
                this.value = 0;
            }
            if (this.value > parseInt($(this).data('max-count'))) {
                this.value = parseInt($(this).data('max-count'));
            }
        });


        $('.cart-item-qty').on('click', function () {
                let qty = $(this).val()
                let item_id = $(this).attr('data-id')
                let data = {
                    qty: qty,
                    item_id: item_id
                }
                $.ajax({
                        method: 'GET',
                        url: '{% url "change_item_qty" %}',
                        data: data,
                        success: function (data) {
                            $('$cart-item-total-' + item_id).html(parseFloat(data.item_total).toFixed(2))
                            $('$cart-total-price').html(parseFloat(data.cart_total_price).toFixed(2))

                        }
                    }
                )
            }
        )


        // Конец $document
    }
)


