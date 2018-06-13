# Generated by Django 2.0.5 on 2018-06-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_date']},
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='due_date',
            field=models.DateTimeField(default=True, null=True),
        ),
    ]