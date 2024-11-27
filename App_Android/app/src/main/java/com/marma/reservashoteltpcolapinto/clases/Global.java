package com.marma.reservashoteltpcolapinto.clases;

import com.marma.reservashoteltpcolapinto.AdapterReservas;

import java.util.ArrayList;
import java.util.List;

public class Global {
    private static Global instance;
    public Categoria categoria;
    public Servicio servicio;
    public Reserva reserva;
    public List<Categoria> categorias = new ArrayList<>();
    public Usuario usuario = new Usuario("");
    public AdapterReservas adapterReservas;

    public static synchronized Global getInstance(){
        if(instance == null)
            instance = new Global();
        return instance;
    }

    public void notificarCambiosAdapterReservas(){
        if(adapterReservas !=null){
            adapterReservas.notifyDataSetChanged();
        }
    }

}
