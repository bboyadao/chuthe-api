# Generated by Django 4.0.5 on 2022-07-31 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alias', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alias',
            name='des',
            field=models.TextField(max_length=500, null=True),
        ),
    ]