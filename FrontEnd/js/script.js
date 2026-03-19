const dropZone = document.getElementById("dropZone");
const inputFile = document.getElementById("fileUpload");
const mainView = document.querySelector(".mainbody");
const chargeView = document.getElementById("ChargeView");
const resultView = document.getElementById("resultView");

let Filestatus = false;

let archivo = null;

// Crear elementos para mostrar info
const nombreArchivo = document.createElement("h2");
const estado = document.createElement("h2");



// DRAG
dropZone.addEventListener("dragover", (e) => {
    e.preventDefault(); 
    dropZone.classList.add("dragover");
});

dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("dragover");
});

// DROP
dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropZone.classList.remove("dragover");

    const file = e.dataTransfer.files[0];
    manejarArchivo(file);
});

// CLICK → abre selector
dropZone.addEventListener("click", () => {
    inputFile.click();
});

// INPUT FILE
inputFile.addEventListener("change", (e) => {
    const file = e.target.files[0];
    manejarArchivo(file);
});

// FUNCIÓN PRINCIPAL
function manejarArchivo(file) {
	dropZone.innerHTML = "";
	dropZone.appendChild(nombreArchivo);
	dropZone.appendChild(estado);
    if (!file) return;

    archivo = file;

    // Mostrar nombre
    nombreArchivo.textContent = "Archivo: " + file.name;

    // Estado inicial
    estado.textContent = "Cargando...";

    // Simulación de carga
    setTimeout(() => {
        estado.textContent = "Listo ✅";
    }, 800);

    Filestatus = true
}


const btnEnviar = document.getElementById("btnEnviar");

btnEnviar.addEventListener("click", (e) => {
    e.preventDefault();

    if (!archivo) {
        alert("Debes seleccionar un archivo primero");
        return;
    }

    mainView.style.display = "none";
    chargeView.style.display = "flex";

    const formData = new FormData();
    formData.append("imagen", archivo);

    fetch("http://localhost:5000/upload", {
        method: "POST",
        body: formData
    })
    .then(res => res.text())
    .then(data => {
        console.log("Respuesta:", data);
        alert("Archivo enviado correctamente ✅");
    })
    .catch(err => {
        console.error(err);
        alert("Error al enviar ❌");
    });
});