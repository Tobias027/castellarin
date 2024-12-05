import os
import dotenv
from supabase import create_client, Client
from Negocio.Model.Featured import Featured


class SupabaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )

    def featured(self) -> list[Featured]:

        response = self.supabase.table(
            "Productos").select("*").execute()

        featured_data = []

        if len(response.data) > 0:
            for featured_item in response.data:
                featured_data.append(
                    Featured(
                        Nombre=featured_item["Nombre"],
                        Descripcion=featured_item["Descripcion"],
                        Categoria=featured_item["Categoria"],
                        Marca=featured_item["Marca"],
                        Modelo=featured_item["Modelo"],
                        Precio=featured_item["Precio"],
                        Cantidad_Disponible=featured_item["Cantidad Disponible"],
                        Imagen=featured_item["Imagen"],
                        Material=featured_item["Material"],
                        Alto=featured_item["Alto"],
                        Ancho=featured_item["Ancho"]
                    )
                )
        return featured_data