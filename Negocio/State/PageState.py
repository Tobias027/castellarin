import reflex as rx
from Negocio.API.api import live
from Negocio.API.api import ProductosAPI

USER="martinciriook"

class PageState(rx.State):
    is_live:bool
    title:str
    Productos:list
    async def check_live(self):
        data= await live(USER)
        self.is_live= data["bool"]
        self.title= data["title"]
        
    async def Productos_links(self):
        self.Productos= await ProductosAPI()