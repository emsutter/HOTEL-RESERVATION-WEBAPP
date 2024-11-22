document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('form-agregar-hotel');

    document.getElementById("agregar-imagen").addEventListener("click", function() {
        const imagenesContainer = document.getElementById("imagenes-container");
        const nuevaImagen = document.createElement("input");
        nuevaImagen.type = "url";
        nuevaImagen.name = "imagenes_hotel[]"; 
        nuevaImagen.classList.add("imagen-url");
        nuevaImagen.placeholder = "https://www.buscateUnaImagenEnGoogle.com";
        imagenesContainer.appendChild(nuevaImagen);
    });

    form.addEventListener('submit', function(event) {
        event.preventDefault();
       
        const nombreHotel = document.getElementById('nombre_hotel').value;
        const descripcionHotel = document.getElementById('descripcion_hotel').value;
        const ubicacionHotel = document.getElementById('ubicacion_hotel').value;
        const imagenesInputs = document.querySelectorAll('input[name="imagenes_hotel[]"]');
        const imagenesHotel = Array.from(imagenesInputs).map(input => input.value.trim());

        const data = {
            nombre: nombreHotel,
            descripcion: descripcionHotel,
            ubicacion: ubicacionHotel,
            imagenes: imagenesHotel
        };

        fetch('http://127.0.0.1:5000/admin/agregar_hotel', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);

            
            if (data.hotel) {
                const hotelesTable = document.getElementById('hoteles-table-body');
                
                const newRow = document.createElement('tr');
                newRow.id = `hotel-row-${data.hotel.id}`;

                newRow.innerHTML = `
                    <td>${data.hotel.id}</td>
                    <td>${data.hotel.nombre}</td>
                `;
                
                hotelesTable.appendChild(newRow);
            }

            document.getElementById('nombre_hotel').value = '';
            document.getElementById('descripcion_hotel').value = '';
            document.getElementById('ubicacion_hotel').value = '';

            const imagenesContainer = document.getElementById("imagenes-container");
            const imagenesInputs = document.querySelectorAll('input[name="imagenes_hotel[]"]');
            imagenesInputs.forEach(input => input.value = '');  
            imagenesContainer.innerHTML = '';  

        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Error al agregar el hotel');
        });
    });
});


function deleteHotel(hotelId) {
    if (confirm("¿Estás seguro de que quieres eliminar este hotel?")) {
        // Enviar una solicitud DELETE a la API para eliminar el hotel
        fetch(`/admin/eliminar_hotel/${hotelId}`, {
            method: 'DELETE',
        })
        .then(response => {
            if (response.ok) {
                alert('Hotel eliminado correctamente');
                // Opcionalmente, puedes recargar la página o eliminar el hotel de la lista
                location.reload(); // Recarga la página para actualizar la lista de hoteles
            } else {
                alert('Hubo un error al eliminar el hotel');
            }
        })
        .catch(error => {
            alert('Error al eliminar el hotel: ' + error);
        });
    }
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
});


document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('form-agregar-servicio');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
       
        const nombreServicio = document.getElementById('nombre_servicio').value;
        const descripcionServicio = document.getElementById('descripcion_servicio').value;
        const urlImagen = document.getElementById('url_imagen').value;
        const ubicacionServicio = document.getElementById('ubicacion_servicio').value;
        

        const data = {
            nombre: nombreServicio,
            descripcion: descripcionServicio,
            url_imagen: urlImagen,
            ubicacion: ubicacionServicio
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