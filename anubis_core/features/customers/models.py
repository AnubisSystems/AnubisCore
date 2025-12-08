# MODELOS DE PRODUCTO
from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class CustomerAdressTypes(Enum):
    MAIN = 1
    INVOICE = 2
    SHIPPING = 3
    CONTACT = 4

class CoreCustomerAddress(BaseModel):
    id: Optional[int] = None    
    tipo_direccion: Optional[CustomerAdressTypes] = CustomerAdressTypes.MAIN
    nombre: str = None
    direccion_1: Optional[str] = None
    direccion_2: Optional[str] = None
    cp: Optional[str] = None
    localidad: Optional[str] = None
    provincia: Optional[str] = None
    pais: Optional[str] = None
    telefono: Optional[str] = None

class CoreCustomersLoyalty(BaseModel):
    id: Optional[int] = None    
    programa: Optional[str] = None    
    puntos: Optional[int] = None    

class CoreCustomerHistoryInvoice(BaseModel):
    id: Optional[int] = None    

class CoreCustomerInvoiceLines(BaseModel):
    id : Optional[int] = None    
    producto_id: Optional[int] = None
    nombre_articulo: Optional[str] = None    
    cantidad: Optional[int] = None
    precio_unitario : Optional[float] = None
    subtotal: Optional[float] = None
    impuesto_id: Optional[int] = None  

class CoreCustomerInvoice(BaseModel):
    id: Optional[int] = None  
    nombre: Optional[str] = None    
    fecha: Optional[datetime] = None    
    referencia_pago: Optional[str] = None    
    lineas: List[CoreCustomerInvoiceLines] = []
    cantidad_sin_impuestos: Optional[float] = None
    cantidad_total: Optional[float] = None


class CoreCustomer(BaseModel):
        
    id : Optional[int] = None
    
    email: str = None

    nif: Optional[str] = None

    nombre: str = None

    apellido_1: str = None
    
    apellido_2: Optional[str] = None

    genero: Optional[int] = None 

    fecha_nacimiento: Optional[datetime] = None

    direcciones: Optional[List[CoreCustomerAddress]] = []

    puntos_fidelidad: Optional[List[CoreCustomersLoyalty]] = []

    facturas: Optional[List[CoreCustomerInvoice]] = []

    sitio_web_id:  Optional[int] = None

    boletin: bool = False
