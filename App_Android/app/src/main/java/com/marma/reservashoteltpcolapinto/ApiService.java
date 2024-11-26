package com.marma.reservashoteltpcolapinto;
import com.marma.reservashoteltpcolapinto.clases.Reserva;
import com.marma.reservashoteltpcolapinto.clases.ReservaServicioRequest;
import com.marma.reservashoteltpcolapinto.clases.Servicio;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;
import retrofit2.http.Query;

import java.util.List;

public interface ApiService {

    @GET("admin/obtener_reserva/{id_reserva}")
    Call<Reserva> obtenerReserva(@Path("id_reserva") int idReserva);

    @GET("admin/obtener_servicios_reserva/{id_reserva}")
    Call<List<Servicio>> obtenerServiciosReserva(@Path("id_reserva") int idReserva);

    @GET("/admin/obtener_servicios")
    Call<List<Servicio>> obtenerServicios();

    @POST("/admin/crear_reserva_servicio")
    Call<Void> crearReservaServicio(@Body ReservaServicioRequest reservaServicioRequest);

    @DELETE("/admin/eliminar_servicio_reserva/{id_servicio}/{id_reserva}")
    Call<Void> eliminarServicioReserva(
            @Path("id_servicio") int idServicio,
            @Path("id_reserva") int idReserva
    );

}

