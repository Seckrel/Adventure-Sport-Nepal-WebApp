# Generated by Django 3.2.5 on 2021-07-27 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ski', '0022_auto_20210727_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hook',
            name='ski',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ski_hook_related', related_query_name='ski_hooks', to='ski.ski'),
        ),
    ]