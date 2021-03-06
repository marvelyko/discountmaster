# Generated by Django 3.1.7 on 2021-03-10 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_sitemodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email', models.EmailField(max_length=254)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sitemodel')),
            ],
        ),
    ]
