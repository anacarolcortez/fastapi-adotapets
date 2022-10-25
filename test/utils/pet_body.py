from datetime import datetime

def create_valid_pet():
    return {
        "nome": "teste dog",
        "data_nasc": "2020-09-15",
        "data_cadastro": f"{datetime.now()}",
        "sexo": "f",
        "raca": "srd",
        "porte": "medio",
        "cor": "caramelo e branco",
        "tipo": "cachorro",
        "pcd": False,
        "foto": "imgur.com/testeteste.jpg",
        "obs": "brincalhona e sociável; foi resgatada grávida e teve três fihotes: drogo, viserion e rhaegal",
        "adotado": False
    }
