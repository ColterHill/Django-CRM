from django.db import models
from django.db.models import PROTECT
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class AccountLabel(models.Model):
    account_type_label = models.CharField(max_length=50)
    description = models.TextField(null=False, blank=False)
    
    def __str__(self) -> str:
        return self.account_type_label


class Record(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email', max_length=50)
    phone = models.CharField('Phone', max_length=15)
    address = models.CharField('Address', max_length=100)
    city = models.CharField('City', max_length=50)
    state = models.CharField('State', max_length=50)
    zipcode = models.CharField('Zipcode', max_length=20)
    customer_type = models.ForeignKey(AccountLabel, verbose_name='Customer Type', on_delete=models.PROTECT, null=True, blank=False)
    primary_rep = models.ForeignKey(User, verbose_name='Primary Rep', on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
    
class OppStage(models.Model):
    stage_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.stage_name
    
    
class Opportunities(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    opp_name = models.CharField('Opp Name', max_length=50)
    account_name = models.ForeignKey(Record, verbose_name='Account Name', on_delete=models.PROTECT, null=True, blank=False)
    opp_owner = models.ForeignKey(User, verbose_name='Opp Owner', on_delete=models.PROTECT, null=True, blank=False)
    stage = models.ForeignKey(OppStage, verbose_name='Stage', on_delete=models.PROTECT, null=True, blank=False)
    quote_amount = models.PositiveIntegerField('Quote Amount', default=0)
    profit = models.PositiveIntegerField('Profit', default=0)
    
    def __str__(self):
        return self.opp_name
    
    


class Product(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    sell_price = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)
    product_type = models.CharField(max_length=50)
    


    # def count_of_quotes(self):
    #     self.quote_count = len(models.Quote.objects.filter(account_name='Record'))
    #     return self.quote_count

#     @property
#     def quote_count(self):
#         quote_count = len(models.Quote.objects.filter(account_name='Record'))
#         return quote_count
#
#
# class Quote(models.Model):
#     quote_name = models.CharField(max_length=100)
#     account_name = models.ForeignKey(Record, PROTECT)
#     sales_amount = models.DecimalField(default=0, null=True, blank=True, max_digits=9, decimal_places=2)

