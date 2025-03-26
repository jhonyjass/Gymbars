from flask import session, request, render_template


def verificar_sesion():
    rutas_no_protegidas = ['sesion_usuario_bp.iniciar_sesion', 'pagina_no_encontrada']

    # Excluir las rutas de archivos estaticos
    if request.endpoint and 'static' in request.endpoint:
        return None 
    
    # Verificar si usuario no esta en sesion
    if 'usuario' not in session and request.endpoint not in rutas_no_protegidas:
        return render_template('alertas/404.html', error_404=True), 404 



def pagina_no_encontrada(e):
    return render_template('alertas/404.html',error_404=True),404
