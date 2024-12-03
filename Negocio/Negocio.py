import reflex as rx
from Negocio.Pages.index import index
from Negocio.Styles import styles
from Negocio.API.api import live

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index)
app.api.add_api_route("/live/{user}",live)