# Generated by Django 4.2.3 on 2023-08-08 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recreation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lodging', '0005_remove_lodgingscrap_createdat_review_createdat'),
    ]

    operations = [
        migrations.CreateModel(
            name='teamSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamToken', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('teamName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='teamUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamSpace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamSpace', to='team.teamspace')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='teamShoppingScrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('teamSpace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamSpaceShopping', to='team.teamspace')),
            ],
        ),
        migrations.CreateModel(
            name='teamRecreationScrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recreation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recreation', to='recreation.recreationmain')),
                ('teamSpace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamSpaceRecreation', to='team.teamspace')),
            ],
        ),
        migrations.CreateModel(
            name='teamLodgingScrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lodging', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lodging', to='lodging.lodgingmain')),
                ('teamSpace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamSpaceLodging', to='team.teamspace')),
            ],
        ),
    ]
