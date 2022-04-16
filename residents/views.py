from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic.detail import View, DetailView

from .forms import CustomAuthForm, CustomAuthWithCodeForm
from .models import BaseResident, Own, EntityResident, IndividualResident, BaseResidentRel, User, Code2FA
from . import business_logic


def lk(request):
    return render(request, 'residents/index.html')


def signin(request):

    if request.method == 'GET':
        return render(request, 'residents/signin.html', {'form':CustomAuthForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        check_code = request.POST.get('check_code', None)
    if user is None:
        return render(request, 'residents/signin.html', {'form':CustomAuthForm(), 'error':'Account didn\'t found!'})
    elif check_code:
        code_2fa = business_logic.find_code(user)
        if request.POST['check_code'] == str(code_2fa.code):
            code_status = business_logic.delete_code(user)
            login(request, user)
            return redirect('residents:lk')
        else:
            return render(request, 'residents/signin.html', {'form':CustomAuthWithCodeForm(request.POST), 'error':'Wrong code!'})
    else:
        #SEND THE CODE
        code_status = business_logic.create_code(user)
        code_status = business_logic.send_code(user)
        return render(request, 'residents/signin.html', {'form':CustomAuthWithCodeForm(request.POST)})




class BaseView(View):

    def get(self, request):
        if self.request.user.is_personnel:
            resident = get_object_or_404(EntityResident, staff=self.request.user)
            residents_record = get_object_or_404(BaseResidentRel, entity_resident=resident)
        elif not self.request.user.is_personnel:
            resident = get_object_or_404(IndividualResident, user=self.request.user)
            residents_record = get_object_or_404(BaseResidentRel, individual_resident=resident)
        else:
            residents_record = None
        if resident is not None:
            owns = Own.objects.filter(owners=residents_record)

        context = {
            'owns': owns,
            'resident': resident
        }

        return render(request, 'residents/owns.html', context)


class ProfileDetailView(DetailView):
    template_name = 'residents/profile_detail.html'
    context_object_name = 'profile'
    model = User

    def get_object(self, queryset=None):
        return get_object_or_404(User, id=self.request.user.id)
