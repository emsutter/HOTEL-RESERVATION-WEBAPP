package com.marma.reservashoteltpcolapinto;
import com.marma.reservashoteltpcolapinto.clases.Servicio;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

import java.util.List;

public interface ApiService {
    @GET("admin/obtener_servicios_reserva/{id_reserva}")
    Call<List<Servicio>> obtenerServiciosReserva(@Path("id_reserva") String idReserva);

    @GET("/admin/obtener_servicios")
    Call<List<Servicio>> obtenerServicios();
    
}

