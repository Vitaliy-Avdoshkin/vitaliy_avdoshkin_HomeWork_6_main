# Generated by Django 5.1.2 on 2024-12-11 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_purchase_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="purchase_price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Цена"
            ),
        ),
    ]