# Generated by Django 4.1.4 on 2023-01-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_alter_sections_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
