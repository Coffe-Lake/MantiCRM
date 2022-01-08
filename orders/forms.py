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
            'staff_comment',
            'sales_channel',
            'courier',
        )
        widgets = {
            'order_status': forms.Select(
                attrs={
                    'class': "form-select form-select-sm fw-bold w-75",
                }
            ),
            'pre_order': forms.TextInput(
                attrs={
                    'type': "datetime-local",
                    'class': "col form-control form-control-sm w-100 fw-bold",
                }
            ),
            'staff_comment': forms.Textarea(
                attrs={
                    'class': "col form-control form-control-sm w-75",
                    'rows': '3',
                }
            ),
            'sales_channel': forms.Select(
                attrs={
                    'class': "form-select form-select-sm w-75"
                }
            ),
            'courier': forms.Select(
                attrs={
                    'class': "form-select form-select-sm w-75"
                }
            ),
            'persons': forms.NumberInput(
                attrs={
                    'class': "form-control form-control-sm w-50 p-2"
                }
            ),
            'delivery_price': forms.Select(
                attrs={
                    'class': "form-select form-select-sm w-50"
                }
            ),
            'discount_sum': forms.Select(
                attrs={
                    'class': "form-select form-select-sm w-100"
                }
            ),
            'pay_method': forms.Select(
                attrs={
                    'class': "form-select form-select-sm w-75"
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
                    "type": "tel",
                    "class": "col form-control form-control-sm w-75 fw-bold text-center",
                    "placeholder": "8(___)___-__-__",
                    "max-length": "18",
                    "autofocus": "True",
                    "data-tel-input": "True",
                    "autocomplete": "False"
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': "form-control form-control-sm w-75",
                    "max-length": "30",
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': "form-control form-control-sm",
                    'style': 'width: 345px',
                    'cols': "30",
                    'rows': "3",
                }
            ),
            'home': forms.TextInput(
                attrs={
                    'class': "form-control form-control-sm",
                    'style': "width: 130px",
                }
            ),
            'building': forms.TextInput(
                attrs={
                    'class': "form-control form-control-sm",
                    'style': "width: 130px",
                }
            ),
            'room': forms.TextInput(
                attrs={
                    'class': "form-control form-control-sm",
                    'style': "width: 130px",
                }
            ),
            'entrance': forms.TextInput(
                attrs={
                    'class': "form-control form-control-sm",
                    'style': "width: 130px",
                }
            ),
            'floor': forms.TextInput(
                attrs={
                    'class': "form-control form-control-sm ",
                    'style': "width: 130px",
                }
            ),
            'code': forms.TextInput(
                attrs={
                    'class': "form-control form-control-sm",
                    'style': "width: 130px",
                }
            ),
            'mark': forms.Textarea(
                attrs={
                    'class': "col form-control form-control-sm w-75",
                    'rows': '3',
                }
            ),
        }


class OrderCourierForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('courier',)
        widgets = {
            'courier': forms.Select(
                attrs={
                    'class': "form-select fw-bold",
                    'id': 'list_order_courier'
                }
            ),
        }
