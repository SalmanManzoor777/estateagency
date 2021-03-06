# Generated by Django 3.1.7 on 2021-10-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_listing_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/user_directory')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
