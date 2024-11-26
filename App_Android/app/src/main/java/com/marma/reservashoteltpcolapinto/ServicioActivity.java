package com.marma.reservashoteltpcolapinto;

import android.graphics.Color;
import android.location.Address;
import android.location.Geocoder;
import android.os.Bundle;

import com.bumptech.glide.Glide;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import androidx.appcompat.app.AppCompatActivity;

import com.marma.reservashoteltpcolapinto.clases.Global;
import com.marma.reservashoteltpcolapinto.clases.Servicio;
import com.marma.reservashoteltpcolapinto.clases.Usuario;
import com.marma.reservashoteltpcolapinto.databinding.ActivityServicioBinding;

import java.io.IOException;
import java.util.List;
import java.util.Locale;

public class ServicioActivity extends AppCompatActivity implements OnMapReadyCallback {
    private GoogleMap mMap;
    private ActivityServicioBinding binding;
    private Servicio servicio;
    private Usuario usuario;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        this.binding = ActivityServicioBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        this.servicio = Global.getInstance().servicio;
        this.usuario = Global.getInstance().usuario;
        initUI();
    }

    private void initUI() {
        this.binding.descripcion.setText(servicio.getDescripcion());
        this.binding.ll.nombre.setText(servicio.getNombre());
        Glide.with(this)
                .load(this.servicio.getUrlImagen())
                .into(this.binding.ll.imagen);


        if(this.usuario.contratoSerivico(this.servicio)){
            cambiarColorBoton(true);
        }

        this.binding.contratar.setOnClickListener(v -> {
            if(this.usuario.contratoSerivico(this.servicio)){
                this.usuario.deleteServicio(servicio);
                cambiarColorBoton(true);
            }
            else{
                this.usuario.addServicio(servicio);
                this.usuario.addServicio(servicio);
                cambiarColorBoton(false);
            }
        });
    }

    private void cambiarColorBoton(boolean contratado){
        if(contratado){
            this.binding.contratar.setText("Anular");
            this.binding.contratar.setBackgroundColor(Color.RED);
        }
        else{
            this.binding.contratar.setText("Contratar");
            this.binding.contratar.setBackgroundColor(getResources().getColor(R.color.primary));
        }

    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        this.mMap = googleMap;
        showUbicacion();
    }

    private void showUbicacion() {
        Geocoder geocoder = new Geocoder(this, Locale.getDefault());
        String ubicacion = this.servicio.getUbicacion();
        try {
            List<Address> addresses = geocoder.getFromLocationName(ubicacion, 1);
            if (addresses != null && !addresses.isEmpty()) {
                Address address = addresses.get(0);
                LatLng location = new LatLng(address.getLatitude(), address.getLongitude());

                this.mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(location, 10));
                this.mMap.addMarker(new MarkerOptions().position(location).title(ubicacion));
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}