import uvicorn
from fastapi import FastAPI

from src.routes import home, pets, adotante

desc = """
APIs para sistema de adoção de pets, com autenticação de usuário administrador. 
\nMicrosserviços em Python, FastAPI, MongoDB, Motor Asyncio e Uvicorn.
\nAna Cortez * https://github.com/anacarolcortez
"""

app = FastAPI(title="Adota Pets", 
              version="1.0",
              description=desc)


app.include_router(home.router)
app.include_router(pets.router)
app.include_router(adotante.router)


# if __name__ == '__main__':
#     uvicorn.run("main:app", port=8000, reload=True, access_log=False)