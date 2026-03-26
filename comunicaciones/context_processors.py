from .models import Comunicado


def comunicados_pendientes(request):
    if request.user.is_authenticated:
        count = Comunicado.objects.filter(activo=True).count()
        urgentes = Comunicado.objects.filter(activo=True, tipo='UR').count()
        return {
            'notif_count': count,
            'notif_urgentes': urgentes,
        }
    return {'notif_count': 0, 'notif_urgentes': 0}