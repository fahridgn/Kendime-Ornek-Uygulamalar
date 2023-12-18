# context_processors.py dosyasında
from .models import Theme

def themes(request):
    themes = Theme.objects.all().values()
    themes_dict = {}
    for theme in themes:
        themes_dict[theme['name']] = {
            'tag': theme['tag'],
            'attrs': theme['attrs'],
            'value': theme['value'],
        }

    return {'themes': themes_dict}