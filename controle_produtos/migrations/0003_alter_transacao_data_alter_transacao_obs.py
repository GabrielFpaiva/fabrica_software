# Generated by Django 4.1.1 on 2022-09-18 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_produtos', '0002_transacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
