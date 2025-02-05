# Generated by Django 5.1.5 on 2025-02-01 12:44

import apps.utils
import django.db.models.deletion
import imagekit.models.fields
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=255, unique=True, verbose_name='SLUG')),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories/', verbose_name='Изображение категории')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активная категория')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='settings.category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Тут нужно писать название товара', max_length=255, verbose_name='Название')),
                ('slug', models.TextField(unique=True, verbose_name='SLUG')),
                ('description', models.TextField(help_text='Тут нужно писать описание товара', verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, help_text='Тут нужно писать цену товара', max_digits=100, verbose_name='Цена')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('category', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='settings.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(help_text='Ваше фото будет пересохранено на формат <webp>', upload_to=apps.utils.get_product_upload_path, verbose_name='Изображение')),
                ('position', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='settings.product', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'ordering': ['position'],
            },
        ),
    ]
