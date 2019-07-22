from django.forms import PasswordInput,forms,CharField,EmailField,IntegerField
from bill.models import Regis
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class SignupForm(forms.Form):
    first_name=CharField(max_length=100)
    last_name=CharField(max_length=100)
    user_name=CharField(max_length=100)
    email=EmailField()
    password=CharField(max_length=12,widget=PasswordInput,help_text="password must be between 8 to 12 characters long")
    cnf_pass=CharField(max_length=12,widget=PasswordInput)



    def clean_cnf_pass(self):
        print('here')
        pas=self.cleaned_data['password']
        cnf=self.cleaned_data['cnf_pass']
        if cnf !=pas:
            raise ValidationError(_("please reconfirm your password"))
        print(cnf)

        if len(pas)<8:
           raise ValidationError(_('Password must be atleast 8 digits long '))
        return pas

    def clean_user_name(self):
        name=self.cleaned_data['user_name']
        if Regis.objects.filter(user_name=name).exists():
            raise ValidationError(_(" The given username already exists"))

        return name

    def clean_email(self):
        name=self.cleaned_data['email']
        if Regis.objects.filter(email=name).exists():
            raise ValidationError(_(" The given Email already exists"))

        return name






class LogForm(forms.Form):
    username=CharField(max_length=100)
    password=CharField(max_length=12,widget=PasswordInput)

    def clean_password(self):
        name=self.cleaned_data['username']
        pas=self.cleaned_data['password']

        if Regis.objects.filter(user_name=name).exists():
            pass
        else:
            raise ValidationError(_('The given username does not exists'))


        val=Regis.objects.get(user_name=name)
        try :

            print(val.password)

        except:
            raise ValidationError(_("incorrect password !!"))

        if pas != val.password:
            raise ValidationError(_("incorrect password !!"))
        return pas


class AddForm(forms.Form):
    message=CharField(max_length=100,help_text="Enter message of your amount")
    amount=IntegerField()
