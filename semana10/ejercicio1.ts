let nombre: string = "alex";
let edad: number = 28;
let activo: boolean = true;

type Estado = "activo"| "inactivo" | "mantenimiento";



//console.log(`${nombre}, ${edad}, ${activo}`)

interface Equipo {
    id: number;
    nombre: string;
    tipo: string;
    ip: string;
    ubicacion: string;
    activo: Estado;
}


const equipos: Equipo[] = [
    {id: 1,
    nombre: "SW-MDF-01",
    tipo: "switch",
    ip: "172.16.0.1",
    ubicacion: "MDF",
    activo: "activo"}, 
    
    {id: 2,
    nombre: "SW-IDF-02",
    tipo: "switch",
    ip: "172.16.0.2",
    ubicacion: "IDF",
    activo: "activo"},

    {id: 3,
    nombre: "SW-IDF-03",
    tipo: "switch",
    ip: "172.16.0.3",
    ubicacion: "IDF",
    activo: "inactivo"}

];

const formatear = (equipo: Equipo): string =>{

    return `${equipo.id}, ${equipo.nombre}, ${equipo.tipo}, ${equipo.ubicacion}, ${equipo.activo}`;

}


for (const equipo of equipos){

    console.log(formatear(equipo));
}

const envolver = <T>(data: T) => ({
    data,
    ok: true
});

console.log(envolver<Equipo>(equipos[0]));
console.log(envolver<string>("SW-MDF-01"));