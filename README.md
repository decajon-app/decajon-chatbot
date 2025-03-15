# decajon-chatbot
Este programa es el asistente virtual a la aplicación Decajón. Aquí se procesan las solicitudes que se hacen desde el cliente (frontend, react native), las recibe el backend y se envían hasta aquí. Se procesa la solicitud y se regresa al backend el comando que se debe ejecutar.

A continuacion se detallan las instrucciones para correr el programa.

## Pre-requisitos
1. Python 3.10+
2. pip 25.0.1+

## Instrucciones para correr el programa

Siga estos pasos para correr el chatbot.

### Crear un entorno virtual

Activar un entorno virtual nos servirá para instalar paquetes que solo estarán disponibles en ese entorno sin afectar la instalación global de python.
    
- Windows PowerShell
    
`python -m venv nombre_del_entorno`

### Activar el entorno virtual

- Windows PowerShell

`.\nombre_del_entorno\Scripts\Activate.ps1`

Si el entorno está activo vas a ver el nombre de tu entorno entre paréntesis al comienzo la linea de comandos.

Ejemplo:

`(decajon_env) PS C:\Users\Edgar\Documents\decajon-chatbot>`

### Instalar las dependencias

Situado en la raíz del proyecto ejecutar:

`pip install -r requirements.txt`

### Ejecutar el programa

Ejecutar el programa con el comando:

`uvicorn main:app --reload`

La flag --reload es opcional y es para propósitos de desarrollo.

### Eliminar un entorno virtual

Si deseas eliminar el entorno virutal se deben seguir los siguientes pasos.

1. Desactivar el entorno

`deactivate`

2. Eliminar la carpeta

- Windows PowerShell

`Remove-Item -Recurse -Force nombre_del_entorno`

### Posibles errores

Si se presenta un error de ejecucion de permisos, es necesario cambiar la política de ejecución.

- Windows PowerShell

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`