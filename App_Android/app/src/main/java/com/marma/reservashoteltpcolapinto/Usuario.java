package com.marma.reservashoteltpcolapinto;

import java.util.ArrayList;
import java.util.List;

public class Usuario {
    private String mail;
    private List<Servicio> servicios;

    public Usuario(String mail, Servicio servicio){
        this.mail = mail;
        this.servicios = new ArrayList<>();
        this.servicios.add(servicio);
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
        return this.servicios.contains(servicio);
    }
}
