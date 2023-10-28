from django.contrib import admin
from .models import Record, Product, AccountLabel, Opportunities, OppStage

admin.site.register(Record)
admin.site.register(Product)
admin.site.register(AccountLabel)
admin.site.register(Opportunities)
admin.site.register(OppStage)
# admin.site.register(Quote)
