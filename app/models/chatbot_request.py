from pydantic import BaseModel, Field

# BaseModel y Field se utilizan para definir modelos de datos con validaciones automaticas.
# Acepta JSON en el campo que se llama command
# Si el campo no está presente regresa un error
# Si se envía un JSON válido, por ejemplo: 
# {
#   "command": "Añade la cancion Guadalajara al grupo Mariachi Mexcalli"
# }
# Lo convertirá a un objeto de python con el campo y el valor dado.
# Las validaciones son atomaticas gracias la la libreria pydantic

class Request(BaseModel):
    command: str = Field(
        ..., 
        min_length=3, 
        max_length=255, 
        description="Comando del usuario"
    )