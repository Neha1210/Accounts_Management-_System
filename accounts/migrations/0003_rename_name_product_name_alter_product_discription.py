# Generated by Django 4.0 on 2022-01-16 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_tag_order_customer_order_product_product_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='Discription',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
