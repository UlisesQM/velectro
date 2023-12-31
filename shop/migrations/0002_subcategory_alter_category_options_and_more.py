# Generated by Django 4.1.5 on 2023-08-15 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Subcategoria', 'verbose_name_plural': 'subcategorias'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AddField(
            model_name='category',
            name='subcategory1',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='shop.subcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='shop.subcategory'),
        ),
    ]
