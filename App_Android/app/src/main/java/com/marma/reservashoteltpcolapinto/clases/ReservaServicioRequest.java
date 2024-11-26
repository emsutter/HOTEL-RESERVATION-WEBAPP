package com.marma.reservashoteltpcolapinto.clases;

public class ReservaServicioRequest {
    private int id_reserva;
    private int id_servicio;

    public ReservaServicioRequest(int id_reserva, int id_servicio) {
        this.id_reserva = id_reserva;
        this.id_servicio = id_servicio;
    }

    // Getters y Setters
    public int getId_reserva() {
        return id_reserva;
    }

    public void setId_reserva(int id_reserva) {
        this.id_reserva = id_reserva;
    }

    public int getId_servicio() {
        return id_servicio;
    }

    public void setId_servicio(int id_servicio) {
        this.id_servicio = id_servicio;
    }
}

