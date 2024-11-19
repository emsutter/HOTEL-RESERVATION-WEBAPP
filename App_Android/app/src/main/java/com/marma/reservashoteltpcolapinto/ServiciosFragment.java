package com.marma.reservashoteltpcolapinto;

import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;

import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

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
        List<Servicio> serviciosList = new ArrayList<>();

        String url = "https://media.istockphoto.com/id/1324283285/es/foto/ciervos-mulos-de-las-montañas-rocosas-vadeando-en-el-lago-al-atardecer.jpg?s=612x612&w=0&k=20&c=Lv8KwJTep66Dt4mwYphQHQBJkzlVTeO28ixb5h6fa4s=";
        String nombre = "Excursiones";
        serviciosList.add(new Servicio(url, nombre));

        url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8qCH2yT7EYH-DZPXPWiSoSZKAdb_q6xY9Qg&s";
        nombre = "spa";
        serviciosList.add(new Servicio(url, nombre));

        url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_Nr0WT6H41xKTW3D_-ZJzQm0eyBxEVq4SPw&s";
        nombre = "pileta";
        serviciosList.add(new Servicio(url, nombre));

        ServiciosAdapter adapter = new ServiciosAdapter(serviciosList);
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