import multipleformwizard as mf
from django import forms
from django.forms import formset_factory

from .models import Order
from .models import Client


class OrderForm(forms.ModelForm):
    # order_status = forms.ChoiceField(
    #     label="Статус заказа",
    #     choices=ORDER_STATUS,
    #     required=False,
    #     widget=forms.Select(
    #         attrs={
    #             'class': "form-select w-75 fw-bold text-center",
    #             'onchange': "getOrderStatus(this.value)",
    #         }
    #     )
    # )
    # phone = forms.CharField(
    #     label='Телефон',
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={
    #             'type': "tel",
    #             'class': "col form-control w-75 fw-bold text-center",
    #             'placeholder': "+7(___)___-__-__",
    #             'max-length': '18',
    #             'value': '',
    #             'onchange': "getClientData(this.value)",
    #             'autofocus': "True",
    #             'data-tel-input': 'True',
    #         }
    #     )
    # )
    # name = forms.CharField(
    #     label="Имя",
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': "Имя",
    #             'class': "form-control form-control-md w-75",
    #         }
    #     )
    # )
    # address = forms.CharField(
    #     label="Адрес",
    #     required=False,
    #     widget=forms.Textarea(
    #         attrs={
    #             'placeholder': "Адрес",
    #             'class': "form-control form-control-md w-75",
    #             'cols': 30,
    #             'rows': 3,
    #         }
    #     )
    # )
    # room = forms.CharField(
    #     label="Квартира",
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': "квартира/комната",
    #             'class': "form-control form-control-md w-75",
    #         }
    #     )
    # )
    # entrance = forms.CharField(
    #     label="Подъезд",
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': "form-control form-control-md",
    #             'style': "width: 110px",
    #         }
    #     )
    # )
    # floor = forms.IntegerField(
    #     label="Этаж",
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': "form-control form-control-md",
    #             'style': "width: 110px",
    #         }
    #     )
    # )
    # code = forms.CharField(
    #     label="Код домофона",
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control form-control-md w-50',
    #             # 'style': 'width: 110px',
    #         }
    #     )
    # )
    # pre_order_date = forms.CharField(
    #     label="Дата",
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control form-control-md',
    #             'style': 'width: 250px',
    #             'type': "datetime-local",
    #         }
    #     )
    # )
    #
    # mark = forms.CharField(
    #     label="Отметка",
    #     required=False,
    #     widget=forms.Textarea(
    #         attrs={
    #             'placeholder': "Отметка",
    #             'class': 'form-control form-control-md',
    #             'cols': 30,
    #             'rows': 3,
    #         }
    #     )
    # )
    # comment = forms.CharField(
    #     label="Комментарий",
    #     required=False,
    #     widget=forms.Textarea(
    #         attrs={
    #             'placeholder': "Комментарий",
    #             'class': 'form-control form-control-md',
    #             'cols': 30,
    #             'rows': 3,
    #         }
    #     )
    # )
    # sales_channel = forms.ModelChoiceField(
    #     label="Канал продаж",
    #     required=False,
    #     queryset=SalesChannel.objects.all(),
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-select',
    #             'style': 'width: 100%',
    #         }
    #     )
    # )
    # courier = forms.ModelChoiceField(
    #     label="Курьер",
    #     required=False,
    #     queryset=Courier.objects.all(),
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-select',
    #             'style': 'width: 100%',
    #         }
    #     )
    # )
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
    #     ("CAS", 'Наличными'),
    #     ("ONL", 'Онлайн'),
    #     ("TER", 'Терминал'),
    #     ("TRN", 'Переводом')
    # )
    # pay = forms.ChoiceField(
    #     label="Способ оплаты",
    #     choices=PAY_METHOD_CHOICES,
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-select w-25',
    #         }
    #     )
    # )
    # discount_sum = forms.ModelChoiceField(
    #     label="Скидка",
    #     required=False,
    #     queryset=Discounts.objects.all(),
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-select w-50',
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

    class Meta:
        model = Order
        fields = (
            'order_status',
            'delivery_price',
            'discount_sum',
            'pay_method',
            'paid',
            'persons',
            'pre_order',
            'mark',
            'staff_comment',
            'sales_channel',
            'courier',
        )
        widgets = {
            'order_status': forms.Select(
                attrs={
                    'class': "form-select fw-bold w-75",
                }
            ),
            'pre_order': forms.TextInput(
                attrs={
                    'type': "datetime-local",
                    'class': "col form-control w-75 fw-bold",

                }
            ),
            'mark': forms.Textarea(
                attrs={
                    'class': "col form-control w-75",
                    'rows': '3',
                }
            ),
            'staff_comment': forms.Textarea(
                attrs={
                    'class': "col form-control w-75",
                    'rows': '3',
                }
            ),
            'sales_channel': forms.Select(
                attrs={
                    'class': "form-select w-50"
                }
            ),
            'courier': forms.Select(
                attrs={
                    'class': "form-select w-50"
                }
            ),
            'persons': forms.NumberInput(
                attrs={
                    'class': "form-control w-25 p-2"
                }
            ),
            'delivery_price': forms.Select(
                attrs={
                    'class': "form-select w-50"
                }
            ),
            'discount_sum': forms.Select(
                attrs={
                    'class': "form-select"
                }
            ),
            'pay_method': forms.Select(
                attrs={
                    'class': "form-select w-75"
                }
            ),
            'paid': forms.CheckboxInput(
                attrs={
                    'class': "form-check-input",
                    'type': "checkbox",
                    'style': 'cursor: pointer'
                }
            )
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'order_status': forms.TextInput(
                attrs={
                    'type': "tel",
                    'class': "col form-control w-75 fw-bold text-center",
                    'placeholder': "+7(___)___-__-__",
                    'max-length': '18',
                    'value': '',
                    'onchange': "getClientData(this.value)",
                    'autofocus': "True",
                    'data-tel-input': 'True',
                }
            )
        }
