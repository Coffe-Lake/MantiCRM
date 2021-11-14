from django import forms
from marketing.models import Discounts
from orders.models import Order
from staff.models import Courier
from marketing.models import SalesChannel


class NewOrderForm(forms.Form):
    ORDER_STATUS = (
        ("NEW", 'Новый'),
        ("PREORDER", 'Предзаказ'),
        ("PREPARING", 'Готовится'),
        ("READY", 'Заказ готов'),
        ("DELIVERED", 'Доставляется'),
        ("COMPLETED", 'Выполнен'),
        ("CANCELED", 'Отменен'),
    )
    order_status = forms.ChoiceField(
        label="Статус заказа*",
        choices=ORDER_STATUS,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'style': 'width: 190px',
                'onchange': "getOrderStatus(this.value)",
            }
        )
    )
    # phone = forms.CharField(
    #     label="Номер телефона*",
    #     widget=forms.NumberInput(
    #         attrs={
    #             'placeholder': 'Телефон',
    #             'class': 'form-control form-control-md',
    #             'autofocus': True,
    #             'type': 'tel',
    #             'id': 'phone',
    #             'maxlength': '18',
    #         }
    #     )
    # )

    name = forms.CharField(
        label="Имя",
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Имя',
                'class': 'form-control form-control-md',
            }
        )
    )
    address = forms.CharField(
        label="Адрес",
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': "Адрес",
                'class': 'form-control form-control-md',
                'cols': 30,
                'rows': 3,
            }
        )
    )
    room = forms.CharField(
        label="Квартира",
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'квартира/комната',
                'class': 'form-control form-control-md',
            }
        )
    )
    entrance = forms.CharField(
        label="Подъезд",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-md',
                'style': 'width: 110px',
            }
        )
    )
    floor = forms.IntegerField(
        label="Этаж",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-md',
                'style': 'width: 110px',
            }
        )
    )
    code = forms.CharField(
        label="Код домофона",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-md w-50',
                # 'style': 'width: 110px',
            }
        )
    )
    # delivery_price = forms.ModelChoiceField(
    #     label="Стоимость доставки",
    #     initial=0,
    #     queryset=DeliveryPrice.objects.all(),
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-select',
    #             'style': 'width: 110px'
    #         }
    #     )
    # )
    # PAY_METHOD_CHOICES = (
    #     ("CASH", 'Наличными'),
    #     ("ONLINE", 'Онлайн'),
    #     ("TERMINAL", 'Терминал'),
    #     ("TRANSFER", 'Переводом')
    # )
    # pay = forms.ChoiceField(
    #     label="Способ оплаты",
    #     choices=PAY_METHOD_CHOICES,
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-select',
    #             'style': 'width: 190px'
    #         }
    #     )
    # )
    # discount_sum = forms.ModelChoiceField(
    #     label="Скидка",
    #     required=False,
    #     queryset=Discounts.objects.all(),
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-select',
    #             'style': 'width: 100%',
    #         }
    #     )
    # )
    # margin_order = forms.IntegerField(
    #     label="Наценка",
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': 'Наценка',
    #         }
    #     )
    # )
    # persons = forms.IntegerField(
    #     label="Количество персон",
    #     initial=0,
    #     required=False,
    #     widget=forms.NumberInput(
    #         attrs={
    #             'placeholder': 0,
    #             'class': 'form-control form-control-md',
    #             'style': 'width: 80px',
    #             'min': '0',
    #             'max': '255',
    #         }
    #     )
    # )

    pre_order_date = forms.CharField(
        label="Дата",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-md',
                'style': 'width: 250px',
                'type': "datetime-local",
            }
        )
    )

    mark = forms.CharField(
        label="Отметка",
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': "Отметка",
                'class': 'form-control form-control-md',
                'cols': 30,
                'rows': 3,
            }
        )
    )
    comment = forms.CharField(
        label="Комментарий",
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': "Комментарий",
                'class': 'form-control form-control-md',
                'cols': 30,
                'rows': 3,
            }
        )
    )
    sales_channel = forms.ModelChoiceField(
        label="Канал продаж",
        required=False,
        queryset=SalesChannel.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'style': 'width: 100%',
                'onchange': "getSalesChannel(this.value)",
            }
        )
    )
    courier = forms.ModelChoiceField(
        label="Курьер",
        required=False,
        queryset=Courier.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'style': 'width: 100%',
                'onchange': "getCourier(this.value)",
            }
        )
    )


class Meta:
    model = Discounts
    fields = ('coupon', 'name')
