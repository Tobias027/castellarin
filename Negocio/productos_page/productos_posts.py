import reflex as rx
from Negocio.State.PageState import PageState
import Negocio.Styles.styles as Styles
from Negocio.Model.Featured import Featured

def ProductCard(featured: Featured):
    return rx.container(
        rx.heading(featured["Nombre"], style=Styles.products_title_style),
        rx.box(
            rx.image(src=featured["Imagen"], width="200px"),
            style=Styles.Products_image_style,
        ),
        rx.box(
            rx.button(
                "Agregar al carrito.",
                style=Styles.button_Products_style,
            ),
        ),
        style=Styles.container_style,
        bg=Styles.Color.PRIMARY.value,
        border=f"{'2.3px' if Styles.Color.SECONDARY.value != None else '0px'} solid {Styles.Color.SECONDARY.value}",
    )


def index_links() -> rx.Component:
    return rx.vstack(
        rx.cond(
            PageState.featured_info,
            rx.section(
                rx.grid(
                    rx.foreach(
                        PageState.featured_info,
                        ProductCard
                    ),
                    spacing=Styles.Spacing.DEFAULT.value,
                    columns="3"
                ),
                spacing=Styles.Spacing.DEFAULT.value
            )
        ),

    spacing=Styles.Spacing.DEFAULT.value,
    on_mount=PageState.featured_links
    )