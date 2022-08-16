# Generated by Django 4.0.5 on 2022-08-16 09:19

from django.db import migrations, models
import django.db.models.deletion


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
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='alias.alias')),
            ],
            options={
                'verbose_name_plural': 'Aliases',
            },
        ),
    ]
