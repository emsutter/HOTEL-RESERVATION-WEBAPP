let map;
let marker;

   // Inicializa el mapa

function initMap() {
   const defaultLocation = { lat: -34.6037, lng: -58.3816 };

   map = new google.maps.Map(document.getElementById("map"), {
      zoom: 12,
      center: defaultLocation,
   });

   marker = new google.maps.Marker({
      position: defaultLocation,
      map: map,
   });

   const hotelSelect = document.getElementById("hotel_id");

   const selectedOption = hotelSelect.options[hotelSelect.selectedIndex];
   if (selectedOption && selectedOption.value) {
      const ubicacion = selectedOption.getAttribute("data-ubicacion");
      if (ubicacion) {
            geocodeAddress(ubicacion); 
      }
   }

   hotelSelect.addEventListener("change", updateMap);
}

   // Actualiza el mapa cuando se selecciona un hotel

function updateMap() {
   const hotelSelect = document.getElementById("hotel_id");
   const selectedOption = hotelSelect.options[hotelSelect.selectedIndex];
   const ubicacion = selectedOption.getAttribute("data-ubicacion");

   if (ubicacion) {
      geocodeAddress(ubicacion);
   }
}
   // Busca la dirección en el mapa y centra el mapa en esa dirección

function geocodeAddress(address) {
   const geocoder = new google.maps.Geocoder();

   geocoder.geocode({ address: address }, function (results, status) {
      if (status === google.maps.GeocoderStatus.OK) {
            const location = results[0].geometry.location;
            map.setCenter(location);
            marker.setPosition(location);
      } else {
            alert("No se pudo encontrar la dirección: " + status);
      }
   });
}
