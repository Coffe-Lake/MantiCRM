// function getClientData(val) {
//     let settings = {
//         "async": true,
//         "crossDomain": true,
//         "url": "/new_order",
//         "method": "GET",
//         "client": {
//
//         }
//     }
//
//     $.ajax(settings).done(function (response) {
//         console.log(response);
//     });
// }
//

//
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


