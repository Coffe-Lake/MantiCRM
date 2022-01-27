let WinPrint, timer;


function printing() {
    clearTimeout(timer);
    WinPrint.focus();
    WinPrint.print();
    WinPrint.close();
}

function CallPrint(strid) {
    let prtContent = document.getElementById(strid), s = '';
    s += '<html><head>';
    s += '<link rel="stylesheet" type="text/css" href="/static/css/check.css">';
    s += prtContent.innerHTML;
    s += '</body></html>';
    WinPrint = window.open('', '_blank', 'left=50,top=50,width=800px,height=640,toolbar=0,scrollbars=1,status=0');
    WinPrint.document.writeln(s);
    WinPrint.document.close();
    timer = setTimeout('printing()', 500);
}

function CallPrintInvoice(invoiceid) {
    let prtContent = document.getElementById(invoiceid), s = '';
    s += '<html><head>';
    s += '<link rel="stylesheet" type="text/css" href="/static/css/invoice.css">';
    s += prtContent.innerHTML;
    s += '</body></html>';
    WinPrint = window.open('', '_blank', 'left=50,top=50,width=800px,height=640,toolbar=0,scrollbars=1,status=0');
    WinPrint.document.writeln(s);
    WinPrint.document.close();
    timer = setTimeout('printing()', 500);
}
