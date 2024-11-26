package com.marma.reservashoteltpcolapinto;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;


import com.marma.reservashoteltpcolapinto.clases.Categoria;
import com.marma.reservashoteltpcolapinto.clases.Global;
import com.marma.reservashoteltpcolapinto.clases.Reserva;
import com.marma.reservashoteltpcolapinto.clases.Servicio;
import com.marma.reservashoteltpcolapinto.databinding.ActivityIniciarSesionBinding;

import java.io.IOException;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class IniciarSesionActivity extends AppCompatActivity {

    private ActivityIniciarSesionBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityIniciarSesionBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        RetrofitClient.getApiService();
        setListeners();

    }

    private void setListeners(){
        binding.ingresar.setOnClickListener(v -> {
            int idReserva = Integer.parseInt(binding.mail.getText().toString());
            binding.progressBar.setVisibility(View.VISIBLE);
            binding.ingresar.setVisibility(View.GONE);
            obtenerReserva(idReserva);
        });
    }

    private void obtenerReserva(int id){
        ApiService apiService = RetrofitClient.getApiService();
        apiService.obtenerReserva(id).enqueue(new Callback<Reserva>() {
            @Override
            public void onResponse(Call<Reserva> call, Response<Reserva> response) {
                if (response.isSuccessful() && response.body() != null) {
                    Global.getInstance().reserva = response.body();
                    obtenerServiciosPorReserva(Global.getInstance().reserva.getReservas_id());
                    obtenerServicios();
                }
                else{
                    Toast.makeText(IniciarSesionActivity.this, "No se encontre una reserva con el ID ingresado.", Toast.LENGTH_SHORT).show();
                    binding.progressBar.setVisibility(View.GONE);
                    binding.ingresar.setVisibility(View.VISIBLE);
                }
            }

            @Override
            public void onFailure(Call<Reserva> call, Throwable t) {
                Toast.makeText(IniciarSesionActivity.this, "Error: " + t, Toast.LENGTH_SHORT).show();
                binding.progressBar.setVisibility(View.GONE);
                binding.ingresar.setVisibility(View.VISIBLE);
            }
        });
    }

    private void obtenerServicios(){
        ApiService apiService = RetrofitClient.getApiService();
        apiService.obtenerServicios().enqueue(new Callback<List<Servicio>>() {
            @Override
            public void onResponse(Call<List<Servicio>> call, Response<List<Servicio>> response) {
                if (response.isSuccessful() && response.body() != null) {
                    List<Servicio> servicios = response.body();
                    if (servicios.isEmpty()) {
                        Log.d("API_RESPONSE", "No se encontraron servicios para esta reserva");
                    } else {
                        for (Servicio servicio : servicios) {
                            Log.e("URLS", servicio.getUrlImagen());
                            if(!categoriaExiste(servicio)){
                                Categoria categoriAux = new Categoria(servicio.getCategoria(), servicio.getUrlImagen());
                                categoriAux.addSerivicio(servicio);
                                Global.getInstance().categorias.add(categoriAux);
                            }
                            Intent intent = new Intent(IniciarSesionActivity.this, MainActivity.class);
                            startActivity(intent);
                            finish();
                        }
                    }
                } else {
                    Log.e("API_ERROR", "Código de error: " + response.code());
                }
            }
            @Override
            public void onFailure(Call<List<Servicio>> call, Throwable t) {
                Log.e("ERROR API FETCH", t.getMessage());
            }
        });
    }

    private void obtenerServiciosPorReserva(int idReserva){
        ApiService apiService = RetrofitClient.getApiService();
        apiService.obtenerServiciosReserva(idReserva).enqueue(new Callback<List<Servicio>>() {
            @Override
            public void onFailure(Call<List<Servicio>> call, Throwable t) {
                Log.e("API_ERROR", "Error: " + t.getMessage());
            }

            @Override
            public void onResponse(Call<List<Servicio>> call, Response<List<Servicio>> response) {
                if (response.isSuccessful() && response.body() != null) {
                    List<Servicio> servicios = response.body();
                    if (servicios.isEmpty()) {
                        Log.d("API_RESPONSE", "No se encontraron servicios para esta reserva");
                    } else {
                        for (Servicio servicio : servicios) {
                            Global.getInstance().usuario.addServicio(servicio);
                        }
                    }
                } else {
                    Log.e("API_ERROR", "Código de error: " + response.code());
                }
            }

        });
    }

    private boolean categoriaExiste(Servicio servicio){
        for(Categoria categoria : Global.getInstance().categorias){
            if(categoria.getNombre().equals(servicio.getCategoria())){
                categoria.addSerivicio(servicio);
                return true;
            }
        }
       return false;
    }
}