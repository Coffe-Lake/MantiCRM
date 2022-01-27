# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render
# from django.urls import reverse_lazy
#
# from document.models import Invoice
#
# from django.views.generic import DetailView
#
# from orders.models import Order
#
#
# class InvoiceDetailView(LoginRequiredMixin, DetailView):
#     """Накладная"""
#
#     model = Invoice
#     template_name = 'orders/invoice/invoice.html'
#     extra_context = {'title': "Накладная"}
#     redirect_to_login = True
#     success_url = reverse_lazy('invoice')
