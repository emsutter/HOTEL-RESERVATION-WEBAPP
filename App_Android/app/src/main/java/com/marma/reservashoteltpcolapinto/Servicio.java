package com.marma.reservashoteltpcolapinto;

public class Servicio {
    private String urlImagen;
    private String nombre;

    public Servicio(){

    }

    public Servicio(String urlImagen, String nombre){
        this.urlImagen = urlImagen;
        this.nombre = nombre;
    }

    public String getUrlImagen() {
        return urlImagen;
    }

    public String getNombre() {
        return nombre;
    }
}
