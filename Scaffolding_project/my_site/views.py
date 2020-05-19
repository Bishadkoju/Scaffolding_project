from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from account.models import Company
from .forms import AddCompanyForm
from django.urls import reverse_lazy
from .filters import CompanyFilter
# Create your views here.

def dashboard(request):
    
    return render(request,'dashboard.html',{})


class CompanyCreateView(SuccessMessageMixin,generic.CreateView):
    model=Company
    form_class=AddCompanyForm
    
    success_message="Company Successfully Created "
    template_name='company/company_add.html'
    

class CompanyUpdateView(SuccessMessageMixin,generic.UpdateView):
    model=Company
    form_class=AddCompanyForm
    success_message="Company Successfully Updated"
    template_name='company/company_update.html'
    

class CompanyListView(generic.ListView):
    model=Company
    paginated_by=10
    context_object_name='company_list'
    template_name='company/company_list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['filter']=CompanyFilter(self.request.GET,self.get_queryset())
        return context

class CompanyDetailView(generic.DetailView):
    model=Company
    context_object_name='company'
    template_name='company/company_detail.html'


class CompanyDeleteView(SuccessMessageMixin,generic.DeleteView):
    model=Company
    context_object_name='company'
    template_name='company/company_delete.html'
    success_message="Company Deleted Successfully"
    success_url=reverse_lazy('company_list')

    

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)