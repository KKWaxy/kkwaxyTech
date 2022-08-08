# Generated by Django 3.2.5 on 2022-08-08 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kkwaxyApp', '0006_alter_post_intro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Nom')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['updated_date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='kkwaxyApp.Tag'),
        ),
    ]