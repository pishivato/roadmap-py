from fastapi import FastAPI
from pydantic import BaseModel

class Equipo(BaseModel):
    nombre: str
    tipo: str
    ip: str
    ubicacion: str
    activo: bool



app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API de inventario de red"}


import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5433,
        database="roadmap",
        user="sqltest",
        password="sql123"
    )

@app.get("/equipos")
def listar_equipos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, tipo, ip, ubicacion, activo FROM equipos")
    filas = cursor.fetchall()
    cursor.close()
    conn.close()
    
    equipos = []
    for fila in filas:
        equipos.append({
            "id": fila[0],
            "nombre": fila[1],
            "tipo": fila[2],
            "ip": fila[3],
            "ubicacion": fila[4],
            "activo": fila[5]
        })
    
    return equipos

@app.post("/equipos")
def crear_equipos(equipo: Equipo):
    # conectar a la BD
    conn = get_connection()
    cursor = conn.cursor()

    # ejecutar INSERT
    cursor.execute("""  
        INSERT INTO equipos (nombre, tipo, ip, ubicacion, activo)
        VALUES(%s, %s, %s, %s, %s)
        RETURNING id, nombre, tipo, ip, ubicacion, activo""", 
        (equipo.nombre, equipo.tipo, equipo.ip, equipo.ubicacion, equipo.activo))
    conn.commit()
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
        
    # retornar el equipo creado
    return {
        "id":fila[0],
        "nombre":fila[1],
        "tipo":fila[2],
        "ip":fila[3],
        "ubicacion":fila[4],
        "activo":fila[5]
    }

@app.delete("/equipos/{id}")
def eliminar_equipo(id:int):
    # conectar a la BD
    conn = get_connection()
    cursor = conn.cursor()

    # Delete 
    cursor.execute("DELETE FROM equipos where id = %s", (id, ))

    conn.commit()
    cursor.close()
    conn.close()

    return f"{id} Deleted"


@app.put("/equipos/{id}")
def actualizar_equipo(id:int, equipo: Equipo):
    # conectar a la BD
    conn = get_connection()
    cursor = conn.cursor()

    #PUT
    cursor.execute("""
        UPDATE equipos 
        SET nombre = %s, tipo = %s, ip = %s, ubicacion = %s, activo = %s
        WHERE id = %s
        RETURNING id, nombre, tipo, ip, ubicacion, activo""", 
        (equipo.nombre, equipo.tipo, equipo.ip, equipo.ubicacion, equipo.activo, id ))
    conn.commit()
    fila = cursor.fetchone()
    cursor.close()
    conn.close()

    return {
        "id":fila[0],
        "nombre":fila[1],
        "tipo":fila[2],
        "ip":fila[3],
        "ubicacion":fila[4],
        "activo":fila[5]
    }


    


