from django.db import models
from django.db.models import PROTECT


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    DisplayFields = ['created_at', 'first_name', 'last_name', 'quote_count']

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

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

