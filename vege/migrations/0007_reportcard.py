# Generated by Django 5.0.2 on 2024-03-08 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_alter_subjectmarks_student_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_report_card_genration', models.DateField(auto_created=True)),
                ('student_rank', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentreportcard', to='vege.student')),
            ],
        ),
    ]
