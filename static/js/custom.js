$(document).ready(function () {
    $.mask.definitions['h'] = "[0|1|4|5|9]"
    $("#phone").click(function () {
        $(this).setCursorPosition(2);
    }).mask("8(h99) 999-99-99");
})
