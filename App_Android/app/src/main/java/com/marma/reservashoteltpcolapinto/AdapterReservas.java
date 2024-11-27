package com.marma.reservashoteltpcolapinto;

import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.marma.reservashoteltpcolapinto.clases.Categoria;
import com.marma.reservashoteltpcolapinto.clases.Global;
import com.marma.reservashoteltpcolapinto.clases.ReservaServicioRequest;
import com.marma.reservashoteltpcolapinto.clases.Servicio;

import java.io.IOException;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class AdapterReservas extends RecyclerView.Adapter<AdapterReservas.ViewHolder> {

    private List<Servicio> list;

    // Constructor
    public AdapterReservas(List<Servicio> list) {
        this.list = list;
    }

    @NonNull
    @Override
    public AdapterReservas.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_servicio, parent, false);
        return new AdapterReservas.ViewHolder(itemView);
    }

    @Override
    public int getItemCount() {
        return list.size();
    }

    // ViewHolder
    public void removeItem(int position) {
        list.remove(position);
        notifyItemRemoved(position);
        notifyItemRangeChanged(position, list.size()); // Opcional para actualizar los índices
    }

    @Override
    public void onBindViewHolder(@NonNull AdapterReservas.ViewHolder holder, int position) {
        Servicio object = list.get(position);
        holder.bind(object, position, this);
    }

    // Modificar el ViewHolder
    static class ViewHolder extends RecyclerView.ViewHolder {
        ImageView imagen;
        TextView nombre;
        TextView categoria;
        TextView cancelar;

        ViewHolder(View itemView) {
            super(itemView);
            this.imagen = itemView.findViewById(R.id.imagen);
            this.nombre = itemView.findViewById(R.id.nombre);
            this.categoria = itemView.findViewById(R.id.categoria);
            this.cancelar = itemView.findViewById(R.id.cancelar);
        }

        void bind(Servicio servicio, int position, AdapterReservas adapter) {
            Glide.with(this.itemView.getContext())
                    .load(servicio.getUrlImagen())
                    .into(this.imagen);

            this.nombre.setText(servicio.getNombre());
            this.categoria.setText(servicio.getCategoria());

            this.cancelar.setOnClickListener(v -> {
                adapter.removeItem(position);
                removerDeBaseDeDatos(servicio.getServicio_id(), this.itemView.getContext());
            });
        }

        private void removerDeBaseDeDatos(int id, Context context){
            ApiService apiService = RetrofitClient.getApiService();
            Call<Void> call;

            call = apiService.eliminarServicioReserva(id, Global.getInstance().reserva.getReservas_id());

            call.enqueue(new Callback<Void>() {
                @Override
                public void onResponse(Call<Void> call, Response<Void> response) {
                    if (response.isSuccessful()) {
                            Toast.makeText(context, "Reserva borrada exitosamente", Toast.LENGTH_SHORT).show();
                    } else {
                        // Obtener detalles del error
                        String errorMessage = "Código de error: " + response.code();
                        try {
                            if (response.errorBody() != null) {
                                errorMessage += "\n" + response.errorBody().string();
                            }
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        Log.e("API", errorMessage);
                        Toast.makeText(context, "No se pudo crear la reserva: " + errorMessage, Toast.LENGTH_LONG).show();
                    }
                }

                @Override
                public void onFailure(Call<Void> call, Throwable t) {
                    Toast.makeText(context, "Error de conexión: " + t.getMessage(), Toast.LENGTH_SHORT).show();
                }
            });
        }
    }
}