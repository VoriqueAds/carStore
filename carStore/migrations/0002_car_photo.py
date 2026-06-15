from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carStore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Foto Principal'),
        ),
    ]
