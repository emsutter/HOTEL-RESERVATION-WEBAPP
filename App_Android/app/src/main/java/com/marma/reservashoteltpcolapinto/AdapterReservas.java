package com.marma.reservashoteltpcolapinto;

import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

import java.util.ArrayList;
import java.util.List;

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
            this.categoria.setText(getCategoria(servicio));

            this.cancelar.setOnClickListener(v -> {
                adapter.removeItem(position);
            });
        }

        private String getCategoria(Servicio servicio) {
            for (Categoria categoria : Global.getInstance().categorias) {
                if (categoria.contiene(servicio)) {
                    return categoria.getNombre();
                }
            }
            return "";
        }
    }
}