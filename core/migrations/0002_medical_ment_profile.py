# Generated by Django 3.2 on 2023-09-11 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s1', models.CharField(max_length=200)),
                ('s2', models.CharField(max_length=200)),
                ('s3', models.CharField(max_length=200)),
                ('s4', models.CharField(max_length=200)),
                ('s5', models.CharField(max_length=200)),
                ('disease', models.CharField(max_length=200)),
                ('medicine', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='core.user')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='profile/avator.png', upload_to='')),
                ('birth_date', models.DateField(default='None')),
                ('region', models.CharField(default='', max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('country', models.CharField(default='Tanzania', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('time', models.CharField(max_length=200, null=True)),
                ('ment_day', models.DateTimeField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dor', to='core.user')),
                ('medical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medical', to='core.medical')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pat', to='core.user')),
            ],
        ),
    ]
