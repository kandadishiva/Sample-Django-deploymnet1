from django.shortcuts import render

# Create your views here.
from .models import *
print("2")
def home(request):
    return render(request,'home.html',{'name':'Shiva Prasad Reddy'})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2

    return render(request,'result.html',{'result':res})
def dashboard(request):
    cus=Customer.objects.all()
    return render(request,'dashboard.html',{'customers':cus})

def products(request):
    products=product.objects.all()
    b=[]
    for i in products:
        #a=i.tags.all()
        #b=a.values_list('name',flat=True)
        #print(b)
        #print(list(b))
        b.append(",".join(list(i.tags.all().values_list('name',flat=True))))
    print(b)
    con={'products':products,'tags':b}
    return render(request,'products.html',con)

def customers(request,cid):
    customer=Customer.objects.get(id=cid)
    customers=Customer.objects.all()
    orders=customer.order_set.all()
    order_count=orders.count()

    context={'customers':customers,'cust':customer,'ord':orders,'ordcount':order_count}
    print(context)
    return render(request,'customer.html',context)