from django.shortcuts import render,redirect
from bill.models import Regis,login,budget
from bill.forms import SignupForm,LogForm,AddForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

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
           return HttpResponseRedirect(reverse('dashboard',args=(user,)))

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


def dashboard(request,username):
    if login.objects.filter(username=username).exists():
        st=Regis.objects.get(user_name=username)

        total=0
        sts=budget.objects.filter(username=username).all()
        #budget.objects.filter(id=7).delete()
        for st in sts:
            print(st.username)
            print(st.message)
            print(st.amount)
            print("id",st.id)
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

               return HttpResponseRedirect(reverse('dashboard',args=(user,)))

        else:
            #proposed_date=datetime.date.today()+datetime.timedelta(weeks=3)

            form=AddForm()

        context={
        'form':form,
        #'book_instance':book_instance,
        }


        return render(request,'add.html',context)

    else:
        return Login(request)



def logout(request,user):
    login.objects.filter(username=user).delete()
    return index(request)

def delete(request,id,user):
    budget.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('dashboard',args=(user,)))
