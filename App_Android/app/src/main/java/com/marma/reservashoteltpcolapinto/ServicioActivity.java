package com.marma.reservashoteltpcolapinto;

import android.graphics.Color;
import android.location.Address;
import android.location.Geocoder;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import com.bumptech.glide.Glide;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import androidx.appcompat.app.AppCompatActivity;

import com.marma.reservashoteltpcolapinto.clases.Global;
import com.marma.reservashoteltpcolapinto.clases.Reserva;
import com.marma.reservashoteltpcolapinto.clases.ReservaServicioRequest;
import com.marma.reservashoteltpcolapinto.clases.Servicio;
import com.marma.reservashoteltpcolapinto.clases.Usuario;
import com.marma.reservashoteltpcolapinto.databinding.ActivityServicioBinding;

import java.io.IOException;
import java.util.List;
import java.util.Locale;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

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
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

        this.binding.descripcion.setText(servicio.getDescripcion());
        this.binding.ll.nombre.setText(servicio.getNombre());
        Glide.with(this)
                .load(this.servicio.getUrlImagen())
                .into(this.binding.ll.imagen);


        if(this.usuario.contratoSerivico(this.servicio)){
            cambiarColorBoton(true);
        }

        this.binding.contratar.setOnClickListener(v -> {
            this.binding.progress.setVisibility(View.VISIBLE);
            this.binding.contratar.setVisibility(View.GONE);
            if(this.usuario.contratoSerivico(this.servicio)){
                this.usuario.deleteServicio(servicio);
                cambiarColorBoton(false);
                agregarABaseDeDatos(servicio.getServicio_id(), true);
            }
            else{
                this.usuario.addServicio(servicio);
                agregarABaseDeDatos(servicio.getServicio_id(), false);
                cambiarColorBoton(true);
            }
            Global.getInstance().notificarCambiosAdapterReservas();
        });
    }

    private void agregarABaseDeDatos(int id, boolean borrar){
        ApiService apiService = RetrofitClient.getApiService();
        ReservaServicioRequest reservaServicioRequest = new ReservaServicioRequest(Global.getInstance().reserva.getReservas_id(), id);
        Call<Void> call;
        if(borrar){
            call = apiService.eliminarServicioReserva(id, Global.getInstance().reserva.getReservas_id());
        }
        else{
             call = apiService.crearReservaServicio(reservaServicioRequest);
        }
        call.enqueue(new Callback<Void>() {
            @Override
            public void onResponse(Call<Void> call, Response<Void> response) {
                if (response.isSuccessful()) {
                    if(borrar){
                        Toast.makeText(getApplicationContext(), "Reserva borrada exitosamente", Toast.LENGTH_SHORT).show();
                    }
                    else{
                        Toast.makeText(getApplicationContext(), "Reserva creada exitosamente", Toast.LENGTH_SHORT).show();
                    }

                } else {
                    // Obtener detalles del error
                    String errorMessage = "Código de error: " + response.code();
                    try {
                        if (response.errorBody() != null) {
                            errorMessage += "\n" + response.errorBody().string();
                        }
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    Log.e("API", errorMessage);
                    Toast.makeText(getApplicationContext(), "No se pudo crear la reserva: " + errorMessage, Toast.LENGTH_LONG).show();
                }
                binding.progress.setVisibility(View.GONE);
                binding.contratar.setVisibility(View.VISIBLE);
            }

            @Override
            public void onFailure(Call<Void> call, Throwable t) {
                Toast.makeText(getApplicationContext(), "Error de conexión: " + t.getMessage(), Toast.LENGTH_SHORT).show();
                binding.progress.setVisibility(View.GONE);
                binding.contratar.setVisibility(View.VISIBLE);
            }
        });
    }


    private void cambiarColorBoton(boolean contratado){
        if(contratado){
            this.binding.contratar.setText("Cancelar");
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