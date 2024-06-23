from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import Customer
from django.shortcuts import render, get_object_or_404
from .forms import CustomerForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserCreationForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'form': form})

@login_required
def customers_view(request):
    customers = Customer.objects.all().order_by('first_name')
    paginator = Paginator(customers, 10)  # Show 10 customers per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'accounts/customers.html', {'page_obj': page_obj})

@login_required
def customer_list_view(request):
    customers = Customer.objects.all().order_by('first_name')
    paginator = Paginator(customers, 10)  # Show 10 customers per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'accounts/customer_list.html', {'page_obj': page_obj})

@login_required
def customer_detail_view(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'accounts/customer_detail.html', {'customer': customer})

@login_required
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_by = request.user
            customer.save()
            return redirect('customers')
        else:
            print(form.errors) 
    else:
        form = CustomerForm()
    return render(request, 'accounts/create_customer.html', {'form': form})

@login_required
def update_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
        else:
            print(form.errors)  
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'accounts/update_customer.html', {'form': form})

@login_required
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect(reverse('customer_list'))
    return render(request, 'accounts/delete_customer.html', {'customer': customer})


@csrf_exempt
@api_view(['POST'])
def api_login(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'}, status=400)