# Generated by Django 3.2.5 on 2021-07-29 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ski', '0027_auto_20210727_1417'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='pricinginfo',
            name='price_gte_0',
        ),
        migrations.AddConstraint(
            model_name='pricinginfo',
            constraint=models.CheckConstraint(check=models.Q(('price__gte', 0)), name='ski_price_gte_0'),
        ),
    ]
