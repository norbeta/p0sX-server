# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-04 10:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=255, unique=True)),
                ('credit', models.IntegerField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=12)),
                ('crew', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CrewSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField()),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Crew')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.SmallIntegerField(choices=[(0, 'CASH'), (1, 'CREW'), (2, 'CARD'), (3, 'VIPPS'), (4, 'MCASH'), (5, 'MOBILEPAY'), (6, 'IZETTLE'), (7, 'UNDO')], default=0)),
                ('expression', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.SmallIntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField(default=0)),
                ('barcode', models.CharField(max_length=255)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('created_in_the_kitchen', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ItemIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default', models.BooleanField(default=False)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Ingredient')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('state', models.SmallIntegerField(choices=[(0, 'OPEN'), (1, 'DONE'), (2, 'ARCHIVED')], default=0)),
                ('payment_method', models.SmallIntegerField(choices=[(0, 'CASH'), (1, 'CREW'), (2, 'CARD'), (3, 'VIPPS'), (4, 'MCASH'), (5, 'MOBILEPAY'), (6, 'IZETTLE'), (7, 'UNDO')], db_index=True, default=0)),
                ('message', models.CharField(blank=True, max_length=64)),
                ('authenticated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cashier', to='pos.Crew')),
                ('crew', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchasing_crew', to='pos.Crew')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('ingredients', models.ManyToManyField(blank=True, to='pos.Ingredient')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderlines', to='pos.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('authenticated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Crew')),
            ],
        ),
        migrations.AddField(
            model_name='discount',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Item'),
        ),
    ]
