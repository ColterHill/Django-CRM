# Generated by Django 4.2.6 on 2023-10-25 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_record_quote_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='quote_count',
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
    ]
