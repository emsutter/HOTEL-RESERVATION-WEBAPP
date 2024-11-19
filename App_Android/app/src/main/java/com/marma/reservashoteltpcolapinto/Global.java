package com.marma.reservashoteltpcolapinto;

public class Global {
    private static Global instance;
    public Servicio servicio;
    public static synchronized Global getInstance(){
        if(instance == null)
            instance = new Global();
        return instance;
    }
}
