# Twitter-Bot
Este repositorio contiene el código y los archivos correspondientes a un bot de Twitter, 
el cual es capaz de publicar tweets desde un archivo de texto así como también imágenes, ambos de forma periódica según un tiempo especificado. 

El proyecto nació con el propósito de ser destinado a publicar citas e imágenes del artista argentino Charly García. El bot fue desplegado y comenzó a funcionar públicamente en julio de 2021 a partir de los servicios de AWS. Desde diciembre de 2022 se encuentra trabajando gracias a [Railway](https://railway.app/). La cuenta de Twitter correspondiente al bot es: https://twitter.com/Bot_CharlyG

El código se encuentra comentado a fin de explicar los distintos procedimientos, y es funcional al día de la fecha. 
Sólo deben reemplazarse las keys, la lista de tweets en el archivo "text.txt" y las imágenes a publicar, 
que se encuentran en la carpeta images y deben ser archivos png enumerados. El tiempo que transcurre entre cada publicación también puede ser modificado, 
siempre respetando los segundos como unidad.
