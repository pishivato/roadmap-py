

const equipos = [
    {
        nombre: "sw-mdf-01",
        tipo: "switch",
        ip: "172.16.0.1",
        activo: true,
    },
    
    {
        nombre: "sw-mdf-02",
        tipo: "switch",
        ip: "172.16.0.2",
        activo: false,
    },
    
    {
        nombre: "sw-mdf-03",
        tipo: "switch",
        ip: "172.16.0.3",
        activo: true,
    }
]


const format2 = (equipos) => {
    for (const item of equipos)
    {
        console.log(`Nombre: ${item. nombre}, Tipo: ${item.tipo}, IP: ${item.ip}, Estado: ${item.activo ? "✅": "❌"}`);
    }}

format2(equipos);