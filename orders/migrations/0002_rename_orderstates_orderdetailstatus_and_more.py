# Generated by Django 4.0.4 on 2022-05-31 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderStates',
            new_name='OrderDetailStatus',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='order_state',
            new_name='order_detail_status',
        ),
        migrations.RenameField(
            model_name='orderdetailstatus',
            old_name='state',
            new_name='name',
        ),
        migrations.AlterModelTable(
            name='orderdetailstatus',
            table='order_detail_statuses',
        ),
    ]