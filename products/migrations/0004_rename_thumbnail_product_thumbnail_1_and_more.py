# Generated by Django 4.0.4 on 2022-05-25 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_image_imageurl_rename_color_optioncolor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='thumbnail',
            new_name='thumbnail_1',
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail_2',
            field=models.CharField(max_length=260, null=True),
        ),
    ]
