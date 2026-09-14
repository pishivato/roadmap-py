"use strict";
let nombre = "alex";
let edad = 28;
let activo = true;
const equipos = [
    { id: 1,
        nombre: "SW-MDF-01",
        tipo: "switch",
        ip: "172.16.0.1",
        ubicacion: "MDF",
        activo: "activo" },
    { id: 2,
        nombre: "SW-IDF-02",
        tipo: "switch",
        ip: "172.16.0.2",
        ubicacion: "IDF",
        activo: "activo" },
    { id: 3,
        nombre: "SW-IDF-03",
        tipo: "switch",
        ip: "172.16.0.3",
        ubicacion: "IDF",
        activo: "inactivo" }
];
const formatear = (equipo) => {
    return `${equipo.id}, ${equipo.nombre}, ${equipo.tipo}, ${equipo.ubicacion}, ${equipo.activo}`;
};
for (const equipo of equipos) {
    console.log(formatear(equipo));
}
