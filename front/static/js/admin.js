    // Envia la informacion del hotel a la API para agregarlo a la base de datos

document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.getElementsByClassName('toggle-hotel-btn');

    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', function (event) {
            const hotelId = event.target.dataset.hotelId;
            toggleHotelStatus(hotelId, event.target);
        });
    }

    const form = document.getElementById('form-agregar-hotel');

    document.getElementById("agregar-imagen").addEventListener("click", function () {
        const imagenesContainer = document.getElementById("imagenes-container");
        const nuevaImagen = document.createElement("input");
        nuevaImagen.type = "url";
        nuevaImagen.name = "imagenes_hotel[]";
        nuevaImagen.classList.add("imagen-url");
        nuevaImagen.placeholder = "https://www.buscateUnaImagenEnGoogle.com";
        imagenesContainer.appendChild(nuevaImagen);
    });

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(form);
        const imagenesImputs = document.querySelectorAll('input[name="imagenes_hotel[]"]');
        const data = {
            nombre: formData.get('nombre_hotel'),
            descripcion: formData.get('descripcion_hotel'),
            ubicacion: formData.get('ubicacion_hotel'),
            imagenesHotel: Array.from(imagenesImputs).map(input => input.value.trim())
        };

        fetch('https://marm4.pythonanywhere.com/admin/agregar_hotel', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (result.hotel) {
                addHotelRow(result.hotel);
                form.reset();
            } else {
                alert(result.error || 'Error al agregar el hotel');
            }
        })
        .catch(error => {
            alert('Error al agregar el hotel: ' + error);
        });
    });
});

    // Cambia el estado del hotel (habilitado/deshabilitado) en la base de datos

function toggleHotelStatus(hotelId, button) {
    const isDeshabilitado = button.classList.contains('deshabilitado');
    const action = isDeshabilitado ? 'habilitar' : 'deshabilitar';
    const confirmMessage = isDeshabilitado ?
        "¿Estás seguro de que quieres habilitar este hotel?" :
        "¿Estás seguro de que quieres deshabilitar este hotel?";

    
        

    if (confirm(confirmMessage)) {
        fetch(`/admin/${action}_hotel/${hotelId}`, {
            method: 'POST',
        })
        .then(response => {
            if (response.ok) {
                alert(`Hotel ${isDeshabilitado ? 'habilitado' : 'deshabilitado'} correctamente`);
                button.classList.toggle('deshabilitado');
                button.textContent = isDeshabilitado ? 'Deshabilitar' : 'Habilitar';
                const row = document.getElementById(`hotel-row-${hotelId}`);
                if (row) {
                    row.classList.toggle('deshabilitado');
                } else {
                    console.error(`Row with ID hotel-row-${hotelId} not found`);
                }
            } else {
                alert(`Hubo un error al ${isDeshabilitado ? 'habilitar' : 'deshabilitar'} el hotel`);
            }
        })
        .catch(error => {
            alert(`Error al ${isDeshabilitado ? 'habilitar' : 'deshabilitar'} el hotel: ` + error);
        });
    }
}

    // Agrega el hotel recien creado a la tabla de hoteles

function addHotelRow(hotel) {
    const tableBody = document.getElementById('hoteles-table-body');
    const row = document.createElement('tr');
    row.id = `hotel-row-${hotel.hotel_id}`;
    row.className = hotel.habilitado ? '' : 'deshabilitado';

    const habilitadoClass = hotel.habilitado ? '' : 'deshabilitado';
    const buttonText = hotel.habilitado ? 'Deshabilitar' : 'Habilitar';

    row.innerHTML = `
        <td>${hotel.hotel_id}</td>
        <td>${hotel.nombre}</td>
        <td>
            <button class="toggle-hotel-btn ${habilitadoClass}" data-hotel-id="${hotel.hotel_id}">
                ${buttonText}
            </button>
        </td>
    `;

    tableBody.appendChild(row);

    const button = row.querySelector('.toggle-hotel-btn');
    button.addEventListener('click', function(event) {
        const hotelId = event.target.dataset.hotelId;
        toggleHotelStatus(hotelId, event.target);
    });
}

    // Envia la informacion de la habitacion a la API para agregarla a la base de datos

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector('form[action="admin_actions.php"]');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const capacidad = document.getElementById('capacidad').value;
        const hotelId = document.getElementById('hotel_id').value;

        const data = {
            capacidad: capacidad,
            hotel_id: hotelId
        };

        fetch('https://marm4.pythonanywhere.com/admin/agregar_habitacion', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(result => {
                if (result.habitacion) {
                    alert('Habitación agregada correctamente');
                    addHabitacionRow(result.habitacion);
                    form.reset();
                } else {
                    alert('Error al agregar la habitación');
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('Error al agregar la habitación');
            });
    });

    // Aca empieza el codigo para deshabilitar habitacion

    const buttons = document.getElementsByClassName('toggle-habitacion-btn');

    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', function (event) {
            const habitacionId = event.target.dataset.habitacionId;
            toggleHabitacionStatus(habitacionId, event.target);
        });
    }
});

    // Agrega la habitacion recien creada a la tabla de habitaciones

function addHabitacionRow(habitacion) {
    console.log(habitacion);
    const tableBody = document.getElementById('habitaciones-table-body');
    const row = document.createElement('tr');
    row.id = `habitacion-row-${habitacion.id}`;
    const buttonText = 'Deshabilitar';

    row.innerHTML = `
        <td>${habitacion.id}</td>
        <td>${habitacion.capacidad}</td>
        <td>${habitacion.hotel.id}</td>
        <td>
            <button class="toggle-habitacion-btn" data-habitacion-id="${habitacion.id}">
                ${buttonText}
            </button>
        </td>   
    `;

    tableBody.appendChild(row);

    const button = row.querySelector('.toggle-habitacion-btn');
    button.addEventListener('click', function (event) {
        const habitacionId = event.target.dataset.habitacionId;
        toggleHabitacionStatus(habitacionId, event.target);
    });
}

    // Cambia el estado de la habitacion (habilitado/deshabilitado) en la base de datos

function toggleHabitacionStatus(habitacionId, button) {
    const isDeshabilitado = button.classList.contains('deshabilitado');
    const action = isDeshabilitado ? 'habilitar' : 'deshabilitar';
    const confirmMessage = isDeshabilitado ?
        "¿Estás seguro de que quieres habilitar esta habitacion?" :
        "¿Estás seguro de que quieres deshabilitar esta habitacion?";

    if (confirm(confirmMessage)) {
        fetch(`/admin/${action}_habitacion/${habitacionId}`, {
            method: 'POST',
        })
            .then(response => {
                if (response.ok) {
                    alert(`habitacion ${isDeshabilitado ? 'habilitada' : 'deshabilitada'} correctamente`);
                    button.classList.toggle('deshabilitado');
                    button.textContent = isDeshabilitado ? 'Deshabilitar' : 'Habilitar';
                    document.getElementById(`habitacion-row-${habitacionId}`).classList.toggle('deshabilitado');
                } else {
                    alert(`Hubo un error al ${isDeshabilitado ? 'habilitar' : 'deshabilitar'} la habitacion`);
                }
            })
            .catch(error => {
                alert(`Error al ${isDeshabilitado ? 'habilitar' : 'deshabilitar'} la habitacion: ` + error);
            });
    }
}

    // Envia la informacion del servicio a la API para agregarlo a la base de datos

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('form-agregar-servicio');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const nombreServicio = document.getElementById('nombre_servicio').value;
        const descripcionServicio = document.getElementById('descripcion_servicio').value;
        const urlImagen = document.getElementById('url_imagen').value;
        const ubicacionServicio = document.getElementById('ubicacion_servicio').value;
        const categoriaServicio = document.getElementById('categoria_servicio').value;

        const data = {
            nombre: nombreServicio,
            descripcion: descripcionServicio,
            url_imagen: urlImagen,
            ubicacion: ubicacionServicio,
            categoria: categoriaServicio
        };

        fetch('https://marm4.pythonanywhere.com/admin/agregar_servicio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                if (data.servicio) {
                    addServicioRow(data.servicio);
                    form.reset();
                }
            }
            )
            .catch((error) => {
                console.error('Error:', error);
                alert('Error al agregar el servicio');
            });
    }
    );
});

    // Agrerga el servicio recien creado a la tabla de servicios

function addServicioRow(servicio) {
    const tableBody = document.getElementById('servicios-table-body');
    const row = document.createElement('tr');
    row.id = `servicio-row-${servicio.servicio_id}`;
    row.className = servicio.habilitado ? '' : 'deshabilitado';

    const habilitadoClass = servicio.habilitado ? '' : 'deshabilitado';
    const buttonText = servicio.habilitado ? 'Deshabilitar' : 'Habilitar';

    row.innerHTML = `
        <td>${servicio.servicio_id}</td>
        <td>${servicio.nombre}</td>
        <td>${servicio.descripcion}</td>
        <td>${servicio.categoria}</td>
        <td>
            <button class="toggle-servicio-btn ${habilitadoClass}" data-servicio-id="${servicio.servicio_id}">
                ${buttonText}
            </button>
        </td>
        `;

    tableBody.appendChild(row);

    const button = row.querySelector('.toggle-servicio-btn');
    button.addEventListener('click', function (event) {
        const servicioId = event.target.dataset.servicioId;
        toggleServicioStatus(servicioId, event.target);
    });
}

    // Cambia el estado del servicio (habilitado/deshabilitado) en la base de datos

function toggleServicioStatus(servicioId, button) {
    const isDeshabilitado = button.classList.contains('deshabilitado');
    const action = isDeshabilitado ? 'habilitar' : 'deshabilitar';
    const confirmMessage = isDeshabilitado ?
        "¿Estás seguro de que quieres habilitar este servicio?" :
        "¿Estás seguro de que quieres deshabilitar este servicio?";

    if (confirm(confirmMessage)) {
        fetch(`/admin/${action}_servicio/${servicioId}`, {
            method: 'POST',
        })
            .then(response => {
                if (response.ok) {
                    alert(`servicio ${isDeshabilitado ? 'habilitada' : 'deshabilitada'} correctamente`);
                    button.classList.toggle('deshabilitado');
                    button.textContent = isDeshabilitado ? 'Deshabilitar' : 'Habilitar';
                    document.getElementById(`servicio-row-${servicioId}`).classList.toggle('deshabilitado');
                } else {
                    alert(`Hubo un error al ${isDeshabilitado ? 'habilitar' : 'deshabilitar'} el servicio`);
                }
            })
            .catch(error => {
                alert(`Error al ${isDeshabilitado ? 'habilitar' : 'deshabilitar'} el servicio: ` + error);
            });
    }
}