# Generated by Django 4.2.5 on 2023-10-15 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_date_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_create',
            field=models.DateField(default='2023-10-15', verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_last_change',
            field=models.DateField(default='2023-10-15', verbose_name='дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='цена за покупку'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(blank=True, null=True, verbose_name='номер версии')),
                ('version_name', models.CharField(max_length=100, verbose_name='название версии')),
                ('is_active', models.BooleanField(default=True, verbose_name='признак текущей версии')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='catalog.product', verbose_name='продукты')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
                'ordering': ('product',),
            },
        ),
    ]
