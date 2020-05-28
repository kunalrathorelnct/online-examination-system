# Generated by Django 3.0.2 on 2020-05-28 11:24

from django.db import migrations, models
import django.db.models.deletion
import exam.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_code', models.CharField(max_length=20, unique=True)),
                ('start_time', models.DateTimeField()),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('ex_img', models.FileField(blank=True, null=True, upload_to=exam.models.Question.file_path)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warning_count', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('ss', models.FileField(blank=True, null=True, upload_to=exam.models.Student_Exam.file_path)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('response', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Question')),
                ('student_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Student_Exam')),
            ],
        ),
    ]
