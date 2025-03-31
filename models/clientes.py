from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, Integer, String, Boolean, Date, Float, DateTime, Numeric
from conexion import conexion


class objetivos(conexion.Model):
    __tablename__ = "objetivos"

    id_objetivo = conexion.Column(Integer, primary_key=True)
    nombre_objetivo = conexion.Column(String(length=30))

    def __init__(self, nombre_objetivo):
        self.nombre_objetivo = nombre_objetivo


class clientes(conexion.Model):
    __tablename__ = 'clientes'

    id_cliente = conexion.Column(Integer, primary_key=True)
    nombre = conexion.Column(String(length=60))
    dpi = conexion.Column(Numeric(13, 0))
    fecha_nacimiento = conexion.Column(Date)
    edad = conexion.Column(Integer)
    sexo = conexion.Column(String(length=10))
    grupo_sanguineo = conexion.Column(String(length=25))
    correo = conexion.Column(String(length=60))
    fecha_inscripcion = conexion.Column(Date)
    id_objetivo = conexion.Column(Integer, ForeignKey('objetivos.id_objetivo'))

    objetivo_cliente = relationship('objetivos', backref=backref('clientes', cascade='all, delete-orphan'))

    def __init__(self, nombre, dpi, fecha_nacimiento, edad, sexo, grupo_sanguineo,
                 correo, fecha_inscripcion, id_objetivo):
        
        self.nombre = nombre
        self.dpi = dpi
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.sexo = sexo
        self.grupo_sanguineo = grupo_sanguineo
        self.correo = correo
        self.fecha_inscripcion = fecha_inscripcion
        self.id_objetivo = id_objetivo



class telefonos(conexion.Model):
    __tablename__ = 'telefonos'

    id_telefono = conexion.Column(Integer, primary_key=True)
    id_cliente = conexion.Column(Integer, ForeignKey('clientes.id_cliente'))
    telefono = conexion.Column(Integer)
    tipo_telefono = conexion.Column(String(length=15))

    cliente_tel = relationship('clientes', backref=backref('telefonos', cascade='all, delete-orphan'))

    def __init__(self, id_cliente, telefono, tipo_telefono):
        self.id_cliente = id_cliente
        self.telefono = telefono
        self.tipo_telefono = tipo_telefono


class direcciones(conexion.Model):
    __tablename__ = "direcciones"

    id_direccion = conexion.Column(Integer, primary_key=True)
    id_cliente = conexion.Column(Integer, ForeignKey('clientes.id_cliente'))
    direccion = conexion.Column(String(length=100))

    direccion_clie = relationship('clientes', backref=backref('direcciones', cascade='all, delete-orphan'))
    
    def __init__(self, id_cliente, direccion):
        self.id_cliente = id_cliente
        self.direccion = direccion


class afecciones(conexion.Model):
    __tablename__ = "afecciones"

    id_afeccion = conexion.Column(Integer, primary_key=True)
    id_cliente = conexion.Column(Integer, ForeignKey('clientes.id_cliente'))
    hipertension_arterial = conexion.Column(Boolean)
    diabetes = conexion.Column(Boolean)
    afecciones_alergicas = conexion.Column(Boolean)
    afecciones_respiratorias = conexion.Column(Boolean)
    afecciones_cardiovasculares = conexion.Column(Boolean)
    afecciones_osteoarticulares = conexion.Column(Boolean)
    fuma = conexion.Column(Boolean)
    consume_alcohol = conexion.Column(Boolean)

    afecciones_clie = relationship('clientes', backref=backref('afecciones', cascade='all, delete-orphan'))

    def __init__(self, id_cliente, hipertension_arterial, diabetes, afecciones_alergicas, afecciones_respiratorias,
                 afecciones_cardiovasculares, afecciones_osteoarticulares, fuma, consume_alcohol):
        
        self.id_cliente = id_cliente
        self.hipertension_arterial = hipertension_arterial
        self.diabetes = diabetes
        self.afecciones_alergicas = afecciones_alergicas
        self.afecciones_respiratorias = afecciones_respiratorias
        self.afecciones_cardiovasculares = afecciones_cardiovasculares
        self.afecciones_osteoarticulares = afecciones_osteoarticulares
        self.fuma = fuma
        self.consume_alcohol = consume_alcohol


class medidas(conexion.Model):
    __tablename__ = "medidas"

    id_medidas = conexion.Column(Integer, primary_key=True)
    id_cliente = conexion.Column(Integer, ForeignKey("clientes.id_cliente"))
    fecha_hora = conexion.Column(DateTime)
    cuello = conexion.Column(Float)
    pecho = conexion.Column(Float)
    brazo_derecho = conexion.Column(Float)
    brazo_izquierdo = conexion.Column(Float)
    antebrazo_derecho = conexion.Column(Float)
    antebrazo_izquierdo = conexion.Column(Float)
    cintura = conexion.Column(Float)
    cadera = conexion.Column(Float)
    muslo_derecho = conexion.Column(Float)
    muslo_izquierdo = conexion.Column(Float)
    pantorilla_derecha = conexion.Column(Float)
    pantorilla_izquierda = conexion.Column(Float)
    muñeca_derecha = conexion.Column(Float)
    muñeca_izquierda = conexion.Column(Float)
    tobillo_derecho = conexion.Column(Float)
    tobillo_izquierdo = conexion.Column(Float)
    peso_corporal = conexion.Column(Float)

    medidas_clie = relationship('clientes', backref=backref('medidas', cascade='all, delete-orphan'))

    def __init__(self, id_cliente, fecha_hora, cuello, pecho, brazo_derecho, brazo_izquierdo,
                 antebrazo_derecho, antebrazo_izquierdo, cintura, cadera, muslo_derecho,
                 muslo_izquierdo, pantorilla_derecha, pantorilla_izquierda, muñeca_derecha,
                 muñeca_izquierda, tobillo_derecho, tobillo_izquierdo, peso_corporal):
        
        self.id_cliente = id_cliente
        self.fecha_hora = fecha_hora
        self.cuello = cuello
        self.pecho = pecho
        self.brazo_derecho = brazo_derecho
        self.brazo_izquierdo = brazo_izquierdo
        self.antebrazo_derecho = antebrazo_derecho
        self.antebrazo_izquierdo = antebrazo_izquierdo
        self.cintura = cintura
        self.cadera = cadera
        self.muslo_derecho = muslo_derecho
        self.muslo_izquierdo = muslo_izquierdo
        self.pantorilla_derecha = pantorilla_derecha
        self.pantorilla_izquierda = pantorilla_izquierda
        self.muñeca_derecha = muñeca_derecha
        self.muñeca_izquierda = muñeca_izquierda
        self.tobillo_derecho = tobillo_derecho
        self.tobillo_izquierdo = tobillo_izquierdo
        self.peso_corporal = peso_corporal

