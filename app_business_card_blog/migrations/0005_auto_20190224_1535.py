# Generated by Django 2.1.7 on 2019-02-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_business_card_blog', '0004_auto_20190224_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='detail_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/details/', verbose_name='detail_'),
        ),
        migrations.AlterField(
            model_name='blogarticles',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/preview/', verbose_name='preview_'),
        ),
    ]