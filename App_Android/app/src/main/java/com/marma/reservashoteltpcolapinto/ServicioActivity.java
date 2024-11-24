package com.marma.reservashoteltpcolapinto;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.marma.reservashoteltpcolapinto.databinding.ActivityServicioBinding;

public class ServicioActivity extends AppCompatActivity {

    private ActivityServicioBinding binding;
    private Servicio servicio;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.binding = ActivityServicioBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        this.servicio = Global.getInstance().servicio;
        setView();
    }

    private void setView() {
        this.binding.nombreServicio.setText(this.servicio.getNombre());
    }
}