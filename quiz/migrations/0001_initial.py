# Generated by Django 2.0.1 on 2018-01-26 10:44

from django.db import migrations, models
import django.db.models.deletion
import quiz.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('population', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag_image', models.ImageField(upload_to=quiz.models.get_image_path)),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='flag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Flag'),
        ),
    ]