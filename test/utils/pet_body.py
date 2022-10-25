from datetime import datetime


def create_valid_pet():
    return {
        "nome": "miau miau",
        "data_nasc": "2020-09-15",
        "data_cadastro": f"{datetime.now()}",
        "sexo": "f",
        "raca": "srd",
        "porte": "pequeno",
        "cor": "caramelo e branco",
        "tipo": "gato",
        "pcd": False,
        "foto": "imgur.com/miaumiaucat.jpg",
        "obs": "brincalhona e sociável",
        "adotado": False
    }
