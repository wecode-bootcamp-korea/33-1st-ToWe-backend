# Generated by Django 4.0.4 on 2022-06-02 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_orderstates_orderdetailstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order_detail_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.orderdetailstatus'),
        ),
    ]
