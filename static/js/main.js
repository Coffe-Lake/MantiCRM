function getClientData(val) {
    return alert("Клиент с номером: " + val + " уже есть в базе!");
}


function getDiscount(coupon) {
    return alert(coupon + " активирован")
}


// function getPayMethod(pay_method) {
//     return alert("Способ оплаты: " + pay_method)
// }


// function getDeliveryCost(delivery_cost) {
//     return alert("Стоимость доставки: " + delivery_cost + "₽")
// }


// function getCourier(courier) {
//     return alert("Заказ доставит курьер : " + courier)
// }


// function getOrderStatus(status) {
//     return alert("Статус заказа: " + status)
// }


function printOrder(order) {
    let printContents = document.getElementById(order).innerHTML;
    let originalContents = document.body.innerHTML;

    document.body.innerHTML = printContents;

    window.print();

    document.body.innerHTML = originalContents;
}

// $(document).ready(function () {
//     $('form').submit(function () {
//         let formID = $(this).attr('id'); // Получение ID формы
//         let formNm = $('#' + formID);
//         $.ajax({
//             type: 'POST',
//             url: 'new_order/', // Обработчик формы отправки
//             data: formNm.serialize(),
//             success: function (data) {
//                 // Вывод текста результата отправки в текущей форме
//                 $(formNm).html(data);
//             }
//         });
//         return false;
//     });
// });
