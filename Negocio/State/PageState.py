import reflex as rx
from reflex import State
from Negocio.API.api import live
from Negocio.API.api import featured
from typing import List
from Negocio.Model.Featured import Featured

USER="martinciriook"

class PageState(State):
    is_live:bool
    title:str
    featured_info: List[Featured] = []
    
    async def check_live(self):
        data= await live(USER)
        self.is_live= data["bool"]
        self.title= data["title"]
        
    async def featured_links(self):
        self.featured_info = await featured()
