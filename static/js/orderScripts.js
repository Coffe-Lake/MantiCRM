$(document).ready(function () {


        $('#id_phone').on('change', function getClientData() {
                let phone = $(this).val()
                $.ajax({
                        async: true,
                        url: '/validate_client',
                        data: {'phone': phone},
                        type: 'GET',
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


        $('#order').keydown(function (event) {
            if (event.keyCode === 13) {
                event.preventDefault();
                return false;
            }
        });

    }
)