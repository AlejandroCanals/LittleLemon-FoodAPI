# Generated by Django 4.2.5 on 2023-09-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0002_menuitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
