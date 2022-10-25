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


def create_invalid_adopted_pet():
    return {
        "nome": "au au",
        "data_nasc": "2020-09-15",
        "data_cadastro": f"{datetime.now()}",
        "sexo": "m",
        "raca": "srd",
        "porte": "pequeno",
        "cor": "preto",
        "tipo": "cachorro",
        "pcd": False,
        "foto": "imgur.com/auaudog.jpg",
        "obs": "brincalhão e sociável",
        "adotado": True
    }


def create_invalid_pet_type():
    return {
        "nome": "au au",
        "data_nasc": "2020-09-15",
        "data_cadastro": f"{datetime.now()}",
        "sexo": "m",
        "raca": "srd",
        "porte": "pequeno",
        "cor": "preto",
        "tipo": "passarinho",
        "pcd": False,
        "foto": "imgur.com/auaudog.jpg",
        "obs": "brincalhão e sociável",
        "adotado": True
    }


def create_invalid_pet_size():
    return {
        "nome": "au au",
        "data_nasc": "2020-09-15",
        "data_cadastro": f"{datetime.now()}",
        "sexo": "m",
        "raca": "srd",
        "porte": "imenso",
        "cor": "preto",
        "tipo": "cachorro",
        "pcd": False,
        "foto": "imgur.com/auaudog.jpg",
        "obs": "brincalhão e sociável",
        "adotado": True
    }


def update_pet_data():
    return {
        "pcd": True,
        "foto": "imgur.com/newpic_update.jpg",
        "obs": "está pedendo aos poucos a visão"
    }
