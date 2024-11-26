package com.marma.reservashoteltpcolapinto.clases;

import java.util.Date;

public class Reserva {
    private int reservas_id;
    private String email;
    private Date fecha_ingreso;
    private Date fecha_egreso;
    private int hotel_id;
    private int habilitado;

    public Reserva(int reservas_id, String email, Date fecha_ingreso, Date fecha_egreso, int hotel_id, int habilitado) {
        this.reservas_id = reservas_id;
        this.email = email;
        this.fecha_ingreso = fecha_ingreso;
        this.fecha_egreso = fecha_egreso;
        this.hotel_id = hotel_id;
        this.habilitado = habilitado;
    }

    public Reserva() {
    }

    public int getReservas_id() {
        return reservas_id;
    }

    public void setReservas_id(int reserva_id) {
        this.reservas_id = reserva_id;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Date getFecha_ingreso() {
        return fecha_ingreso;
    }

    public void setFecha_ingreso(Date fecha_ingreso) {
        this.fecha_ingreso = fecha_ingreso;
    }

    public Date getFecha_egreso() {
        return fecha_egreso;
    }

    public void setFecha_egreso(Date fecha_egreso) {
        this.fecha_egreso = fecha_egreso;
    }

    public int getHotel_id() {
        return hotel_id;
    }

    public void setHotel_id(int hotel_id) {
        this.hotel_id = hotel_id;
    }

    public int getHabilitado() {
        return habilitado;
    }

    public void setHabilitado(int habilitado) {
        this.habilitado = habilitado;
    }
}
