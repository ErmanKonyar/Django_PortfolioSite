# Generated by Django 4.2 on 2023-05-02 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('position', models.CharField(max_length=100)),
            ],
        ),
    ]
