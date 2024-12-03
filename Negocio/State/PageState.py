import reflex as rx
from Negocio.API.api import live

USER="K1ng"

class PageState(rx.State):
    is_live:bool
    async def check_live(self):
        self.is_live= await live(USER)