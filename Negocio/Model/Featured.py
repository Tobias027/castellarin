import reflex as rx
from typing import Optional

class Featured(rx.Base):
        Nombre:str = ""
        Descripcion:str = ""
        Categoria:str = ""
        Marca:str = ""
        Modelo:str = ""
        Precio:float = ""
        Cantidad_Disponible:int = ""
        Imagen:str = ""
        Material:str = ""
        Alto: Optional[float] = ""
        Ancho: Optional[float] = ""