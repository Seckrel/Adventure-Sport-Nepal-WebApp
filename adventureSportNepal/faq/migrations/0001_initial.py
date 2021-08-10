# Generated by Django 3.2.5 on 2021-08-10 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(choices=[('ski', 'SKI'), ('trek', 'TREK'), ('paragliding', 'PARAGLIDING'), ('snowboarding', 'SNOWBOARDING')], default='ski', max_length=20)),
            ],
            options={
                'verbose_name': 'Frequently Asked Question',
                'verbose_name_plural': 'Frequently Asked Questions',
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('faq', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='question_and_answer', to='faq.faq')),
            ],
            options={
                'verbose_name': 'Question and Answer',
            },
        ),
    ]
