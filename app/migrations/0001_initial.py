# Generated by Django 4.1.1 on 2022-09-16 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='karyawan',
            fields=[
                ('idkaryawan', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('namakaryawan', models.CharField(max_length=100)),
                ('kontakkaryawan', models.IntegerField()),
                ('jobdesk', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='pembelian',
            fields=[
                ('idpembelian', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('tanggaltransaksi', models.DateField()),
                ('namasupplier', models.CharField(max_length=100)),
                ('idkaryawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.karyawan')),
            ],
        ),
    ]