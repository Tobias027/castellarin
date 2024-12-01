import reflex as rx
from Negocio.Pages.index import index
from Negocio.Styles import styles

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index)
