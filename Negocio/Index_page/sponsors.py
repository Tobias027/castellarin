import reflex as rx
import Negocio.constants as const
from Negocio.Styles.styles import Size, Spacing
from Negocio.Components.title import title
from Negocio.Components.link_sponsor import link_sponsor
from Negocio.Components.ant_components import float_button

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Nuestras marcas"),
        rx.flex(
            link_sponsor(
                "nakata.png",
                const.ELGATO_URL,
                "Logotipo de Elgato"
            ),
            link_sponsor(
                "skf.png",
                const.MVP_URL,
                "Logotipo de Microsoft MVP"
            ),
            link_sponsor(
                "dolz.png",
                const.GITHUB_STAR_URL,
                "Logotipo de GitHub Star"
            ),
            link_sponsor(
                "dayco.png",
                const.GITHUB_STAR_URL,
                "Logotipo de GitHub Star"
            ),
            link_sponsor(
                "tiper.png",
                const.GITHUB_STAR_URL,
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
