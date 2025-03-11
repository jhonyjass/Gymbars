import os
from app import app

# Para que arranque servidor
if __name__ == '__main__':
    # Obtiene el puerto de la variable de entorno o usa 3000 como valor predeterminado
    port = int(os.environ.get('PORT', 5000))
    # Se mantiene en escucha en 0.0.0.0 para aceptar conexiones externas
    app.run(host="0.0.0.0", port=port, debug=True)