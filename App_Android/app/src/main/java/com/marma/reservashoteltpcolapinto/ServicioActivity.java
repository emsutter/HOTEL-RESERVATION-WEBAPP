package com.marma.reservashoteltpcolapinto;

import android.content.Intent;
import android.location.Address;
import android.location.Geocoder;
import android.net.Uri;
import android.os.Bundle;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapView;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;

import android.view.View;

import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import com.marma.reservashoteltpcolapinto.databinding.ActivityServicioBinding;

import java.io.IOException;
import java.util.List;
import java.util.Locale;

public class ServicioActivity extends AppCompatActivity implements OnMapReadyCallback {
    private GoogleMap mMap;
    private ActivityServicioBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityServicioBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

    }


    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        showUbicacion();
    }

    private void showUbicacion() {
        Geocoder geocoder = new Geocoder(this, Locale.getDefault());
        String ubicacion = Global.getInstance().servicio.getUbicacion();
        try {
            List<Address> addresses = geocoder.getFromLocationName(ubicacion, 1);
            if (addresses != null && !addresses.isEmpty()) {
                Address address = addresses.get(0);
                LatLng location = new LatLng(address.getLatitude(), address.getLongitude());

                mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(location, 10));
                mMap.addMarker(new MarkerOptions().position(location).title(ubicacion));
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

}