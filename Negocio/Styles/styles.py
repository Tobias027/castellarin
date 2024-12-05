import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "560px"
FADEIN_ANIMATION = "animate__animated animate__fadeIn"
BOUNCEIN_ANIMATION = "animate__animated animate__bounceIn"

# Sizes

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://fonts.googleapis.com/css2?family=Montserrat:wght@600&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
]


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    SEMI_LARGE = "1.2em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

# Styles


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
        "_hover": {
                "backgroundColor": Color.BUTTON.value,
        }
    },    
    rx.link: {
        "color": TextColor.BODY.value,
        "text_decoration": "none",
        "_hover": {}
    }
}

container_style=dict(
        width= "100%",
        height= "100%",
        padding= Size.SMALL.value,
        border_radius= Size.DEFAULT.value,
        color= TextColor.HEADER.value,
        background_color= Color.CONTENT.value,
        white_space= "normal",
        text_align= "start",
        position= "relative",  # El contenedor debe ser relativo para que el botón se ancle a él
)


navbar_title_style = dict(
    font_family=Font.NEW.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value,
    align_items="baseline",  # Centra verticalmente los elementos
    gap="0",               # Elimina el espacio entre los elementos
    margin="0",            # Asegúrate de que no haya márgenes adicionales
    padding="0"            # Asegúrate de que no haya relleno adicional
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value
)

products_title_style= dict(
    width="100%",
    padding_top=Size.SMALL.value,
    font_size=Size.SEMI_LARGE.value,
)

Products_image_style = dict(
    display="flex",
    justify_content="center",
    align_items="center",
)

button_Products_style = dict(
    font_weight=FontWeight.LIGHT.value,
    color=TextColor.BODY.value,
    background_color=Color.BACKGROUND.value,
    bottom="0",  # Pegarlo al borde inferior
    width="100%",  # Tamaño responsivo
    _hover={"backgroundColor": "#262626"},
)


button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    color=TextColor.BODY.value
)
