$(document).ready(function () {

        // Обновление страницы по интервалу
        setInterval(function () {
            $('#order_list_block')
                .load(document.location.pathname + " #order_list_block > *")
        }, 10000);


        // Получение данных клиента по номеру тел
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


        // Изменение статуса заказа
        $(document).on('change', '#id_order_status', function setOrderStatus() {
                let order_status = $(this).val();
                const order_id = $(this).attr('data-order-id')
                const csrfToken = $("input[name=csrfmiddlewaretoken]").val();
                $.ajax({
                        url: '/',
                        data: {
                            'order_status': order_status,
                            'order_id': order_id,
                            'csrfmiddlewaretoken': csrfToken,
                        },
                        method: 'POST',
                        success: function () {
                            $('#order_list_block')
                                .load(document.location.pathname + " #order_list_block > *")
                        }
                    }
                )
            }
        )


        // Изменение курьера
        $(document).on('change', '#list_order_courier', function setOrderCourier() {
                let order_courier = $(this).val();
                const order_id = $(this).attr('order-courier-id')
                const csrfToken = $("input[name=csrfmiddlewaretoken]").val();
                $.ajax({
                        url: '/',
                        data: {
                            'order_courier': order_courier,
                            'order_id': order_id,
                            'csrfmiddlewaretoken': csrfToken,
                        },
                        method: 'POST',
                        success: function () {
                            $('#order_list_block')
                                .load(document.location.pathname + " #order_list_block > *")
                        }
                    }
                )
            }
        )


        // Добавление продукта в корзину
        $('#product-button').on('click', function addProductOnCart() {
                let product = $(this).attr('data-product-id');
                const csrfToken = $("input[name=csrfmiddlewaretoken]").val();
                $.ajax({
                        url: '/cart_add',
                        data: {
                            'product': product,
                            'csrfmiddlewaretoken': csrfToken,
                        },
                        method: 'POST',
                        success: function () {
                            alert("Продукт добавлен в корзину")
                        }
                    }
                )
            }
        )


        //Скрыть ненужные значения в выпадающем списке
        $('select#id_order_status option[value=PRO]').hide();
        $('select#id_order_status option[value=""]').remove();
        $('select#id_delivery_price option[value=""]').remove();
        $('select#id_pay_method option[value=""]').remove();


        // $('#orders_nav a').click(function () {
        //         let page = $(this).attr('href')
        //         $("#content").load(page)
        //         return false
        //     }
        // )


        //Кнопка добавить в корзину


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


        $('#order').keydown(function (event) {
            if (event.keyCode === 13) {
                event.preventDefault();
                return false;
            }
        });
        // Конец $document
    }
)


