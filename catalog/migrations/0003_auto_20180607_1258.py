# Generated by Django 2.0.5 on 2018-06-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180607_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='due_date',
            field=models.DateField(default=True, null=True),
        ),
    ]