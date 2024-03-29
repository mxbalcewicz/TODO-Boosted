# Generated by Django 4.2.3 on 2024-01-22 18:33

from django.db import migrations

def migrate_forwards(apps, schema_editor):
    BoostedGroup = apps.get_model("accounts", "BoostedGroup")

    for name in ["Admins", "User", "Viewer"]:
        BoostedGroup.objects.create(name=name)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_add_permissions_mixin_to_user_model'),
    ]

    operations = [
        migrations.RunPython(migrate_forwards, migrations.RunPython.noop)
    ]
