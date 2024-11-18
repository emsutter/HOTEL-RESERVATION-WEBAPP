package com.marma.reservashoteltpcolapinto;

import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.marma.reservashoteltpcolapinto.databinding.FragmentServiciosBinding;


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

        return binding.getRoot();
    }
}