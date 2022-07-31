# Generated by Django 4.0.5 on 2022-07-31 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('des', models.TextField(max_length=500, null=True)),
                ('soft_deleted', models.BooleanField(default=False, null=True)),
                ('path', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Aliases',
            },
        ),
    ]
