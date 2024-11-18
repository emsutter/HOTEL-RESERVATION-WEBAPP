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

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityServicioBinding.inflate(getLayoutInflater());
    }
}