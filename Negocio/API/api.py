from .TwitchApi import TwitchApi
from .SupabaseApi import SupabaseAPI
from Negocio.Model.Featured import Featured
TWITCH_API=TwitchApi()
SUPABASE_API=SupabaseAPI()

async def live(user:str)->dict:
    return TWITCH_API.live(user)

async def featured() -> list[Featured]:
    return SUPABASE_API.featured()
