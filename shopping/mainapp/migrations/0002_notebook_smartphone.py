# Generated by Django 3.2.8 on 2021-10-24 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ')),
                ('display_type', models.CharField(max_length=255, verbose_name='Тип дисплея')),
                ('resolution', models.CharField(max_length=255, verbose_name='Разрешение экрана')),
                ('accum_volume', models.CharField(max_length=255, verbose_name='Ёмкость аккумулятора')),
                ('ram', models.CharField(max_length=255, verbose_name='Оперативная память')),
                ('sd', models.BooleanField(default=True)),
                ('sd_volume_max', models.CharField(max_length=255, verbose_name='Максимальный объём встраиваемой памяти')),
                ('main_cam_mp', models.CharField(max_length=255, verbose_name='Разрешение основой камеры')),
                ('frontal_cam_mp', models.CharField(max_length=255, verbose_name='Разрешение фронтальной камеры')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ')),
                ('display_type', models.CharField(max_length=255, verbose_name='Тип дисплея')),
                ('processor_freq', models.CharField(max_length=255, verbose_name='Частота процессора')),
                ('ram', models.CharField(max_length=255, verbose_name='Оперативная память')),
                ('video', models.CharField(max_length=255, verbose_name='Видеокарта')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='Время работы аккумулятора')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
