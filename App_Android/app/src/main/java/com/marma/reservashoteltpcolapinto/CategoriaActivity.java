package com.marma.reservashoteltpcolapinto;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.marma.reservashoteltpcolapinto.databinding.ActivityCategoriaBinding;
import com.marma.reservashoteltpcolapinto.databinding.ActivityServicioBinding;

public class CategoriaActivity extends AppCompatActivity {

    private ActivityCategoriaBinding binding;
    private Categoria categoria;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.binding = ActivityCategoriaBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        this.categoria = Global.getInstance().categoria;
        setView();
    }

    private void setView() {
        this.binding.nombreCategoria.setText(this.categoria.getNombre());
        Adapter adapter = new Adapter(categoria.getServicioList());
        binding.recyclerView.setAdapter(adapter);
        binding.recyclerView.setLayoutManager(new LinearLayoutManager(this));
    }
}