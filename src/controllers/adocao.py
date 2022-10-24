from fastapi.encoders import jsonable_encoder


from src.services.adocao import (
    get_adoption_by_email_and_pet, get_adoption_opened_request, get_adoption_request_by_id, 
    get_adoption_requests_by_email, get_adoption_requests_by_pet, 
    post_adoption_request, update_status_request
)
from src.services.adotante import get_adopter_by_email
from src.services.pet import get_pet_by_name, update_adopted_status_pet
from src.utils.custom_exceptions import NotFoundException, NotInsertedException, NotUpdatedException, RulesException


async def create_adoption_request(request, email, pet_name):
    new_data = await get_adoption_by_email_and_pet(email, pet_name)
    if new_data is not None:
        raise NotInsertedException("Este pedido já estava registrado. Aguarde o contato dos nossos voluntários")

    get_pet_data = await get_pet_by_name(pet_name)
    if not get_pet_data:
        raise NotFoundException("Pet não encontrado no sistema")
    
    if get_pet_data["adotado"] == True:
        raise RulesException("Este pet não está mais para adoção")
    
    get_adopter_data = await get_adopter_by_email(email)
    
    adoption_request = await get_adoption_request_obj(get_pet_data, get_adopter_data, request)
    
    created_adoption = await post_adoption_request(adoption_request)
    if created_adoption:
        return created_adoption
    raise RulesException("Erro ao cadastrar o pedido")


async def get_adoption_request_obj(pet_data, adopter_data, request):
    request = jsonable_encoder(request)
    adoption_request = {
        "pet": pet_data,
        "adotante": adopter_data,
        "dados_pedido": request,
    }
    del adoption_request["pet"]["_id"]
    del adoption_request["pet"]["adotado"]
    del adoption_request["adotante"]["_id"]
    return adoption_request


async def get_all_adoptions_by_email(email, skip, limit):
    try:
        return await get_adoption_requests_by_email(email, skip, limit)
    except Exception:
        raise NotFoundException("Erro na listagem de adotantes do sistema")


async def get_all_adoptions_by_pet(pet_name, skip, limit):
    try:
        return await get_adoption_requests_by_pet(pet_name, skip, limit)
    except Exception:
        raise NotFoundException("Erro na listagem de pets para adoção")
    

async def update_request_status(email, pet_name, status):
    status = jsonable_encoder(status)
    opened_request = await get_adoption_opened_request(email, pet_name)
    if opened_request is None:
        raise NotUpdatedException("Não há pedidos de adoção em aberto para esta consulta")   
    id = opened_request["_id"]["$oid"]
    await update_adopted_status_pet(pet_name, status)
    updated_status = await update_status_request(id, status)
    if updated_status:
        return await get_adoption_request_by_id(id)
    raise RulesException("Erro na atualização do status do pedido de adoção")   
