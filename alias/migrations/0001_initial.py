# Generated by Django 4.0.5 on 2023-02-27 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=25)),
                ('value', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('alt', models.TextField(blank=True, help_text='Description', null=True)),
                ('val', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.SmallIntegerField(choices=[(1, 'bank'), (2, 'digital wallet')])),
                ('name', models.CharField(max_length=255)),
                ('iden', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('default', models.BooleanField(default=False)),
                ('dst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alias.paymentbrand')),
            ],
        ),
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=128)),
                ('des', models.TextField(max_length=500, null=True)),
                ('default', models.BooleanField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('soft_deleted', models.BooleanField(default=False, null=True)),
                ('contacts', models.ManyToManyField(to='alias.contactinformation')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='alias.alias')),
                ('payments', models.ManyToManyField(to='alias.paymentinformation')),
                ('socials', models.ManyToManyField(to='socialaccount.socialaccount')),
            ],
            options={
                'verbose_name_plural': 'Aliases',
                'ordering': ['-pk'],
            },
        ),
    ]
