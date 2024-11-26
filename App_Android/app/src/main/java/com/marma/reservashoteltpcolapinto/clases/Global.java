package com.marma.reservashoteltpcolapinto.clases;

import java.util.ArrayList;
import java.util.List;

public class Global {
    private static Global instance;
    public Categoria categoria;
    public Servicio servicio;
    public List<Categoria> categorias = new ArrayList<>();
    public Usuario usuario = new Usuario("Un mail");

    public static synchronized Global getInstance(){
        if(instance == null)
            instance = new Global();
        return instance;
    }

}
