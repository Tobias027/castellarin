import reflex as rx
import Negocio.utils as utils
import Negocio.Styles.styles as styles
from Negocio.Index_page.index_navbar import navbar
from Negocio.Components.footer import footer
from Negocio.Index_page.index_links import index_links
from Negocio.Index_page.sponsors import sponsors
from Negocio.Styles.styles import Size
from Negocio.Components.sidebar import sidebar


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        sidebar(),
        rx.center(
            rx.vstack(
                index_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )