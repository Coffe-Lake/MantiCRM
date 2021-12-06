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


function printOrder(check_print) {
    let printContents = document.getElementById(check_print).innerHTML;
    let originalContents = document.body.innerHTML;

    document.body.innerHTML = printContents;
    window.focus();
    window.print();
    window.close()

    document.body.innerHTML = originalContents;
}

//
// var WinPrint, timer;
//
// function CallPrint(strid) {
//     var prtContent = document.getElementById(strid), s = '';
//     s += '<html><head>';
//     s += '<link rel="stylesheet" type="text/css" href="/static/css/check.css">';
//     s += prtContent.innerHTML;
//     s += '</body></html>';
//     WinPrint = window.open('', '_blank', 'left=50,top=50,width=800px,height=640,toolbar=0,scrollbars=1,status=0');
//     WinPrint.document.writeln(s);
//     WinPrint.document.close();
//     timer = setTimeout('printing()', 500);
// };
//
// function printing() {
//     clearTimeout(timer);
//     WinPrint.focus();
//     WinPrint.print();
//     WinPrint.close();
// };
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
