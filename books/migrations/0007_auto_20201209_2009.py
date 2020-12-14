# Generated by Django 3.0.8 on 2020-12-09 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20201208_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quote_image', to='books.Image'),
        ),
    ]