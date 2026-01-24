from datetime import datetime, timedelta
from django.db.models import Count, Sum, Q
from django.db.models.functions import TruncMonth
from django.utils import timezone


class DashboardCalculator:
    
    @staticmethod
    def get_commercial_analysis(period_months=12):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30 * period_months)
        
        expedition_change = DashboardCalculator._calculate_expedition_change(period_months)
        revenue_change = DashboardCalculator._calculate_revenue_change(period_months)
        top_clients = DashboardCalculator._get_top_clients(period_months)
        top_destinations = DashboardCalculator._get_top_destinations(period_months)
        monthly_trends = DashboardCalculator._get_monthly_expeditions_trend(period_months)
        
        return {
            'expedition_change': expedition_change,
            'revenue_change': revenue_change,
            'top_clients': top_clients,
            'top_destinations': top_destinations,
            'monthly_trends': monthly_trends,
            'period_months': period_months
        }
    
    @staticmethod
    def get_operational_analysis(period_months=12):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30 * period_months)
        
        tour_evolution = DashboardCalculator._calculate_tour_evolution(period_months)
        delivery_success = DashboardCalculator._calculate_delivery_success(period_months)
        top_drivers = DashboardCalculator._get_top_drivers(period_months)
        incident_zones = DashboardCalculator._get_incident_zones(period_months)
        peak_activity = DashboardCalculator._get_peak_activity_months(period_months)
        tours_per_month = DashboardCalculator._get_tours_per_month_chart(period_months)
        
        return {
            'tour_evolution': tour_evolution,
            'delivery_success': delivery_success,
            'top_drivers': top_drivers,
            'incident_zones': incident_zones,
            'peak_activity': peak_activity,
            'tours_per_month': tours_per_month,
            'period_months': period_months
        }
    
    @staticmethod
    def get_realtime_metrics():
        now = timezone.now()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        
        today_expeditions = Expedition.objects.filter(
            date_expedition__gte=today_start
        ).count()
        
        today_revenue = Expedition.objects.filter(
            date_expedition__gte=today_start
        ).aggregate(total=Sum('montant_total'))['total'] or 0
        
        today_tours = Tournee.objects.filter(
            date_depart__gte=today_start
        ).count()
        
        today_incidents = Incident.objects.filter(
            date_incident__gte=today_start
        ).count()
        
        active_tours = Tournee.objects.filter(statut='en_cours').count()
        pending_expeditions = Expedition.objects.filter(statut='en_attente').count()
        
        return {
            'today': {
                'expeditions': today_expeditions,
                'revenue': float(today_revenue),
                'tours': today_tours,
                'incidents': today_incidents
            },
            'ongoing': {
                'active_tours': active_tours,
                'pending_expeditions': pending_expeditions
            },
            'updated_at': now.isoformat()
        }
    
    @staticmethod
    def _calculate_expedition_change(period_months):
        end_date = timezone.now()
        current_start = end_date - timedelta(days=30 * period_months)
        
        current_count = Expedition.objects.filter(
            date_expedition__gte=current_start
        ).count()
        
        previous_start = current_start - timedelta(days=30 * period_months)
        previous_end = current_start
        previous_count = Expedition.objects.filter(
            date_expedition__gte=previous_start,
            date_expedition__lt=previous_end
        ).count()
        
        if previous_count > 0:
            change_percent = ((current_count - previous_count) / previous_count) * 100
        else:
            change_percent = 0
        
        return {
            'current_count': current_count,
            'previous_count': previous_count,
            'change_percent': round(change_percent, 1),
            'is_increase': change_percent >= 0,
            'label': f"{'+' if change_percent >= 0 else ''}{round(change_percent, 1)}%"
        }
    
    @staticmethod
    def _calculate_revenue_change(period_months):
        end_date = timezone.now()
        current_start = end_date - timedelta(days=30 * period_months)
        
        current_revenue = Expedition.objects.filter(
            date_expedition__gte=current_start
        ).aggregate(total=Sum('montant_total'))['total'] or 0
        
        previous_start = current_start - timedelta(days=30 * period_months)
        previous_end = current_start
        previous_revenue = Expedition.objects.filter(
            date_expedition__gte=previous_start,
            date_expedition__lt=previous_end
        ).aggregate(total=Sum('montant_total'))['total'] or 0
        
        if previous_revenue > 0:
            change_percent = ((current_revenue - previous_revenue) / previous_revenue) * 100
        else:
            change_percent = 0
        
        return {
            'current_revenue': float(current_revenue),
            'previous_revenue': float(previous_revenue),
            'change_percent': round(change_percent, 1),
            'is_increase': change_percent >= 0,
            'label': f"{'+' if change_percent >= 0 else ''}{round(change_percent, 1)}%"
        }
    
    @staticmethod
    def _get_top_clients(period_months, limit=7):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30 * period_months)
        
        top_clients = Client.objects.filter(
            expedition__date_expedition__gte=start_date
        ).annotate(
            expedition_count=Count('expedition'),
            total_value=Sum('expedition__montant_total')
        ).order_by('-total_value')[:limit]
        
        clients_list = []
        for client in top_clients:
            clients_list.append({
                'name': f"{client.prenom} {client.nom}",
                'company': client.entreprise or "N/A",
                'expedition_count': client.expedition_count,
                'total_value': float(client.total_value or 0)
            })
        
        return clients_list
    
    @staticmethod
    def _get_top_destinations(period_months, limit=10):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30 * period_months)
        
        destinations = Expedition.objects.filter(
            date_expedition__gte=start_date
        ).exclude(
            Q(destination_ville__isnull=True) | Q(destination_ville='')
        ).values('destination_ville').annotate(
            count=Count('id')
        ).order_by('-count')[:limit]
        
        labels = []
        data = []
        for dest in destinations:
            labels.append(dest['destination_ville'])
            data.append(dest['count'])
        
        return {
            'labels': labels,
            'data': data
        }
    
    @staticmethod
    def _get_monthly_expeditions_trend(period_months):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30 * period_months)
        
        monthly_data = Expedition.objects.filter(
            date_expedition__gte=start_date
        ).annotate(
            month=TruncMonth('date_expedition')
        ).values('month').annotate(
            count=Count('id')
        ).order_by('month')
        
        month_names_fr = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 
                         'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc']
        
        counts_dict = {}
        for entry in monthly_data:
            month_key = entry['month'].strftime('%b')
            counts_dict[month_key] = entry['count']
        
        counts = []
        for month in month_names_fr:
            counts.append(counts_dict.get(month, 0))
        
        return {
            'labels': month_names_fr,
            'counts': counts
        }
    
    @staticmethod
    def _calculate_tour_evolution(period_months):
        end_date = timezone.now()
        current_start = end_date - timedelta(days=30 * period_months)
        
        current_count = Tournee.objects.filter(
            date_depart__gte=current_start
        ).count()
        
        previous_start = current_start - timedelta(days=30 * period_months)
        previous_end = current_start
        previous_count = Tournee.objects.filter(
            date_depart__gte=previous_start,
            date_depart__lt=previous_end
        ).count()
        
        if previous_count > 0:
            change_percent = ((current_count - previous_count) / previous_count) * 100
        else:
            change_percent = 0
        
        return {
            'current_count': current_count,
            'previous_count': previous_count,
            'change_percent': round(change_percent, 1),
            'is_increase': change_percent >= 0
        }
    
    @staticmethod
    def _calculate_delivery_success(period_months):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30 * period_months)
        
        stats = Expedition.objects.filter(
            date_expedition__gte=start_date
        ).aggregate(
            total=Count('id'),
            delivered=Count('id', filter=Q(statut='livré')),
            failed=Count('id', filter=Q(statut='échec')),
            delayed=Count('id', filter=Q(statut='retard'))
        )
        
        total = stats['total'] or 1
        delivered = stats['delivered'] or 0
        failed = stats['failed'] or 0
        delayed = stats['delayed'] or 0
        
        success_rate = (delivered / total) * 100 if total > 0 else 0
        
        return {
            'total': total,
            'delivered': delivered,
            'failed': failed,
            'delayed': delayed,
            'success_rate': round(success_rate, 1),
            'percentages': {
                'delivered': round((delivered / total * 100) if total > 0 else 0, 1),
                'failed': round((failed / total * 100) if total > 0 else 0, 1),
                'delayed': round((delayed / total * 100) if total > 0 else 0, 1)
            }
        }
    
    @staticmethod
    def _get_top_drivers(period_months, limit=5):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30 * period_months)
        
        top_drivers = Chauffeur.objects.filter(
            tournee__date_depart__gte=start_date
        ).annotate(
            total_tours=Count('tournee'),
            completed_tours=Count('tournee', filter=Q(tournee__statut='terminé'))
        ).order_by('-completed_tours')[:limit]
        
        drivers_list = []
        for driver in top_drivers:
            completion_rate = (driver.completed_tours / driver.total_tours * 100) if driver.total_tours > 0 else 0
            
            drivers_list.append({
                'name': f"{driver.prenom} {driver.nom}",
                'badge': driver.matricule or f"CH{driver.id:03d}",
                'total_tours': driver.total_tours,
                'completed_tours': driver.completed_tours or 0,
                'completion_rate': round(completion_rate, 1)
            })
        
        return drivers_list
    
    @staticmethod
    def _get_incident_zones(period_months, limit=10):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30 * period_months)
        
        incident_zones = Incident.objects.filter(
            date_incident__gte=start_date
        ).select_related('trajet__expedition').values(
            'trajet__expedition__destination_ville'
        ).annotate(
            count=Count('id')
        ).order_by('-count')[:limit]
        
        labels = []
        data = []
        
        for zone in incident_zones:
            ville = zone['trajet__expedition__destination_ville'] or "Zone Inconnue"
            labels.append(ville)
            data.append(zone['count'])
        
        return {
            'labels': labels,
            'data': data
        }
    
    @staticmethod
    def _get_peak_activity_months(period_months):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30 * period_months)
        
        monthly_tours = Tournee.objects.filter(
            date_depart__gte=start_date
        ).annotate(
            month=TruncMonth('date_depart')
        ).values('month').annotate(
            count=Count('id')
        ).order_by('month')
        
        month_names_fr = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 
                         'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc']
        
        counts_dict = {}
        for entry in monthly_tours:
            month_key = entry['month'].strftime('%b')
            counts_dict[month_key] = entry['count']
        
        counts = []
        for month in month_names_fr:
            counts.append(counts_dict.get(month, 0))
        
        max_val = max(counts) if counts else 1
        
        return {
            'labels': month_names_fr,
            'counts': counts,
            'max_value': max_val
        }
    
    @staticmethod
    def _get_tours_per_month_chart(period_months):
        peak_data = DashboardCalculator._get_peak_activity_months(period_months)
        
        max_val = peak_data['max_value']
        
        scaled_data = []
        for count in peak_data['counts']:
            scaled_value = (count / max_val) * 100
            scaled_data.append(round(scaled_value, 1))
        
        return {
            'labels': peak_data['labels'],
            'data': scaled_data,
            'actual_counts': peak_data['counts'],
            'max_scale': 100
        }


from backend.clients.models import Client
from backend.manageExpedition.models import Expedition, Tournee
from backend.logistics.models import Chauffeur
from backend.incidents.models import Incident