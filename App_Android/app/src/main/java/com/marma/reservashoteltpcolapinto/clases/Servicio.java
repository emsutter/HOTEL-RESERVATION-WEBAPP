package com.marma.reservashoteltpcolapinto.clases;

import java.util.ArrayList;
import java.util.List;

public class Servicio {
    private int servicio_id;
    private String nombre;
    private String descripcion;
    private String url_imagen;
    private String ubicacion;
    private String categoria;
    private int habilitado;

    public Servicio() {
    }

    public Servicio(int servicio_id, String nombre, String descripcion, String urlImagen, String ubicacion, int habilitado, String categoria) {
        this.servicio_id = servicio_id;
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.url_imagen = urlImagen;
        this.ubicacion = ubicacion;
        this.habilitado = habilitado;
        this.categoria = categoria;
    }

    public int getServicio_id() {
        return servicio_id;
    }

    public void setServicio_id(int servicio_id) {
        this.servicio_id = servicio_id;
    }

    public String getUrl_imagen() {
        return url_imagen;
    }

    public void setUrl_imagen(String url_imagen) {
        this.url_imagen = url_imagen;
    }

    public int getHabilitado() {
        return habilitado;
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
