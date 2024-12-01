import reflex as rx
import reflex.components.radix.themes.components as rdxt
import Negocio.Styles.styles as Styles
from Negocio.Styles.styles import Size, Spacing


def link_button(title: str,
                body: str,
                image: str,
                url: str,
                is_external=True,
                highlight_color=None,
                animated=False) -> rx.Component:

    return rx.button(
        rx.hstack(
            rx.image(
                src=image,
                width=Size.LARGE.value,
                height=Size.LARGE.value,
                margin=Size.MEDIUM.value,
                alt=title
            ),
            rx.vstack(
                rx.text(
                    title,
                    size=Spacing.SMALL.value,
                    style=Styles.button_title_style,
                    class_name="hover-text"
                ),
                rx.text(
                    body,
                    size=Spacing.VERY_SMALL.value,
                    style=Styles.button_body_style,
                    class_name="hover-text"
                ),
                align_items="start",
                spacing=Spacing.VERY_SMALL.value,
                padding_y=Size.SMALL.value,
                padding_right=Size.SMALL.value
            ),
            align="center",
            width="100%"
        ),
        border=f"{'2.3px' if highlight_color != None else '0px'} solid {highlight_color}",
        class_name=Styles.BOUNCEIN_ANIMATION if animated else None,
        on_click=rx.redirect(path=url, external=is_external)
    )
