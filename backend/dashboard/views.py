from django.shortcuts import render

def dashboard(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'pages/dashboard.html', context)