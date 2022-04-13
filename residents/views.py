from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import View
from .models import BaseResident, Own, EntityResident, IndividualResident, BaseResidentRel

# Create your views here.
def lk(request):
    return render(request, 'residents/index.html')


class BaseView(View):

    def get(self, request):
        if self.request.user.is_personnel:
            resident = get_object_or_404(EntityResident, staff=self.request.user)
            residents_record = get_object_or_404(BaseResidentRel, entity_resident=resident)
        elif not self.request.user.is_personnel:
            resident = get_object_or_404(IndividualResident, user=self.request.user)
            residents_record = get_object_or_404(BaseResidentRel, individual_resident=resident)

        else:
            resident = None
        if resident is not None:
            owns = Own.objects.filter(owners=residents_record)

        context = {
            'owns': owns,
            'resident': resident
        }

        return render(request, 'residents/profile.html', context)
