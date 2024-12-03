from .TwitchApi import TwitchApi
from .SupabaseApi import SupabaseApi

TWITCH_API=TwitchApi()
SUPABASE_API=SupabaseApi()

async def live(user:str)->dict:
    return TWITCH_API.live(user)

async def ProductosAPI()->dict:
    return SUPABASE_API.productos()