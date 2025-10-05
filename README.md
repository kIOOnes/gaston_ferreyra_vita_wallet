## SETUP ##
NODE:v22.20.0
JDK:11.0.2
APPIUM:3.0.2
## Instalacion
1. Clonar el repositorio:
-En un directorio Local
git clone git@github.com:kIOOnes/gaston_ferreyra_vita_wallet.git
cd gaston_ferreyra_vita_wallet
cd Mobile-test
## Crear y activar entorno virtual
python -m venv env1
.\env1\Scripts\activate  # Windows
source env1/bin/activate  # macOS/Linux
## Instalar dependencias
pip install -r requirements.txt
## Configurar entorno local
Actualizar el documento localconfig, con los valores locales
## Correr tests
pytest tests/test_sample.py -v -s --alluredir=allure-results
## Branches
Master---->Ultima version estable productiva. Por pull request.
Dev------->Version estable que usara el equipo QA. Unicamente por pull request con 1 aprobador/revisor.
gaston---->Branch local. Permisos de pull y de push.


## DOCUMENTACIÓN PARA QA AUTOMATIZADOR
En docstring
## DOCUMENTACION - Definiciones de Estructura y patrones. Convenciones.
S.O.L.I.D ----------------------------> Estructura usada en la codificación orientada a objetos.
Page Objects -------------------------> Patron de diseño para ordenar localizadores, elementos de pantalla, acciones.
A.A.A (Arranque , Acción, Aserción)---> Patron de diseño para armar los test.
PEP 8 --------------------------------> Nomenclatura del proyecto en python.
Convencion de idioma: Ingles.

## DOCUMENTACION - Estructura
├── pages/           # Page objects -----> Pages/Funcionalidad/nombre_pageobject.py. Carpeta de hasta 3 niveles maximo. Agrupada por funcionalidad.
├── tests/           # Test script 
├── core/            # Helpers (Elements, Waits, Gestures)---> Aquí la codificación de los métodos que usaran los pages objects. Dividido por funcionalidad.Elements,Waits,Gestures.
├── screenshots/     # Screenshots captured during tests-----> Aqui iran las capturas de pantalla de ser necesarias
├── reports/         # Allure or other reports---------------> Aqui iran los reportes de Allure que se vayan generando
├── data/            # Test data (users, etc.)--> Aqui iran los fixture y sus clases para ser usados para pruebas. Opcionalmente usar en gitignore datos sensibles.
├── env/             # LocalConfig.py -------> Archivo de Configuración Local. Editar para cada máquina local.
├── utils/           # Aqui iran las utilidades que se llamaran desde cualquier parte del proyecto.
├── env/             # Virtual environment└── README.md
Conftest.py          # Archivo de configuración para Appium





