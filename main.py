from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from router.router import router


app = FastAPI()
app.include_router(router)
app.title = "Productos para gatos"
app.version = "Vero's 1"

@app.get("/", tags=['home'])
def message():
    return HTMLResponse(content= "<h1> Bienvenido a la tienda </h1>")

