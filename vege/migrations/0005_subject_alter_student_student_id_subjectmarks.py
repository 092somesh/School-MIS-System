# Generated by Django 5.0.2 on 2024-03-06 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0004_department_studentid_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stid', to='vege.studentid'),
        ),
        migrations.CreateModel(
            name='SubjectMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart', to='vege.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vege.student')),
            ],
            options={
                'unique_together': {('student', 'subject')},
            },
        ),
    ]