# Generated by Django 3.1.7 on 2021-04-20 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20210417_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.user')),
                ('response', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.comment')),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]