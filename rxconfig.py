import reflex as rx

config = rx.Config(
    app_name="Negocio",
    api_url="https://castellarinautorepuestos.up.railway.app/",
    cors_allowed_origins=[
        "https://castellarinautorepuestos.vercel.app/"
    ]
)
