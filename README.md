# dolar.py
Aplicación escrita en Python para bot de Mastodon con API para publicar actualizaciones del precio del dólar y el euro en bolívares venezolanos.

API del precio del dólar a bolívares: https://github.com/fcoagz/api-pydolarvenezuela?tab=readme-ov-file

Publicado originalmente bajo la licencia Apache 2.0.

![Captura de pantalla de ejemplo de la publicación ejecutada en la aplicación](https://github.com/DanieruOtakuBoy/dolar.py/blob/main/ejemplo.png)

## Descarga de paquetes necesarios para su ejecución

Para usar el programa se recomienda el uso la terminal de Linux (de preferencia una distribución basada en Debian o Ubuntu), Virtualenv, Python en su última versión, y las librerías de Mastodon.py y requests.

### Pasos

* Actualizar los repositorios:

  Siempre es aconsejable actualizar los repositorios antes de cualquier descarga para garantizar que se consiga la versión más recientes y evitar fallas de descarga.

  ```bash
    sudo apt update
  ```

  Con esto los repositorios quedan actualizados, ya de querer actualizar los programas instalados es *totalmente opcional* y se puede realizar mediante el siguiente comando.

  ```bash
    sudo apt upgrade
  ```
  
* Descargar Python:

  La descarga de python se puede realizar también desde la propia terminal con el siguiente comando.

  ```bash
    sudo apt install python3
  ```

  En caso de que python ya estuviera instalado anteriormente saldrá el siguiente mensaje.

  ```
    python3 ya está en su versión más reciente.
  ```

* Descargar Virtualenv:

  Para descargar en la terminal Virtualenv se introduce el siguiente comando.


  ```bash
    sudo apt install virtualenv
  ```

  Este programa es necesario para ejecutar correctamente el programa.

* Crear un entorno virtual:

  Para tener las librerias y archivos correctamente organizados necesitamos un entorno virtual en el cual trabajar, para ello utilizaremos Virtualenv mediante el siguiente código de la terminal.


  ```bash
     virtualenv python
  ```

  En dicho comando, "python" es el directorio o carpeta que creará Virtualenv para almacenar los archivos y las aplicaciones necesarias, dicho directorio o carpeta puede llevar cualquier nombre a parte de python, solo es un nombre de ejemplo.

* Descargar librerias necesarias:

  Las librerias requeridas para que la aplicación de Python funcione correctamente son Mastodon.py y requests, estas dos pueden instalarse fácilmente desde la propia terminal.

  Para ello primero activamos el entorno "python" que creamos con Virtualenv, para ello ejecutamos en la terminal el siguiente comando.

  ```bash
    source /home/(usuario_del_ordenador)/python/bin/activate
  ```

  La terminal marcará en su comienzo (python), marcando que el entorno está activado. Ahora las librerias se podrán descargar con los siguientes comandos.


  ```bash
    pip install Mastodon.py
  ```

  ```bash
    pip install requests
  ```

  Ya con los paquetes y librerias necesarios para su uso, y el entorno virtual activado, se puede utilizar el archivo (apropiadamente configurado con su propia API en la cuenta bot de Mastodon) o crear un archivo personalizado diferente, que utilice una API o comandos diferentes.

## Uso

Para usar la aplicación primero hay que activar el entorno virtual que se ha creado (en caso de no estar activado), para ello se ejecuta el siguiente comando.

```bash
  source /home/(usuario_del_ordenador)/python/bin/activate
```

Ya con el entorno activado, demostrado al tener (python) en el comienzo de la terminal, ejecutamos la aplicación en la propia terminal, ese proceso se hace con el siguiente comando.

```bash
  python /home/(usuario_del_ordenador)/python/dolar.py
```

El directorio en ese comando muestra que la aplicación dolar.py se encuentra almacenado en la carpeta "python" que se encuentra ubicada en la carpeta personal del usuario del ordenador, sin embargo, puede estar almacenada y ser ejecutada en cualquier parte del sistema de archivos que el usuario encuentre más cómoda y óptima.

Tras una corta espera de algunos segundos, si el programa se ejecuta con normalidad, mostrará el mensaje siguiente.

```
  Toot enviado con éxito.
```

## Código de dolar.py

La aplicación dolar.py contiene varios procesos y comandos internos de Python y Mastodon.py, junto con su token de acceso. Para comprender mejor estos datos recomiendo leer o aprender sobre la documentación del lenguaje de programación Python y Mastodon.py.

[Documentación de Mastodon.py (en inglés)](https://mastodonpy.readthedocs.io/en/stable/)

[Documentación de Python 3.13.2 (en español)](https://docs.python.org/es/3/index.html)
