package com.marma.reservashoteltpcolapinto.clases;

import java.util.ArrayList;
import java.util.List;

public class Usuario {
    private String mail;
    private List<Servicio> servicios;

    public Usuario(String mail){
        this.mail = mail;
        this.servicios = new ArrayList<>();
    }

    public void addServicio(Servicio servicio){
        this.servicios.add(servicio);
    }
    public void deleteServicio(Servicio servicio){
        this.servicios.remove(servicio);
    }

    public List<Servicio> getServicios(){
        return this.servicios;
    }

    public boolean contratoSerivico(Servicio servicio){
        for(Servicio servicioAux : servicios){
            if(servicio.getNombre().equals(servicioAux.getNombre()) && servicio.getCategoria().equals(servicioAux.getCategoria()))
                return true;
        }
        return false;
    }
}
