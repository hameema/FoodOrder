# Generated by Django 2.2.2 on 2019-06-06 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20190606_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='desh',
        ),
        migrations.AlterField(
            model_name='order',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='order.menu'),
        ),
    ]
