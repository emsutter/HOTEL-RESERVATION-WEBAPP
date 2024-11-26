package com.marma.reservashoteltpcolapinto.clases;

import java.util.ArrayList;
import java.util.List;

public class Servicio {
    private String nombre;
    private String descripcion;
    private String url_imagen;
    private String ubicacion;
    private String categoria;
    private int habilitado;

    public Servicio() {
    }

    public Servicio(String nombre, String descripcion, String urlImagen, String ubicacion, int habilitado, String categoria) {
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.url_imagen = urlImagen;
        this.ubicacion = ubicacion;
        this.habilitado = habilitado;
        this.categoria = categoria;
    }

    public String getUrlImagen() {
        return url_imagen;
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

    public int isHabilitado() {
        return habilitado;
    }


    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public void setUrlImagen(String urlImagen) {
        this.url_imagen = urlImagen;
    }

    public void setUbicacion(String ubicacion) {
        this.ubicacion = ubicacion;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public void setHabilitado(int habilitado) {
        this.habilitado = habilitado;
    }
}
