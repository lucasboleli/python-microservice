# Generated by Django 3.1.3 on 2024-09-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('likes', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
            ],
        ),
        migrations.AddConstraint(
            model_name='productuser',
            constraint=models.UniqueConstraint(fields=('user_id', 'product_id'), name='user_product'),
        ),
    ]
