from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from datetime import datetime

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=1036'
    },
    {
        'title': 'Via lactea',
        'user': {
            'name': 'C. Vander',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903'
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'The Test',
            'picture': 'https://picsum.photos/60/60/?image=1076'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=883'
    }
]


@login_required
def list_posts(request):
    return render(request, 'posts/feed.html', {'posts': posts})
