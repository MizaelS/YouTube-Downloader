# Descargador de YouTube

## Descripción

Esta es una aplicación web desarrollada en Python utilizando el framework Flask. Permite a los usuarios descargar videos de YouTube en diferentes resoluciones y calidades de audio. La aplicación muestra una vista previa del video, el título, la cantidad de vistas y permite seleccionar la calidad de video y audio antes de descargar.

## Requerimientos

- Python 3
- Flask
- pytube
- ffmpeg
- Una VPS (Se recomienda comprar una en [Teramont Host](https://www.teramont.net/vps))

## Instalación

1. Clona este repositorio en tu máquina local.

```
git clone https://github.com/MizaelS/YouTube-Downloader.git
```

2. Navega al directorio del proyecto.

```
cd YouTube-Downloader
```

3. Crea un entorno virtual.

```
python -m venv env
```

4. Activa el entorno virtual.

- En Windows:

```
.\env\Scripts\activate
```

- En macOS y Linux:

```
source env/bin/activate
```

5. Instala las dependencias necesarias.

```
pip install -r requirements.txt
```

6. Inicia la aplicación.

```
python app.py
```

La aplicación ahora debería estar ejecutándose en `http://127.0.0.1:5001/`.

## Vista Previa

Puedes ver una vista previa de la aplicación en funcionamiento en [este enlace](http://198.251.82.48:5001/).

## Licencia

Este proyecto está bajo la licencia MIT.
