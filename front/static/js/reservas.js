function submitReserva(event) {
    event.preventDefault(); // Evitar el envío tradicional del formulario

    // Obtener los valores del formulario
    const nombre = document.getElementById('Name').value;
    const email = document.getElementById('Email').value;
    const ingreso = document.getElementById('Ingreso').value;
    const egreso = document.getElementById('Egreso').value;
    const hotelId = document.getElementById('hotel_id').value;

    // Crear el objeto con los datos del formulario
    const formData = {
       Name: nombre,
       Email: email,
       Ingreso: ingreso,
       Egreso: egreso,
       hotel_id: hotelId
    };

    // Enviar los datos al backend usando fetch (AJAX)
    fetch('/admin/agregar_reserva', {
       method: 'POST',
       headers: {
          'Content-Type': 'application/json'  // Indicamos que enviamos JSON
       },
       body: JSON.stringify(formData)  // Convertir el objeto a JSON
    })
    .then(response => response.json())  // Parsear la respuesta como JSON
    .then(data => {
       if (data.success) {
          alert('Reserva realizada con éxito');
          // Opcionalmente, redirigir a otra página o hacer algo más
       } else {
          alert('Hubo un error al procesar la reserva');
       }
    })
    .catch(error => {
       console.error('Error:', error);
       alert('Hubo un problema con el envío de la reserva');
    });
 }

 
 function submitReserva(event) {
   event.preventDefault(); 


   const email = document.getElementById("Email").value;
   const ingreso = document.getElementById("Ingreso").value;
   const egreso = document.getElementById("Egreso").value;
   const hotelId = document.getElementById("hotel_id").value;

 
   if (!email ){
    alert("Por favor, completa todos los campos email.");} if (!ingreso){
        alert("Por favor, completa todos los campos.");}
    
    if (!egreso){
        alert("Por favor, completa todos los campos Egreso.");
    }   
    if (!hotelId) {
       alert("Por favor, completa todos los campos hotel.");
    
       return;
   }

   const data = {
       email: email,
       ingreso: ingreso,
       egreso: egreso,
       hotel_id: hotelId,
   };
   fetch("/admin/agregar_reserva", {
       method: "POST",
       headers: {
           "Content-Type": "application/json",
       },
       body: JSON.stringify(data),
   })
   .then((response) => {
       if (response.ok) {
           return response.json();
       } else {
           throw new Error("Error al enviar la reserva.");
       }
   })
   .then((result) => {
       alert("Reserva creada exitosamente.");
       console.log(result);
   })
   .catch((error) => {
       console.error(error);
       alert("Hubo un problema al crear la reserva.");
   });
}
