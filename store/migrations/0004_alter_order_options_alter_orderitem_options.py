# Generated by Django 5.0.3 on 2024-03-28 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_alter_cart_options_alter_cartitem_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ('order',)},
        ),
    ]
