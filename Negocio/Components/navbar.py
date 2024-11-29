import reflex as rx
import Negocio.Styles.styles as styles
from Negocio.routes import Route
from Negocio.Styles.styles import Size
from Negocio.Styles.colors import Color, HeaderText


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("moure", as_="span", color=HeaderText.First_word.value),
                rx.text("dev", as_="span", color=HeaderText.Second_word.value),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
