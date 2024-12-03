import os
import dotenv
from supabase import create_client, Client

class SupabaseApi:
    dotenv.load_dotenv()

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    
    def productos(self) -> list:
        response = self.supabase.table("Productos").select("*").execute()
        productos_data=[]
        if len(response.data) > 0:
            productos_data = response.data
        else:
            response.data=["text"]
            
        print(productos_data)
        return productos_data