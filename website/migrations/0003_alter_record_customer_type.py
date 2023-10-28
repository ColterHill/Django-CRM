# Generated by Django 4.2.6 on 2023-10-27 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_record_customer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='customer_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='website.accountlabel', verbose_name='AccountLabel'),
        ),
    ]
