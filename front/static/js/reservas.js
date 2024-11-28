    // Busca las habitaciones disponibles para un hotel y las muestra en el selector de reservas

document.addEventListener("DOMContentLoaded", function () {
    const hotelSelect = document.getElementById('hotel_id');
    const habitacionSelect = document.getElementById('habitacion_id');

    hotelSelect.addEventListener('change', function () {
        const hotelId = this.value;
        fetch(`/admin/obtener_habitaciones/${hotelId}`)
            .then(response => response.json())
            .then(data => {
                console.log('Rooms fetched:', data);
                habitacionSelect.innerHTML = '<option value="" disabled selected>Selecciona una habitación</option>';
                if (Array.isArray(data)) {
                    data.forEach(habitacion => {
                        const option = document.createElement('option');
                        option.value = habitacion.habitacion_id;
                        option.textContent = `Habitación ${habitacion.habitacion_id} - Capacidad: ${habitacion.capacidad}`;
                        habitacionSelect.appendChild(option);
                    });
                } else {
                    console.error('Expected an array but got:', data);
                }
            })
            .catch(error => {
                console.error('Error fetching habitaciones:', error);
            });
    });
});

    // Crea una reserva con los datos ingresados en el formulario

function submitReserva(event) {
    event.preventDefault();

    const email = document.getElementById('Email').value;
    const ingreso = document.getElementById('Ingreso').value;
    const egreso = document.getElementById('Egreso').value;
    const hotelId = document.getElementById('hotel_id').value;
    const habitacionId = document.getElementById('habitacion_id').value;

    if (!email || !ingreso || !egreso || !hotelId || !habitacionId) {
        alert('Por favor, completa todos los campos.');
        return;
    }

    const data = {
        email: email,
        ingreso: ingreso,
        egreso: egreso,
        hotel_id: hotelId,
        habitacion_id: habitacionId
    };

    fetch('/admin/agregar_reserva', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(result => {
            if (result.success) {
                alert('Reserva creada exitosamente.');
                const form = document.getElementById('request');
                form.reset();
            } else {
                alert('Hubo un problema al crear la reserva.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Hubo un problema al crear la reserva.');
        });
}
