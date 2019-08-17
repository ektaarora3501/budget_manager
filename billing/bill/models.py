from django.db import models
#from django.db import models
from django.urls import reverse
import datetime
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Regis(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user_name=models.CharField('Dude Name',max_length=100,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=12)
    #cnf_pass=models.CharField(max_length=12)

    def __str__(self):
        return f'{self.user_name},{self.email}'

#    def get_absolute_url(self):
#        return reverse('profile-detail',args=[(self.user_name)])

class login(models.Model):
    username=models.CharField(max_length=100)
    session=models.CharField(max_length=2,default=0)

    def __str__(self):
        return f"{self.username}"

# Create your models here.

class budget(models.Model):
    username=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    amount=models.IntegerField(default=0)
    date=models.DateField(_("Date"),default=datetime.date.today)
    x=datetime.datetime.now()
    month=models.CharField(default=x.month,max_length=2)

    def __str__(self):
        return f"{self.username},{self.message},{self.amount},{self.date}"

class remind(models.Model):
    username=models.CharField(max_length=100)
    pay=models.CharField(max_length=100)
    amount=models.DecimalField(max_length=100,default=0.0,decimal_places=4,max_digits=8)
    date=models.DateField(_("Date"),default=datetime.date.today)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username},{self.pay},{self.amount},{self.date}"

class sumup(models.Model):
    username=models.CharField(max_length=100)
    total=models.IntegerField(default=0)
    x=datetime.datetime.now()
    month=models.CharField(default=x.month,max_length=2)

    def __str__(self):
        return f"{self.username},{self.total},{self.month}"
