import reflex as rx
import Negocio.constants as const
from Negocio.Styles.styles import Size, Spacing
from Negocio.Components.title import title
from Negocio.Components.link_sponsor import image_sponsor
from Negocio.Components.ant_components import float_button

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Nuestras marcas"),
        rx.flex(
            image_sponsor(
                "nakata.png",
                "Logotipo de Elgato"
            ),
            image_sponsor(
                "skf.png",
                "Logotipo de Microsoft MVP"
            ),
            image_sponsor(
                "dolz.png",
                "Logotipo de GitHub Star"
            ),
            image_sponsor(
                "dayco.png",
                "Logotipo de GitHub Star"
            ),
            image_sponsor(
                "tiper.png",
                "Logotipo de GitHub Star"
            ),
            spacing=Spacing.BIG.value,
            flex_direction=["column", "row"]
        ),
        float_button(),
        width="100%",
        align_items="start",
        spacing=Spacing.DEFAULT.value
    )
