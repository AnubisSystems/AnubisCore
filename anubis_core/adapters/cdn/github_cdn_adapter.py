import requests
from anubis_core.ports.cdn_manager import ICdnManagerPort
import re
import unidecode

class GithubCdnManagerAdapter(ICdnManagerPort):

    def __init__(self, user: str, repo: str, path: str, token: str):
        self.url_cdn = f"https://{user}.github.io/{repo}/{path}"
        self.url = f"https://api.github.com/repos/{user}/{repo}/contents/docs/{path}"        
        self.headers = {"Authorization": f"token {token}"}

    def check_filename(self,  filename):
        if requests.get(f"{self.url_cdn}/{filename}",headers=self.headers).status_code == 404:
            return True
        else:
            return False

    def send_file(self, filename, base64, msg):

        data = {
            "message": msg,
            "content": base64
        }
        url_up = f"{self.url}/{filename}"
        url_down = f"{self.url_cdn}/{filename}"

        if self.check_filename(filename):

        # Enviar solicitud
            response = requests.put(url_up, json=data, headers=self.headers)

        # Verificar respuesta
            if response.status_code == 201:
                return url_down
            else:
                print("❌ Error:", response.json())
        else:
            return url_down

    def convert_filename(self, name):
        # Quitar acentos y caracteres especiales
        titulo = unidecode.unidecode(name)
        # Reemplazar caracteres no permitidos por un guion bajo
        titulo = re.sub(r'[^\w\s-]', '', titulo)
        # Reemplazar espacios por guiones bajos
        titulo = re.sub(r'\s+', '_', titulo)
        # Convertir a minúsculas
        return titulo.lower()