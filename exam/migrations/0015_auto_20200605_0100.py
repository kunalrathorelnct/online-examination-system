# Generated by Django 3.0.6 on 2020-06-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0014_remove_section_section_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='total_marks',
            field=models.IntegerField(default=0),
        ),
    ]
