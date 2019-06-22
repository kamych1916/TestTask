# Generated by Django 2.2.2 on 2019-06-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_auto_20190622_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='time',
            field=models.CharField(max_length=100, null=True, verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='chats_users',
            name='id_chat',
            field=models.ForeignKey(null=True, on_delete=False, to='chats.Chats', verbose_name='чат'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='id_chat',
            field=models.ForeignKey(null=True, on_delete=False, to='chats.Chats', verbose_name='чат'),
        ),
    ]
