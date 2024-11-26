document.addEventListener("DOMContentLoaded", function() {
    // Add event listener to all toggle buttons
    const buttons = document.getElementsByClassName('toggle-hotel-btn');
    
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', function(event) {
            const hotelId = event.target.dataset.hotelId;
            toggleHotelStatus(hotelId, event.target);
        });
    }

    // Add event listener to the form to handle hotel addition
    const form = document.getElementById('form-agregar-hotel');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const data = {
            nombre: formData.get('nombre_hotel'),
            descripcion: formData.get('descripcion_hotel'),
            ubicacion: formData.get('ubicacion_hotel')
        };

        fetch('/admin/agregar_hotel', {
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

    // Attach event listener to the new button
    const button = row.querySelector('.toggle-hotel-btn');
    button.addEventListener('click', function(event) {
        const hotelId = event.target.dataset.hotelId;
        toggleHotelStatus(hotelId, event.target);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form[action="admin_actions.php"]');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const capacidad = document.getElementById('capacidad').value;
        const hotelId = document.getElementById('hotel_id').value;

        const data = {
            capacidad: capacidad,
            hotel_id: hotelId
        };

        fetch('/admin/agregar_habitacion', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .catch((error) => {
            console.error('Error:', error);
            alert('Error al agregar la habitación');
        });
    });

    // Aca empieza el codigo para deshabilitar habitacion

    const buttons = document.getElementsByClassName('toggle-habitacion-btn');
    
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', function(event) {
            const habitacionId = event.target.dataset.habitacionId;
            toggleHabitacionStatus(habitacionId, event.target);
        });
    }
});

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


document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('form-agregar-servicio');

    form.addEventListener('submit', function(event) {
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

        fetch('http://127.0.0.1:5000/admin/agregar_servicio', {
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
                const serviciosTable = document.getElementById('servicios-table-body');
                
                const newRow = document.createElement('tr');
                newRow.id = `servicio-row-${data.servicio.servicio_id}`;

                newRow.innerHTML = `
                    <td>${data.servicio.servicio_id}</td>
                    <td>${data.servicio.nombre}</td>
                    <td>${data.servicio.descripcion}</td>
                    <td>${categoriaServicio}</td>
                
                `;
                
                serviciosTable.appendChild(newRow);
            }

            document.getElementById('nombre_servicio').value = '';
            document.getElementById('descripcion_servicio').value = '';
            document.getElementById('url_imagen').value = '';
            document.getElementById('ubicacion_servicio').value = '';

        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Error al agregar el servicio');
        });
    });
});