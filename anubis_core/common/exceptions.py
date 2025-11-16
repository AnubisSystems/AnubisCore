#  ENUMERACIONES CON PLANTILLA

from enum import Enum
class EnumExceptionsTemplate(Enum):
    def __init__(self, codigo, plantilla):
        self.codigo = codigo
        self.plantilla = plantilla

    def mensaje(self, **kwargs):
        return self.plantilla.format(**kwargs)



class AnubisException(Exception):
    def __init__(self, tipo_excepcion: type, codigo_error: object, contexto: dict = None, original: Exception = None):
        self.tipo_excepcion = tipo_excepcion
        self.codigo_error = codigo_error
        self.contexto = contexto or {}
        self.original = original
        mensaje = self.codigo_error.mensaje(**self.contexto)
        super().__init__(mensaje)

class ErrorDominio(EnumExceptionsTemplate):
    VALIDACION_NEGOCIO = ("validacion_negocio", "La entidad {entidad} tiene datos inválidos: {detalle}")
    INVARIANTE_VIOLADA = ("invariante_violada", "Se ha violado una regla de negocio: {regla}")
    ENTIDAD_NO_ENCONTRADA = ("entidad_no_encontrada", "No se encontró la entidad {entidad} con ID {id}")

class AnubisDomainException(AnubisException):
    def __init__(self , tipo_excepcion: type, codigo_error, contexto=None, original=None):
        super().__init__(tipo_excepcion, codigo_error, contexto, original)

# ESTAS DOS CLASES NO HARIAN FALTA. A NO SER QUE SEA PARA ORGANIZACION DEL CODIGO
# SI QUE HACEN FALTA. PARA PODER INTERCEPTARLAS EN LOS ADAPTADORES DE ENTRADA.
class AnubisBaseAplicationException(AnubisException):
    def __init__(self , tipo_excepcion: type, codigo_error, contexto=None, original=None):
        super().__init__(tipo_excepcion, codigo_error, contexto, original)

class AnubisBaseAdapterException(AnubisException):
    def __init__(self , tipo_excepcion: type, codigo_error, contexto=None, original=None):
        super().__init__(tipo_excepcion, codigo_error, contexto, original)


