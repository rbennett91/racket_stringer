from django.db import migrations
from django.conf import settings


def update_site_name(apps, schema_editor):
    SiteModel = apps.get_model('sites', 'Site')
    # TODO: maybe don't hard code this here, update this.
    # Make this a setting, make a note in project README
    domain = '192.168.1.111:8080'
    name = 'racket_stringer'

    SiteModel.objects.update_or_create(
        pk=settings.SITE_ID,
        domain=domain,
        name=name
    )


class Migration(migrations.Migration):
    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('racket_stringer', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(update_site_name),
    ]
