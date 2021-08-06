from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView, FormView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from .models import Customer
from .forms import CustomerForm

DEFAULT_PAGINATE = 25
class CustomerListView(ListView):
    context_object_name = 'customer_list'

    def get(self,request):
        search = request.GET.get('word', '')
        paginate_by = request.GET.get('paginate', DEFAULT_PAGINATE)
        queryset = Customer.objects.all()

        if search:
            queryset = queryset.filter(
                Q(tc_no__icontains=search)|
                Q(name__icontains=search)|
                Q(surname__icontains=search)|
                Q(phone__icontains=search)|
                Q(city__icontains=search)|
                Q(state__icontains=search) 
            )

        paginator = Paginator(queryset.order_by('-id'), paginate_by)
        page = request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        
        context = {
            'customer_list': queryset, 
            'word': search, 
            'paginate': paginate_by
        }
        return render(request, "index.html", context)


class NewCustomerFormView(View):
    form_class = CustomerForm
    template_name = 'new_customer.html'

    def get(self,request,*args, **kwargs):
        return render(request, 'new_customer.html')

    def post(self,request,*args, **kwargs):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        context = {'form': form}

        return render(request, 'new_customer.html', context)


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    

class CustomerUpdateView(UpdateView):
    model = Customer
    success_url = '/'
    template_name = "customer_form_update.html"

    form_class = CustomerForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
            

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'confirm_delete.html'
    success_url = '/'
    

class RegisterFormView(FormView):
    template_name = "registration/register.html"
    form_class = UserCreationForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
            return render(request, "registration/register.html", {'form': form})