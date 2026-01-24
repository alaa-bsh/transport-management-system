from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .services.analytics_service import DashboardCalculator


@csrf_exempt
@login_required
@require_GET
def commercial_analysis(request):
    try:
        period_months = int(request.GET.get('period', 12))
        
        data = DashboardCalculator.get_commercial_analysis(period_months)
        
        return JsonResponse({
            'success': True,
            'data': data,
            'period': f"{period_months} mois"
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e),
            'data': None
        }, status=500)


@csrf_exempt
@login_required
@require_GET
def operational_analysis(request):
    try:
        period_months = int(request.GET.get('period', 12))
        
        data = DashboardCalculator.get_operational_analysis(period_months)
        
        return JsonResponse({
            'success': True,
            'data': data,
            'period': f"{period_months} mois"
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e),
            'data': None
        }, status=500)


@csrf_exempt
@login_required
@require_GET
def complete_dashboard(request):
    try:
        commercial_period = int(request.GET.get('commercial_period', 12))
        operational_period = int(request.GET.get('operational_period', 12))
        
        commercial_data = DashboardCalculator.get_commercial_analysis(commercial_period)
        operational_data = DashboardCalculator.get_operational_analysis(operational_period)
        realtime_data = DashboardCalculator.get_realtime_metrics()
        
        response_data = {
            'commercial': commercial_data,
            'operational': operational_data,
            'realtime': realtime_data
        }
        
        return JsonResponse({
            'success': True,
            'data': response_data
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e),
            'data': None
        }, status=500)


@csrf_exempt
@login_required
@require_GET
def realtime_metrics(request):
    try:
        data = DashboardCalculator.get_realtime_metrics()
        
        return JsonResponse({
            'success': True,
            'data': data
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e),
            'data': None
        }, status=500)


from django.utils import timezone