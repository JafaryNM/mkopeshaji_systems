# Generated by Django 4.0.6 on 2022-07-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_remove_loan_fieldname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='amount',
            field=models.FloatField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='repayment_date',
            field=models.DateField(null=True),
        ),
    ]
