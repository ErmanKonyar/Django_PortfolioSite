# Generated by Django 4.2 on 2023-05-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_skill_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.CharField(max_length=250),
        ),
    ]
