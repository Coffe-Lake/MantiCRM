from django.shortcuts import render
from django.views import View


class ClientView(View):
    def post(self, request, *args, **kwargs):
        pass


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
