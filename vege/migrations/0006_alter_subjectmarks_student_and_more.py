# Generated by Django 5.0.2 on 2024-03-06 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_subject_alter_student_student_id_subjectmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmarks',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentmarks', to='vege.student'),
        ),
        migrations.AlterField(
            model_name='subjectmarks',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vege.subject'),
        ),
    ]
