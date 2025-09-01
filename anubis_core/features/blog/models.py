from pydantic import BaseModel
from typing import List, Optional

class CorePost(BaseModel):
    
    id: Optional[int] = None
    """_summary_
    """

    language: Optional[str] = None
    """_summary_
    """

    images_base64 : Optional[list[str]] = []                
    """imagenes en base 64. La primera es la portada
    """

    title: Optional[str] = None
    """Titulo del post
    """

    summary: Optional[str] = None
    """Resumen del post
    """

    content: Optional[str] = None
    """Contenido del  post
    """

    status: Optional[str] = None
    """Contenido del  post
    """

    url: Optional[str] = None
    """url del  post
    """


    created_date: Optional[str]= None
    """Fecha de creaccion
    """

    publish_date: Optional[str]= None
    """Fecha de publicacion
    """

    update_date : Optional[str]= None
    """Fecha de actualizacion
    """

    """CLASIFICACION
    """
    categories : Optional[list[str]] = []
    """CATEGORIAS
    """
    tags : Optional[list[str]] = []
    """TAGS DEL PRODUCTOS
    """