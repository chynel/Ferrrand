# Generated by Django 3.2.13 on 2023-04-21 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0003_alter_message_reponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reponse',
            field=models.TextField(default="Vous n'avez pas encore de réponse à ce message"),
        ),
    ]
