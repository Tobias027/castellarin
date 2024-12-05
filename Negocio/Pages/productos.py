import reflex as rx
import Negocio.utils as utils
import Negocio.Styles.styles as styles
from Negocio.productos_page.productos_navbar import navbar
from Negocio.Components.footer import footer
from Negocio.Components.title import title
from Negocio.State.PageState import PageState
from Negocio.Styles.styles import Size
from Negocio.productos_page.productos_posts import index_links

@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
    on_load=[PageState.check_live, PageState.featured_links]
)
def productos() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(live=PageState.is_live, title=PageState.title),
        rx.center(
            rx.vstack(
                title("Nuestros productos"),
                index_links(),
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                align ="center",
                justify="center"
            ),
        ),
        footer()
    )
