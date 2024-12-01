import reflex as rx
from Negocio.Styles.styles import Size


def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height="3.5em",
            aspect_ratio="5 / 2",
            alt=alt
        ),
        href=url,
        is_external=True
    )

def image_sponsor(imagen: str, alt: str) -> rx.Component:
    return rx.box(
        rx.image(
            src=imagen,
            height="3.5em",
            aspect_ratio="5 / 2",
            alt=alt
        ),
        is_external=True
    )