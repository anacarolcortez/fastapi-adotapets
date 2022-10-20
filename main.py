import uvicorn
from fastapi import FastAPI
from src.routes import pet, adotante, adocao, usuario


desc = """
Microsserviços em Python, FastAPI, MongoDB, Motor Asyncio e Uvicorn.
\nReadme: https://github.com/anacarolcortez/fastapi-adotapets
"""

app = FastAPI(title="Adota Pets", 
              version="1.0",
              description=desc)


app.include_router(usuario.router)
app.include_router(pet.router)
app.include_router(adotante.router)
app.include_router(adocao.router)




# Descomente para rodar o código no localhost
if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True, access_log=False)