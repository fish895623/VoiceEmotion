# Generated by Django 4.0.4 on 2022-05-06 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_board_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='img/%y/%m/%d'),
        ),
    ]