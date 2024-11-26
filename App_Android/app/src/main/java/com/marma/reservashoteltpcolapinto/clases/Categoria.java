package com.marma.reservashoteltpcolapinto.clases;

import java.util.ArrayList;
import java.util.List;

public class Categoria {
    private String nombre;
    private String urlImagen;
    private List<Servicio> servicioList;

    public Categoria(String nombre, String urlImagen){
        this.nombre = nombre;
        this.urlImagen = urlImagen;
        this.servicioList = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public String getUrlImagen() {
        return urlImagen;
    }

    public void addSerivicio(Servicio servicio){
        this.servicioList.add(servicio);
    }

    public List<Servicio> getServicioList() {
        return servicioList;
    }

    public boolean contiene(Servicio servicio){
        return this.servicioList.contains(servicio);
    }
}
