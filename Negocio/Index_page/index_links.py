import reflex as rx
import Negocio.constants as const
from Negocio.Components.newsletter import newsletter
from Negocio.routes import Route
from Negocio.Components.link_button import link_button
from Negocio.Components.title import title
from Negocio.Styles.styles import Color, Spacing
"""from Negocio.state.PageState import PageState
"""

def index_links() -> rx.Component:
    return rx.vstack(
        title("Conctatos"),
        link_button(
            "Telefono Quilmes",
            "4253-6956",
            "phone.png",
            "/",
            False,
            Color.SECONDARY.value,
            False
        ),
        link_button(
            "Telefono Bernal",
            "4253-6956",
            "phone.png",
            "/",
            False,
            Color.SECONDARY.value
        ),
        link_button(
            "Facebook",
            "Seguinos en facebook y mira nuestras publicaciones",
            "facebook.png",
            const.FACEBOOK,
            False,
            Color.SECONDARY.value,
            False
        ),
        link_button(
            "Marketplace",
            "Seguinos en Marketplace y mira todos los productos que tenemos publicados",
            "shopping-bag.png",
            const.MARKETPLACE,
            False,
            Color.SECONDARY.value,
            False
        ),
        title("Ubicacion"),
        link_button(
            "Local Quilmes",
            "Horarios: Lunes a Viernes 8:30 AM–12 PM / 2:30–5:30 PM. Sabados: 8:30 AM–12 PM",
            "store.png",
            const.MAPS_QUILMES,
            False,
            Color.SECONDARY.value,
            False
        ),
        link_button(
            "Local Bernal",
            "Horarios: Lunes a Viernes 8 AM–12 PM / 2:30–6 PM.",
            "store.png",
            const.MAPS_BERNAL,
            False,
            Color.SECONDARY.value,
            False
        ),

        title("Productos"),
        newsletter(),
        width="100%",
        spacing=Spacing.DEFAULT.value
    )
