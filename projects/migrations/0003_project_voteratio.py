# Generated by Django 4.0.1 on 2022-11-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_votetotal_review_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='voteRatio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
