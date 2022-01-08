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


        $(document).on('change', '#list_order_status', function setOrderStatus() {
                let order_status = $(this).val();
                const order_id = $('#hide_id').val();
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
                        }
                    }
                )
            }
        )

        $(document).on('change', function setOrderStatus() {
                let courier_id = $('#list_order_courier').val();
                const order_id = $('#hide_id').val();
                const csrfToken = $("input[name=csrfmiddlewaretoken]").val();
                $.ajax({
                        url: '/set_courier',
                        data: {
                            'courier_id': courier_id,
                            'order_id': order_id,
                            'csrfmiddlewaretoken': csrfToken,

                        },
                        method: 'POST',
                        success: function (taken_courier) {
                            alert("Заказ доставит " + taken_courier.courier)
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

    }
)