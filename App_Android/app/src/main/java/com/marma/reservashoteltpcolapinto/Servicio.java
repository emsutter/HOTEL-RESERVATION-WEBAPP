package com.marma.reservashoteltpcolapinto;

import java.util.ArrayList;
import java.util.List;

public class Servicio {
    private String nombre;
    private String descripcion;
    private String urlImagen;
    private String ubicacion;
    private boolean habilitado;

    public Servicio(String nombre, String descripcion, String urlImagen, String ubicacion, boolean habilitado) {
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.urlImagen = urlImagen;
        this.ubicacion = ubicacion;
        this.habilitado = habilitado;
    }

    public String getUrlImagen() {
        return urlImagen;
    }

    public String getNombre() {
        return nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public String getUbicacion() {
        return ubicacion;
    }

    public boolean isHabilitado() {
        return habilitado;
    }
}
