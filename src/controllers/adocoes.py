from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


from src.services.adocao import (
    get_adoption_by_email_and_pet, get_adoption_requests_by_email, 
    get_adoption_requests_by_pet, post_adoption_request
)
from src.services.adotante import get_adopter_by_email
from src.services.endereco import get_address_by_adopter_email
from src.services.pets import get_pet_by_name


async def create_adoption_request(request, email, pet_name):
    
    new_data = await get_adoption_by_email_and_pet(email, pet_name)
    if new_data is not None:
        raise HTTPException(status_code=400, detail="Este pedido já estava registrado. Aguarde o contato dos nossos voluntários")

    get_pet_data = await get_pet_by_name(pet_name)
    if not get_pet_data:
        raise HTTPException(status_code=404, detail="Pet não encontrado no sistema")
    if get_pet_data["adotado"] == True:
        raise HTTPException(status_code=400, detail="Este pet não está mais para adoção")
    
    get_adopter_address = await get_address_by_adopter_email(email)
    if not get_adopter_address:
        raise HTTPException(status_code=404, detail="Adotante não tem endereço cadastrado. Cadastre um endereço primeiro")
    
    get_adopter_data = await get_adopter_by_email(email)
    
    adoption_request = await get_adoption_request_obj(get_pet_data, get_adopter_address,
                                                      get_adopter_data, request)
    
    created_adoption = await post_adoption_request(adoption_request)
    if created_adoption:
        return created_adoption
    raise HTTPException(status_code=400, detail="Erro ao cadastrar o pedido")


async def get_adoption_request_obj(pet_data, adopter_address, adopter_data, request):
    request = jsonable_encoder(request)
    adoption_request = {
        "pet": pet_data,
        "adotante": adopter_data,
        "endereco": adopter_address,
        "dados_pedido": request,
    }
    return adoption_request


async def get_all_adoptions_by_email(email, skip, limit):
    try:
        return await get_adoption_requests_by_email(email, skip, limit)
    except Exception:
        raise HTTPException(status_code=404, detail="Erro na listagem de adotantes do sistema")


async def get_all_adoptions_by_pet(pet_name, skip, limit):
    try:
        return await get_adoption_requests_by_pet(pet_name, skip, limit)
    except Exception:
        raise HTTPException(status_code=404, detail="Erro na listagem de pets para adoção")
