### Iniciar el ejercicio
Funciona con venv/, para iniciar el entorno: 
~~~~source venv/bin/activate

Para ejecutar el script: 
~~~~python3 .

### Comentarios
El dataset está en data/raw/dataset.txt
Y al ejecutar el programa guarda los formatos CSV y JSON en data/processed/

El CSV lo he limpiado y he quitado la tabla de media porque me parecía redundante

El JSON lo he reestructurado para que se parezca más a una API con la siguiente estructura: 
Las temperaturas las he almacenado como array para facilitar el locale

~~~~{
    id: Number,
    geom: {
        long: Number, 
        lat: Number
    },
    temperatures: Array (length 12)
}
