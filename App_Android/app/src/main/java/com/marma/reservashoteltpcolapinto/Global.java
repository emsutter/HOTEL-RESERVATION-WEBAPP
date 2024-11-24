package com.marma.reservashoteltpcolapinto;

import java.util.ArrayList;
import java.util.List;

public class Global {
    private static Global instance;
    public Categoria categoria;
    public Servicio servicio;
    public List<Categoria> categorias = new ArrayList<>();
    public Usuario usuario = new Usuario("Un mail", new Servicio("Montana", "Una descripcion", "", "Tucumán 451, C1049 Cdad. Autónoma de Buenos Aires", true));
    public static synchronized Global getInstance(){
        if(instance == null)
            instance = new Global();
        return instance;
    }

}
