const obtenerEquipos = async () => {
    const respuesta = await fetch("http://127.0.0.1:8000/equipos");
    const datos = await respuesta.json();
    for (const item of datos)
    {
        console.log(`ID: ${item.id}, Nombre: ${item.nombre}, Tipo: ${item.tipo}, Ubicacion: ${item.ubicacion}, Estado: ${item.activo ? "✅":"❌"}`);
    }
}

obtenerEquipos();