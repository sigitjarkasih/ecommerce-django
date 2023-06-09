# Generated by Django 4.2.1 on 2023-05-17 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_city_state_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ['id'], 'verbose_name': 'toko', 'verbose_name_plural': 'Toko'},
        ),
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='alamat'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.city', verbose_name='kota'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='owner',
            field=models.CharField(max_length=100, verbose_name='pemilik'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='phone',
            field=models.CharField(max_length=50, null=True, verbose_name='no.telp/hp'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='postal_code',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='kodepos'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.state', verbose_name='provinsi'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nama')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description')),
                ('stock', models.IntegerField(verbose_name='stock')),
                ('weight', models.FloatField(verbose_name='weight')),
                ('price', models.FloatField(verbose_name='price')),
                ('image', models.ImageField(upload_to='images', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='store.category', verbose_name='kategori')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'products',
                'ordering': ['created_at'],
            },
        ),
    ]
