# Generated by Django 4.1.3 on 2023-01-26 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departing_from', models.CharField(choices=[('Sukkur', 'Nawabshah'), ('Kotri', 'Mirpur Khas'), ('Shikarpur', 'Dadu'), ('Tando Allahyar', 'Shahdadko')], max_length=100)),
                ('final_destination', models.CharField(choices=[('lahore', 'japan'), ('chaina', 'france'), ('chaina', 'islamabab'), ('Tando Allahyar', 'Shahdadko')], max_length=100)),
                ('no', models.CharField(max_length=100)),
                ('yes', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('name_airline', models.CharField(max_length=100)),
                ('flight_number', models.IntegerField()),
                ('date2', models.DateField()),
                ('delayed', models.CharField(max_length=50)),
                ('canceled', models.CharField(max_length=50)),
                ('boarding', models.CharField(max_length=50)),
                ('hourse1', models.CharField(max_length=50)),
                ('hourse2', models.CharField(max_length=50)),
                ('hourse3', models.CharField(max_length=50)),
                ('hourse4', models.CharField(max_length=50)),
                ('hourse5', models.CharField(max_length=50)),
                ('never6', models.CharField(max_length=50)),
                ('days', models.CharField(max_length=50)),
                ('days2', models.CharField(max_length=50)),
                ('caused', models.CharField(choices=[('slect the reason', 'dont remember'), ('technical problem', 'bad weather conditions'), ('influence by other flights', 'other problem')], max_length=100)),
            ],
        ),
    ]
