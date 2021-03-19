# Generated by Django 3.0.8 on 2021-02-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0006_auto_20210217_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveysetting',
            name='hasil_survey',
            field=models.FileField(default='media/', upload_to=''),
        ),
        migrations.AddField(
            model_name='surveysetting',
            name='press_release',
            field=models.FileField(default='media/', upload_to=''),
        ),
        migrations.AddField(
            model_name='surveysetting',
            name='survey_desc',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]