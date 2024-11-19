package com.marma.reservashoteltpcolapinto;

import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.marma.reservashoteltpcolapinto.databinding.FragmentContactoBinding;

public class ReservasFragment extends Fragment {

    private FragmentContactoBinding binding;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        binding = FragmentContactoBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }
}