# Generated by Django 3.2.5 on 2021-07-27 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PricingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_date', models.DateTimeField()),
                ('trek', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='trek.trek')),
            ],
        ),
        migrations.CreateModel(
            name='PackageInclusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inclusion_decription', models.TextField()),
                ('trek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trek.trek')),
            ],
        ),
        migrations.CreateModel(
            name='PackageExclusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exclusion_decription', models.TextField()),
                ('trek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trek.trek')),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.PositiveIntegerField()),
                ('end', models.PositiveIntegerField()),
                ('itinerary_description', models.TextField()),
                ('trek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trek.trek')),
            ],
        ),
        migrations.CreateModel(
            name='Hook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hook_title', models.CharField(max_length=50)),
                ('hook_text', models.TextField()),
                ('trek', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='trek.trek')),
            ],
        ),
        migrations.CreateModel(
            name='ExpeditionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expedition_title', models.CharField(max_length=50)),
                ('expedition_description', models.TextField()),
                ('trek', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='trek.trek')),
            ],
        ),
    ]