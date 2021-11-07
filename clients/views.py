from django.shortcuts import render
from django.views import View


class ClientView(View):
    def post(self, request, *args, **kwargs):
        pass

# TODO доработать
# class AddClient(View):
#     """Добавить клиент"""
#
#     def post(self, request, pk):
#         form = NewOrderForm(request.POST)
#         client = Client.objects.create(form)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.client = client
#             form.save()
#         return redirect(client.get_absolute_url())

# def get_client(request):
#     check = request.POST.get("submit")
#
#     firstname = ''
#     emailvalue = ''
#
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         firstname = form.cleaned_data.get("first_name")
#         lastname = form.cleaned_data.get("last_name")
#         emailvalue = form.cleaned_data.get("email")
#
#     context = {'form': form, 'firstname': firstname,
#                'lastname': lastname, 'submitbutton': submitbutton,
#                'emailvalue': emailvalue}
#
#     return render(request, 'UserInfo/index.html', context)
