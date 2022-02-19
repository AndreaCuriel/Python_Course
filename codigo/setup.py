##documento para configurar los paquetes distribuibles, que se puedan usar sin importar su direccion

from setuptools import setup
setup(

	name="paquetecalculos",
	version="1.0",
	description="Paquetes de calculos matematicos",
	author="Andrea",
	author_email="acurielipn@hotmail.com",
	url="wwww.",
	#agregar la ruta completa del paquete 
	packages=["calculos", "calculos.redondeo_potencia"]

	)