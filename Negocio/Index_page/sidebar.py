
import reflex as rx
from Negocio.Styles.colors import Color,TextColor,HeaderText
from Negocio.Styles.styles import Size, Spacing,BASE_STYLE

def sidebar_item(
    text: str, image: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.image(
                src=image,
                width=Size.LARGE.value,
                height=Size.LARGE.value,
                margin=Size.MEDIUM.value,
            ),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": '#d35400',
                    "color": '#F3F8F2',
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Productos", "shock-absorber.png", "/productos"),
        sidebar_item("Quienes somos", "badge-check.png", "/#"),
        sidebar_item("Local Quilmes", "store_white.png", "/#"),
        sidebar_item("Local Bernal", "store_white.png", "/#"),
        spacing="1",
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.box(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="menu.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Menu", size="7", weight="bold"
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                spacing="5",
                position="fixed",
                left="0px",
                top="90px",
                z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                bg="#000000", #value '#F3F8F2'
                align="start",
                height="100%",
                width="16em",
            ),
        )
