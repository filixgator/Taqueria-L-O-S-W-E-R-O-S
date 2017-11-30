### How it works:

![Alt Text](https://github.com/filixgator/Taqueria-L-O-S-W-E-R-O-S/blob/master/1.png)
![Alt Text](https://github.com/filixgator/Taqueria-L-O-S-W-E-R-O-S/blob/master/2.png)
![Alt Text](https://github.com/filixgator/Taqueria-L-O-S-W-E-R-O-S/blob/master/3.png)
![Alt Text](https://github.com/filixgator/Taqueria-L-O-S-W-E-R-O-S/blob/master/4.png)

# Tacos  L O S  |  W E R O S

El programa simula una taquería que lee, procesa y responde órdenes de SQS. Simula taqueros, ingredientes y órdenes en tiempo real

  - Platillo: 
    - Tacos, Quesadilla, Mulita, Tostada, Tortas
  - Carne:
    - Asada, Adobada, Cabeza, Lengua, Suadero       
  - Ingredientes:
    - Cebolla, Salsa, Guacamole, Queso, Frijoles 

# Authors:

- Felix Quevedo: [filixgator](https://github.com/filixgator)
- Alexis Aldrete: [alexisaldrete](https://github.com/alexisaldrete)
- Andrés Marín: [Hanburu](https://github.com/Hanburu)
  
### Support

Taqueria L-O-S-W-E-R-O-S usa los siguientes recursos para su funcionamiento:

[Matplotlib](https://matplotlib.org/) - Grafica de manera amigable


 Taqueria L-O-S-W-E-R-O-S es un programa de código abierto [public repository][Taqueria L-O-S-W-E-R-O-S] en GitHub.

### Installation

Taqueria L-O-S-W-E-R-O-S requiere de librerías extras para su ejecución:  

[Boto3](https://github.com/boto/boto3) 

Es el the amazon web services (AWS) developing software kit (SDK) para python. Este módulo permite a ddesarrolladores de python programar software que haga uso de los servicios de mensajería de Amazon. Para su instalación se debe escribir en terminal:

```sh
  $ pip install boto3
```
Luego se definen las credenciales en un archivo encriptado:

```sh
      ~/.aws/credentials 
```
 Dentro de este archivo se encuentran un ID de la clave de acceso y una clave secreta de acceso:
 
```sh
     [default]
     aws_access_key_id = YOUR_KEY
     aws_secret_access_key = YOUR_SECRET_ACCESS_KEY         
```

Después se define la región en el mismo folder encriptado pero en un archivo diferente:

```sh
      ~/.aws/config        
```
Este archivo debe contener: 
```sh
      [default]
      region=us-east-1      
```
 En python se importa la librería al archivo del programa:
 
```sh
      import boto3    
```       
          
El uso de esta librería es recivir órdenes y regresar una respuesta correspondiente.

[Json](https://docs.python.org/2/library/json.html)

Se usó la librería de Json, para estructurar la data que sería interpretada por el lenguade de elección, python. Para usar esta librería solo es necesario importarla en nuestro archivo main. 
```sh
      import json  
```   
        
[Matplotlib](https://matplotlib.org/)

Esta ibrería se usó para graficar y tabular. Para su instalación se siguen los siguientes pasos: 
           
Debian / Ubuntu:
```sh
      sudo apt-get install python-matplotlib
```  
Windows: 
```sh
      python -m pip install -U pip setuptools
      python -m pip install matplotlib
```  
En nuestro archivo main de python se imprtó la librería de la siguiente manera: 
```sh
      import matplotlib.pyplot as ptl
```

#### Otros

También se usaro otras librerías que ya están instaladas en python y sólo deben mandarse a llamar desde los archivos existentes como: 
- Threading
- Time 
- Queue


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Taqueria-L-O-S-W-E-R-O-S]: <https://github.com/filixgator/Taqueria-L-O-S-W-E-R-O-S>




