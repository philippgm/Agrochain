# Generated by Django 3.2.1 on 2022-02-16 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220216_1229'),
        ('product', '0005_auto_20220216_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transporteproduto',
            name='produto',
        ),
        migrations.AddField(
            model_name='transporteproduto',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.RemoveField(
            model_name='transporteproduto',
            name='transportador',
        ),
        migrations.AddField(
            model_name='transporteproduto',
            name='transportador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.transportador'),
        ),
    ]