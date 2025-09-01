import os
import base64
from pathlib import Path
from typing import Union

from anubis_core.ports.cdn_manager import ICdnManagerPort

class LocalCdnManagerAdapter(ICdnManagerPort):

    def __init__(self, absolute_path: str):
        self.absolute_path = absolute_path
        os.makedirs(self.absolute_path, exist_ok=True)

    def check_filename(self, filename: str) -> bool:
        # Verifica que el nombre no tenga caracteres peligrosos
        return all(c.isalnum() or c in ('-', '_', '.', ' ') for c in filename)

    def send_file(self, filename: str, base64_data: str, msg: Union[str, None] = None) -> str:
        # Verifica y convierte el nombre
        filename = self.convert_filename(filename)
        if not self.check_filename(filename):
            raise ValueError("Nombre de archivo inválido.")

        file_path = os.path.join(self.absolute_path, filename)

        # Decodifica y guarda el archivo
        try:
            with open(file_path, 'wb') as f:
                f.write(base64.b64decode(base64_data))
        except Exception as e:
            raise IOError(f"Error al guardar el archivo: {str(e)}")

        if msg:
            print(f"[INFO] {msg}")

        return file_path  # Retorna la ruta completa del archivo guardado

    def convert_filename(self, name: str) -> str:
        # Normaliza el nombre de archivo
        return name.replace(' ', '_').strip()
