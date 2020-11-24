# Generated by Django 3.1.3 on 2020-11-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('createdDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('quantity', models.FloatField(null=True)),
                ('unit', models.CharField(max_length=20)),
                ('price', models.IntegerField(null=True)),
                ('pricePaid', models.IntegerField(null=True)),
                ('dealer', models.CharField(max_length=30)),
                ('receiver', models.CharField(max_length=30)),
                ('remarks', models.TextField(max_length=200, null=True)),
            ],
        ),
    ]
