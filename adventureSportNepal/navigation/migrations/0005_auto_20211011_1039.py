# Generated by Django 3.2.5 on 2021-10-11 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0004_alter_itineraryinfo_end'),
        ('navigation', '0004_alter_treknav_first_nav_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treknav',
            name='first_nav_item',
        ),
        migrations.AddField(
            model_name='treknav',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='trek.expeditioninfo'),
        ),
    ]
