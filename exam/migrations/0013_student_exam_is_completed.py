# Generated by Django 3.0.6 on 2020-06-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_student_exam_is_started'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_exam',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]