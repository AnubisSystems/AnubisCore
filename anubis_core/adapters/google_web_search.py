import time
import requests
from typing import List, Dict, Optional
from urllib.parse import quote

from anubis_core.ports.web import IWebSearchPort

class GoogleCustomSearchAdapter(IWebSearchPort):
    def __init__(self, api_key: str, id_search=None):
        self.api_key = api_key
        self.id_search = id_search
        self.base_url = "https://www.googleapis.com/customsearch/v1"

    def search(
        self, 
        text: str, 
        rows: int = 10, 
        page: int = 1, 
        id_search: Optional[str] = None, 
        image: bool = False
    ) -> List[str]:
        """
        Busca en Google Custom Search.
        
        Args:
            text: Término de búsqueda.
            rows: Resultados por página (max 10 por limitación de la API).
            page: Número de página (comienza en 1).
            id_search: ID del motor de búsqueda. Si no se proporciona, usa filtros por defecto.
            image: Si True, devuelve {'url': str, 'image': str}.
        
        Returns:
            Lista de URLs o diccionarios con URL + imagen.
        """
        start = (page - 1) * rows + 1
        
        # Construir la query (con/sin exclusiones según id_search)
        query = text
        if not id_search:
            query = f"{text} site:leroymerlin.es/productos/ -site:leroymerlin.es/productos/*/*"
        
        params = {
            "q": query,
            "key": self.api_key,
            "cx": id_search if id_search else "TU_DEFAULT_SEARCH_ENGINE_ID",  # Opcional: valor por defecto
            "num": min(rows, 10),  # La API solo permite max 10 resultados/llamada
            "start": start,
        }

        if image:
            params["searchType"] = "image"

        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data.get("items", []):
            if image:
                results.append({
                    "url": item.get("link", ""),
                    "image": item.get("image", {}).get("thumbnailLink", "")
                })
            else:
                results.append(item.get("link", ""))
        
        time.sleep(2)
        return results