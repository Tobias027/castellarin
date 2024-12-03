from .TwitchApi import TwitchApi

TWITCH_API=TwitchApi()

async def live(user:str)->bool:
    return TWITCH_API.live(user)