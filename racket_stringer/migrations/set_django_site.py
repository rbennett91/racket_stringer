from django.db import migrations
from django.conf import settings


def update_site_name(apps, schema_editor):
    SiteModel = apps.get_model('sites', 'Site')

    SiteModel.objects.update_or_create(
        pk=settings.SITE_ID,
        domain=settings.SITE_DOMAIN,
        name='racket_stringer'
    )


class Migration(migrations.Migration):
    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('racket_stringer', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(update_site_name),
    ]
