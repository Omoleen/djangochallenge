# Generated by Django 4.2.1 on 2023-06-03 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('bic', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contacts', to='mailer.company')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=150)),
                ('total', models.DecimalField(decimal_places=9, max_digits=18)),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='mailer.company')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='mailer.contact')),
            ],
        ),
    ]