# Generated by Django 3.2.7 on 2021-09-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_Img', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]