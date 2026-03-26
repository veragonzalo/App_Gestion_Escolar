def perfil_usuario(request):
    """Expone el perfil del usuario autenticado a todos los templates."""
    if request.user.is_authenticated:
        try:
            return {'perfil': request.user.perfil}
        except Exception:
            pass
    return {'perfil': None}