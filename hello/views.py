from django.shortcuts import render
from django.http import JsonResponse
from .models import Message


def hello_world(request):
    """Main Hello World view - renders an HTML page."""
    # Get or create a hello world message stored in PostgreSQL
    message, created = Message.objects.get_or_create(
        text='Hello, World!',
        defaults={'text': 'Hello, World!'}
    )
    context = {
        'message': message.text,
        'created_at': message.created_at,
        'db_status': 'Connected ✅',
    }
    return render(request, 'hello/index.html', context)


def health_check(request):
    """Health check endpoint - returns JSON status."""
    try:
        # Test DB connection
        Message.objects.count()
        db_status = 'connected'
    except Exception as e:
        db_status = f'error: {str(e)}'

    return JsonResponse({
        'status': 'ok',
        'message': 'Hello, World!',
        'database': db_status,
    })
