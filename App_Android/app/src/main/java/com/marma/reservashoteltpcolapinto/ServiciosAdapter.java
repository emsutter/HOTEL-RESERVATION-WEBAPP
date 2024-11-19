package com.marma.reservashoteltpcolapinto;

import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.recyclerview.widget.RecyclerView;
import com.bumptech.glide.Glide;

import java.util.ArrayList;
import java.util.List;

public class ServiciosAdapter extends RecyclerView.Adapter<ServiciosAdapter.VerServiciosViewHolder> {

    private List<Servicio> serviciosList;
    private List<Servicio> filteredServiciosList;

    // Constructor
    public ServiciosAdapter(List<Servicio> serviciosList) {
        this.serviciosList = serviciosList;
        this.filteredServiciosList = new ArrayList<>(serviciosList);
    }

    @NonNull
    @Override
    public VerServiciosViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_servicio, parent, false);
        return new VerServiciosViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(@NonNull VerServiciosViewHolder holder, int position) {
        Servicio servicio = filteredServiciosList.get(position);
        holder.bind(servicio);
    }


    @Override
    public int getItemCount() {
        return filteredServiciosList.size();
    }


    public void filter(String query) {
        filteredServiciosList.clear();
        if (query.isEmpty()) {
            filteredServiciosList.addAll(serviciosList);
        } else {
            for (Servicio servicio : serviciosList) {
                if (servicio.getNombre().toLowerCase().contains(query.toLowerCase())) {
                    filteredServiciosList.add(servicio);
                }
            }
        }
        notifyDataSetChanged();
    }

    // ViewHolder
    static class VerServiciosViewHolder extends RecyclerView.ViewHolder {
        ImageView imagen;
        TextView nombre;

        VerServiciosViewHolder(View itemView) {
            super(itemView);
            this.imagen = itemView.findViewById(R.id.imagen);
            this.nombre = itemView.findViewById(R.id.nombre);
        }

        void bind(Servicio servicio) {
            this.nombre.setText(servicio.getNombre());
            Glide.with(this.itemView.getContext())
                    .load(servicio.getUrlImagen())
                    .into(this.imagen);

            this.itemView.setOnClickListener(v -> {
                Global.getInstance().servicio = servicio;
                Intent intent = new Intent(this.itemView.getContext(), ServicioActivity.class);
                this.itemView.getContext().startActivity(intent);
            });
        }
    }
}
