import reflex as rx
import datetime
import Negocio.constants as const
from Negocio.Styles.styles import Size, Spacing
from Negocio.Styles.colors import Color, TextColor
# from Negocio.components.ant_components import float_button


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Castellarin Autorepuestos."
        ),
        #rx.link(
            rx.box(
                f"© 1961-{datetime.date.today().year} ",
                rx.text(
                    "",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                "",
                padding_top=Size.DEFAULT.value
            ),
        #    href=const.MOUREDEV_URL,
        #    is_external=True,
        #    font_size=Size.MEDIUM.value
        #),
        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value
    )
