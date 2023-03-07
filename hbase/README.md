# Apache HBase

## Cómo empezar

### Puesta en marcha

```yml
version: '3.9'

services:
  hbase:
    image: bde2020/hbase-standalone
    restart: always
    volumes:
      - ./populate:/data/populate
      - ./hbase-site.xml:/opt/hbase-1.2.6/conf/hbase-site.xml
    container_name: hbase
```

```bash
docker-compose up -d
```

### Configuración del sistema gestor y ejecución de la práctica

Ejecutar una terminal dentro del contenedor docker, con el siguiente comando:

```bash
docker exec -it hbase /bin/bash
```

Una vez en el interior del contenedor, acceder al directorio /data/populate
y ejecutar el script populate.sh:

```bash
cd /data/populate
./populate.sh
```

Este script ejecuta todas las sentencias de creación de tablas, gestión de
permisos de usuarios e inserción de datos.

Todos los ficheros que realizan estas funciones, con la sintaxis apropiada
para hbase, se encuentran tanto en el directorio /data/populate del contenedor
docker, como en el subdirectorio populate de fuentes/hbase, donde se encuentra
este fichero, README.md.
