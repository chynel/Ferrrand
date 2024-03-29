# Generated by Django 3.2.13 on 2023-04-14 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom du service')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Nom de l'ofrre")),
                ('description', models.CharField(max_length=2500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services_Offres.service')),
            ],
        ),
    ]
