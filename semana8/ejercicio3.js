const obtenerEquipos = async () => {
    const respuesta = await fetch("http://127.0.0.1:8000/equipos");
    const datos = await respuesta.json();
    const primero = datos[0];
    const primeroActualizar = {...primero, ip : "172.16.0.99"};

    console.log(primero);
    console.log(primeroActualizar);

    for (const {id, nombre, tipo, ip, ubicacion, activo} of datos)
    {
        console.log(`ID: ${id}, Nombre: ${nombre}, Tipo: ${tipo}, IP: ${ip}, Ubicacion: ${ubicacion}, Estado: ${activo ? "✅":"❌"}`);
    }
}

obtenerEquipos();



