from django.utils.translation import ugettext_lazy as _

from django import forms

from .models import Order
from .models import Client


class OrderForm(forms.ModelForm):
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
                    'class': "col form-control w-100 fw-bold",

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
                    'class': "form-select w-100"
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
            'phone': forms.TextInput(
                attrs={
                    'type': "tel",
                    'class': "col form-control w-75 fw-bold text-center",
                    'placeholder': "+7(___)___-__-__",
                    'max-length': "16",
                    'onchange': "getClientData(this.value)",
                    'autofocus': "True",
                    'data-tel-input': "True",
                    'autocomplete': "False"
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': "form-control form-control-md w-75",
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': "form-control form-control-md",
                    'style': 'width: 393px',
                    'cols': "30",
                    'rows': "3",
                }
            ),
            'home': forms.TextInput(
                attrs={
                    'class': "form-control form-control-md",
                    'style': 'width: 130px',
                }
            ),
            'building': forms.TextInput(
                attrs={
                    'class': "form-control form-control-md",
                    'style': 'width: 130px',
                }
            ),
            'room': forms.TextInput(
                attrs={
                    'class': "form-control form-control-md",
                    'style': 'width: 130px',
                }
            ),
            'entrance': forms.TextInput(
                attrs={
                    'class': "form-control form-control-md",
                    'style': 'width: 130px',
                }
            ),
            'floor': forms.TextInput(
                attrs={
                    'class': "form-control form-control-md ",
                    'style': 'width: 130px',
                }
            ),
            'code': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-md',
                    'style': 'width: 130px',
                }
            ),
        }
