const dropZone = document.getElementById("dropZone");
const inputFile = document.getElementById("fileUpload");
const mainView = document.querySelector(".mainbody");
const chargeView = document.getElementById("ChargeView");
const resultView = document.getElementById("resultView");

let Filestatus = false;

let archivo = null;

window.addEventListener("beforeunload", () => {
    console.log("SE ESTÁ RECARGANDO 🔴");
});

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


// INPUT FILE
inputFile.addEventListener("change", (e) => {
    const file = e.target.files[0];
    manejarArchivo(file);
});



// FUNCIÓN PRINCIPAL
function manejarArchivo(file) {
    if (!file) return;

    const tiposPermitidos = ['image/png', 'image/jpeg', 'image/jpg'];
    const extensionesPermitidas = ['png', 'jpg', 'jpeg'];
    const extension = file.name.split('.').pop().toLowerCase();

    if (!tiposPermitidos.includes(file.type)) {
        alert("Solo se permiten imágenes (PNG, JPG, JPEG)");
        inputFile.value = "";
        return;
    }

    if (!extensionesPermitidas.includes(extension)) {
        alert("Extensión no permitida");
        inputFile.value = "";
        return;
    }

    const reader = new FileReader();

    reader.onload = function (e) {
        const img = new Image();
        img.src = e.target.result;

        img.onload = () => {
            archivo = file;

            dropZone.innerHTML = "";
            dropZone.appendChild(nombreArchivo);
            dropZone.appendChild(estado);

            nombreArchivo.textContent = "Archivo: " + file.name;
            estado.textContent = "Cargando...";

            setTimeout(() => {
                estado.textContent = "Listo";
            }, 800);

            Filestatus = true;
        };

        img.onerror = () => {
            alert("El archivo no es una imagen válida");
            inputFile.value = "";
        };
    };

    reader.readAsDataURL(file);
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
    .then(res => res.json())
    .then(data => {
        chargeView.style.display = "none";
        document.getElementById("resultView").style.display = "block";

        const previewURL = URL.createObjectURL(archivo);
        document.getElementById("preview").src = previewURL;

        const diag = document.getElementById("diagnostico");
        diag.innerText = data.prediccion;

        if (data.prediccion === "BENIGNO") {
            diag.style.backgroundColor = "teal";
            diag.style.color = "white";
        } else {
            diag.style.backgroundColor = "red";
            diag.style.color = "white";
        }

        document.getElementById("confianza").innerText =
            (data.probabilidad * 100).toFixed(2) + "%";
    })
    .catch(err => {
        chargeView.style.display = "none";
        mainView.style.display = "flex";
        alert("Error al conectar con el servidor. Intenta de nuevo.");
        console.error(err);
    });
});

const btnPDF = document.getElementById("pdfBtn");

btnPDF.addEventListener("click", () => {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Título
    doc.setFont("helvetica", "bold");
    doc.setFontSize(22);
    doc.setTextColor(10, 154, 158); // teal
    doc.text("NeoDermisX - Resultado", 105, 20, { align: "center" });

    // Línea separadora
    doc.setDrawColor(10, 154, 158);
    doc.setLineWidth(0.5);
    doc.line(20, 25, 190, 25);

    // Fecha
    doc.setFont("helvetica", "normal");
    doc.setFontSize(11);
    doc.setTextColor(100);
    const fecha = new Date().toLocaleDateString("es-CO", {
        year: "numeric", month: "long", day: "numeric"
    });
    doc.text("Fecha: " + fecha, 20, 35);

    // Imagen
    const canvas = document.createElement("canvas");
    const img = document.getElementById("preview");
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    canvas.getContext("2d").drawImage(img, 0, 0);
    const imgData = canvas.toDataURL("image/jpeg");

    doc.setFont("helvetica", "bold");
    doc.setFontSize(13);
    doc.setTextColor(0);
    doc.text("Imagen analizada:", 20, 48);
    doc.addImage(imgData, "JPEG", 20, 52, 80, 80);

    // Diagnóstico
    doc.setFontSize(13);
    doc.text("Diagnóstico IA:", 20, 148);

    const prediccion = document.getElementById("diagnostico").innerText;
    const esBenigno = prediccion.toLowerCase() === "benigno";

    doc.setFillColor(esBenigno ? 10 : 220, esBenigno ? 154 : 50, esBenigno ? 158 : 50);
    doc.roundedRect(20, 153, 50, 10, 3, 3, "F");
    doc.setTextColor(255);
    doc.setFont("helvetica", "bold");
    doc.setFontSize(11);
    doc.text(prediccion, 45, 160, { align: "center" });

    // Confianza
    doc.setTextColor(0);
    doc.setFont("helvetica", "bold");
    doc.setFontSize(13);
    doc.text("Nivel de confianza:", 20, 178);
    doc.setFontSize(20);
    doc.setTextColor(10, 154, 158);
    doc.text(document.getElementById("confianza").innerText, 20, 190);

    // Footer
    doc.setTextColor(150);
    doc.setFontSize(9);
    doc.setFont("helvetica", "normal");
    doc.text("Este resultado es orientativo. Consulta siempre a un especialista.", 105, 285, { align: "center" });

    doc.save("resultado-neodermisx.pdf");
});