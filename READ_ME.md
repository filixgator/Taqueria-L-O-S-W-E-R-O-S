# Tacos  L O S  |  W E R O S

Here, we create a taco shop that reads, processes, and answer orders from SQS. Just like a real taco shop, we have Taqueros, Tortilleras, and even a bar.
  - Types: 
    - Tacos, Quesadilla, Mulita, Tostada, Tortas
  - Meat:
    - Asada, Adobada, Cabeza, Lengua, Suadero       
  - Ingredients:
    - Cebolla, Salsa, Guacamole, Queso, Frijoles 

# Authors:

- Felix Quevedo: [filixgator](https://github.com/filixgator)
- Alexis Aldrete: [alexisaldrete](https://github.com/alexisaldrete)
- Andrés Marín: [Hanburu](https://github.com/Hanburu)
  
### Support

Taqueria L-O-S-W-E-R-O-S used the following to work correctly:

* [Matplotlib] - Helps with the graphics in a user-friendly way


 Taqueria L-O-S-W-E-R-O-S itself is open source with a [public repository][Taqueria L-O-S-W-E-R-O-S] on GitHub.

### Installation

Taqueria L-O-S-W-E-R-O-S requires some extra libraries for it to run:  

[Boto3](https://github.com/boto/boto3) 

It is the amazon web services (AWS) developing software kit (SDK) for python. This module allows python developers to write software that makes use of the amazon services. To install Boto3 we have to write in the terminal:

```sh
  $ pip install boto3
```
Then, we have to set the credentials in an encrypted file:

```sh
      ~/.aws/credentials 
```
 Inside this file we will have:
 
```sh
     [default]
     aws_access_key_id = YOUR_KEY
     aws_secret_access_key = YOUR_SECRET_ACCESS_KEY         
```

After that we have to set the region in the same encrypted folder , but different file: 

```sh
      ~/.aws/config        
```
Inside this file we will have: 
```sh
      [default]
      region=us-east-1      
```
 In python it is important to import boto3 in our file:
 
```sh
      import boto3    
```       
          
In our program we used this library to receive orders and send the corresponding response.

[Json](https://docs.python.org/2/library/json.html)

We used the Json library, Json is a way to structure data for it to be interpreted by any language. To use it the only thing we have to do is import it in our python file: 
```sh
      import json  
```   
        
[Matplotlib](https://matplotlib.org/)

This library was used to plot, make graphs and tables. To install it we did: 
           
Debian / Ubuntu:
```sh
      sudo apt-get install python-matplotlib
```  
Windows: 
```sh
      python -m pip install -U pip setuptools
      python -m pip install matplotlib
```  
In our python files (where the graphs were made) we imported this library as: 
```sh
      import matplotlib.pyplot
```

#### Others

We also used other libraries that are already installed in python and only have to be imported to the files in which they will be used like: 
- Threading
- Time 
- Queue

### How it works:

![Alt Text](https://github.com/AnaValeriaGM/TacosFranc/blob/master/finalflow2.png)



**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [TacosFranc]: <https://github.com/AnaValeriaGM/TacosFranc/tree/master/CarpetaProyecto>
   [PyQT]: <https://github.com/pyqtgraph/pyqtgraph>




