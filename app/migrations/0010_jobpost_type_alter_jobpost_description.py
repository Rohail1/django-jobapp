# Generated by Django 4.2.2 on 2023-07-17 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_skills_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='type',
            field=models.CharField(choices=[('F', 'Full Time'), ('P', 'Part Time')], default='F', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='description',
            field=models.TextField(),
        ),
    ]
