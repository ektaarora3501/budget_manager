from django.shortcuts import render,redirect
from bill.models import Regis,login,budget,remind
from bill.forms import SignupForm,LogForm,AddForm,RemindForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

# Create your views here.

def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method=='POST':
       form =SignupForm(request.POST)
       print("post")

       if form.is_valid():
           user=form.cleaned_data['user_name']
           print(user)
           us=Regis()
           #url=confirm/user
           print("form valid")
           us.first_name=form.cleaned_data['first_name']
           us.last_name=form.cleaned_data['last_name']
           us.password=form.cleaned_data['password']
           us.user_name=form.cleaned_data['user_name']
           us.email=form.cleaned_data['email']

           us.save()


           return HttpResponseRedirect(reverse('confirm',args=(user,)))

    else:
        #proposed_date=datetime.date.today()+datetime.timedelta(weeks=3)

        form=SignupForm()

    context={
    'form':form,
    #'book_instance':book_instance,
    }


    return render(request,'user_form.html',context)

def Login(request):
    if request.method=='POST':
       form =LogForm(request.POST)
       print("post")

       if form.is_valid():
           user=form.cleaned_data['username']
           us=login()
           us.username=user
           try:
               us.save()
           except:
               pass
           print(user)
           return HttpResponseRedirect(reverse('main',args=(user,)))

    else:
        #proposed_date=datetime.date.today()+datetime.timedelta(weeks=3)

        form=LogForm()

    context={
    'form':form,
    #'book_instance':book_instance,
    }


    return render(request,'login.html',context)

def confirm(request,user):
    context={
    'user':user,
    }

    return render(request,'confirm.html',context)


def Official(request,username):
    if login.objects.filter(username=username).exists():
        x=datetime.datetime.now()
        sts=budget.objects.filter(username=username,month=x.month).all()
        context={
        'sts':sts,
        }
        return render(request,'official.html',context)

    else:
        return Login(request)







def dashboard(request,username,month):
    if login.objects.filter(username=username).exists():
        st=Regis.objects.get(user_name=username)

        total=0
        sts=budget.objects.filter(username=username,month=month).all()
        #budget.objects.filter(id=7).delete()
        for st in sts:
            print(st.username)
            print(st.message)
            print(st.amount)
            print("id",st.id)
            print("date",st.date.month)
            total+=st.amount
        print(total)
        context={
        'user':username,
        'sts':sts,
        'total':total,
        }
        return render(request,'dashboard.html',context)

    else:
        return Login(request)

def show(request,user):
    if login.objects.filter(username=user).exists():
        values=remind.objects.filter(username=user).all()

        for value in values:
            print(value.username)
            print(value.pay)

        context={
        'user':user,
        'values':values,
        }

        return render(request,'remind_show.html',context)

    else:
        return Login(request)


def add(request,user):
    if login.objects.filter(username=user).exists():
        if request.method=='POST':
           form =AddForm(request.POST)
           print("post")

           if form.is_valid():
               us=budget()
               us.username=user
               us.message=form.cleaned_data['message']
               us.amount=form.cleaned_data['amount']

               try:
                   us.save()
               except:
                   pass
               x=datetime.datetime.now().month
               print(x)

               return HttpResponseRedirect(reverse('dashboard',args=(user,x)))

        else:
            #proposed_date=datetime.date.today()+datetime.timedelta(weeks=3)

            form=AddForm()

        context={
        'form':form,

        }


        return render(request,'add.html',context)

    else:
        return Login(request)


def Remind(request,user):
    if login.objects.filter(username=user).exists():
        if request.method=='POST':
           form =RemindForm(request.POST)
           print("post")

           if form.is_valid():
               us=remind()
               us.username=user
               us.amount=form.cleaned_data['amount']
               us.pay=form.cleaned_data['to_pay']
               us.date=form.cleaned_data['date']

               try:
                   us.save()
               except:
                   pass
               x=datetime.datetime.now().month
               print(x)
               return HttpResponseRedirect(reverse('dashboard',args=(user,x)))

        else:
            #proposed_date=datetime.date.today()+datetime.timedelta(weeks=3)

            form=RemindForm()

        context={
        'form':form,

        }


        return render(request,'remind_form.html',context)

    else:
        return Login(request)


def Paid(request,id,user):
    value=remind.objects.get(id=id)
    bug=budget()
    bug.username=user
    bug.message=value.pay
    bug.amount=value.amount
    bug.save()
    x=datetime.datetime.now().month
    print(x)
    remind.objects.filter(id=id).delete()

    return dashboard(request,user,x)




def logout(request,user):
    login.objects.filter(username=user).delete()
    return index(request)

def delete(request,id,user):
    x=budget.objects.get(id=id)
    print("value of x=",x.month)
    budget.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('dashboard',args=(user,x.month)))
