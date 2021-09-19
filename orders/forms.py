from clients.models import Client

from django import forms
from delivery.models import DeliveryPrice
from marketing.models import Discounts


class NewOrderForm(forms.Form):
    ORDER_STATUS_CHOICES = (
        ("NEW", 'Новый'),
        ("PREORDER", 'Предзаказ'),
    )
    order_status = forms.ChoiceField(label="Статус заказа*", choices=ORDER_STATUS_CHOICES)
    phone = forms.CharField(
        label="Номер телефона*",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Телефон',
                'autofocus': True,
            }
        )
    )
    phone_2 = forms.CharField(
        label="Доп. телефон",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Доп. телефон',
            }
        )
    )
    name = forms.CharField(
        label="Имя*",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Имя',
            }
        )
    )
    address = forms.CharField(
        label="Адрес",
        widget=forms.Textarea(
            attrs={
                'placeholder': "Адрес",
                'cols': 30,
                'rows': 3
            }
        )
    )
    room = forms.CharField(
        label="Квартира/комната",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'квартира/комната',
            }
        )
    )
    entrance = forms.CharField(
        label="Подъезд",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Подъезд',
            }
        )
    )
    floor = forms.IntegerField(
        label="Этаж",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Этаж',
            }
        )
    )
    code = forms.CharField(
        label="Код домофона",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Код домофона',
            }
        )
    )
    delivery_price = forms.ModelChoiceField(label="Стоимость доставки", initial=0, queryset=DeliveryPrice.objects.all())
    PAY_METHOD_CHOICES = (
        ("CASH", 'Наличными'),
        ("ONLINE", 'Онлайн'),
        ("TERMINAL", 'Терминал'),
        ("TRANSFER", 'Переводом')
    )
    pay = forms.ChoiceField(label="Способ оплаты", choices=PAY_METHOD_CHOICES)
    discount_sum = forms.ModelChoiceField(label="Скидка", queryset=Discounts.objects.all())
    margin_order = forms.IntegerField(
        label="Наценка",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Наценка',
            }
        )
    )
    persons = forms.IntegerField(
        label="Количество персон",
        initial=0,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Персон',
            }
        )
    )

    pre_order_date = forms.CharField(
        label="Дата",
        widget=forms.TextInput(
            attrs={
                'type': "date"
            }
        )
    )
    pre_order_time = forms.DateTimeField(
        label="Время",
        widget=forms.TextInput(
            attrs={
                'type': "time"
            }
        )
    )
    mark = forms.CharField(
        label="Отметка",
        widget=forms.Textarea(
            attrs={
                'placeholder': "Отметка",
                'cols': 30,
                'rows': 3
            }
        )
    )
    comment = forms.CharField(
        label="Комментарий",
        widget=forms.Textarea(
            attrs={
                'placeholder': "Комментарий",
                'cols': 30,
                'rows': 3
            }
        )
    )


class Meta:
    model = (DeliveryPrice, Discounts)
    fields = ('delivery_price', 'coupon', 'name')
