package com.marma.reservashoteltpcolapinto.fragments;

import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;

import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.marma.reservashoteltpcolapinto.Adapter;
import com.marma.reservashoteltpcolapinto.clases.Categoria;
import com.marma.reservashoteltpcolapinto.clases.Global;
import com.marma.reservashoteltpcolapinto.clases.Servicio;
import com.marma.reservashoteltpcolapinto.databinding.FragmentServiciosBinding;

import java.util.ArrayList;
import java.util.List;

public class ServiciosFragment extends Fragment {

    private FragmentServiciosBinding binding;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        binding = FragmentServiciosBinding.inflate(inflater, container, false);
        initUI();

        return binding.getRoot();
    }

    private void initUI() {
        List<Categoria> categorias = Global.getInstance().categorias;

        Adapter adapter = new Adapter(categorias);
        binding.recyclerView.setAdapter(adapter);
        binding.recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));

        binding.buscarServicio.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {}

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

                adapter.filter(s.toString());
            }

            @Override
            public void afterTextChanged(Editable s) {
            }
        });
    }
}