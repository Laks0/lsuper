# lsuper

### Instalación

correr con 

	/ruta/al/archivo/lsuper
es recomendable crear un link al archivo en algun directorio dentro del path

### Configuración

en el archivo config.py están todos los parámetros por defecto 

### Uso

	lsuper -h

para pedir ayuda.

***

	lsuper -d <depth>
  
para elegir la profundidad de la lista, por ejemplo

	lsuper -d 1
  
muestra todo el directorio, y el contenido en las carpetas del directorio. Un grado de profundidad.

***

	lsuper --onlyDirs
solo muestra los nombres de los directorios
	lsuper --onlyFiles
solo muestra los nombres de los archivos.
Por ejemplo:

	lsuper --onlyDirs -d 2
muestra solo los nombres de los directorios con 2 grados de profundidad.
