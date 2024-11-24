package com.marma.reservashoteltpcolapinto;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.marma.reservashoteltpcolapinto.databinding.ActivityIniciarSesionBinding;

public class IniciarSesionActivity extends AppCompatActivity {

    private ActivityIniciarSesionBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityIniciarSesionBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        setListeners();
    }

    private void setListeners(){
        binding.ingresar.setOnClickListener(v -> {
            String mail = binding.mail.getText().toString();
            if(mail.equals("tp@colapinto.com")){
                Toast.makeText(this, "Mail invalido", Toast.LENGTH_SHORT).show();
            }
            else {
                Intent intent = new Intent(IniciarSesionActivity.this, MainActivity.class);
                startActivity(intent);
                finish();
            }
        });
    }
}