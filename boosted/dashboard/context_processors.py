from datetime import datetime

from django.conf import settings


def global_variables_loader(request):
    return {
        "release_year": datetime.now().year,
        "version": settings.VERSION,
        "github_url": settings.GITHUB_REPO,
    }
