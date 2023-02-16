from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages


from .models import *
from .forms import *
from .filters import *

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=CreateUserForm()
        if request.method=="POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
               form.save()
               user=form.cleaned_data.get('username')
               messages.success(request,"Account created successfully for"+" "+user)
               return redirect('login')
    

    context={'form':form}
    return render(request,'accounts/register.html',context) 


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username='username',password='password')
        
            if user is not None:
               login(request,user)
               return redirect('home')
            else:
               messages.info(request,"username or password is incorrect")
    
    context={}
    return render(request,'accounts/login.html',context)

def logout(request):
    logout(request)
    return redirect('login')

def Home(request):
    customers=Customer.objects.all()
    orders = Order.objects.all()

    total_customers=customers.count()

    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='pending').count()

    context={'orders':orders,'customers':customers,'total_orders':total_orders,
             'delivered':delivered,'pending':pending}

    return render(request,'accounts/home.html',context)

def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()

    total_orders=orders.count()

    # myfilter=OrderFilter(request.GET,queryset=orders)
    # orders=myfilter.queryset

    context={'customer':customer,'orders':orders,'total_orders':total_orders,}

    return render(request,'accounts/customer.html',context)

def products(request):
    products=product.objects.all()

    return render(request,'accounts/products.html',{'products':products})

def create_order(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    customer=Customer.objects.get(id=pk) 
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer) 
    # form=OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # print('printing post:',request.POST)
        # form=OrderForm(request.POST)
        formset=OrderFormSet(request.POST,instance=customer)  
        if formset.is_valid():
            formset.save()
            return redirect(reverse('home'))
    context={'formset':formset}
    return render(request,'accounts/create_order.html',context)

def update_order(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)

    if request.method=="POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    context={'form':form}
    return render(request,'accounts/update_order.html',context)

def delete_order(request,pk):
    order=Order.objects.get(id=pk)

    if request.method=="POST":
        order.delete()
        return redirect(reverse('home'))

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)


def create_customer(request):
    form=CustomerForm()

    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'accounts/create_customer.html',context)

def update_customer(request,pk):
    customer=Customer.objects.get(id=pk)
    form=CustomerForm(instance=customer)
    
    if request.method=='POST':
        form=CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'accounts/create_customer.html',context)

def Add_product(request):
    form=ProductForm()

    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'accounts/Add_product.html',context)

def view_product(request,pk):
    products=product.objects.filter(id=pk)
    context={'products':products}

    return render(request,'accounts/view_product.html',context)
 