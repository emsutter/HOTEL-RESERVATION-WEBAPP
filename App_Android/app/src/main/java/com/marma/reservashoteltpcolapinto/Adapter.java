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
import com.marma.reservashoteltpcolapinto.clases.Categoria;
import com.marma.reservashoteltpcolapinto.clases.Global;
import com.marma.reservashoteltpcolapinto.clases.Servicio;

import java.util.ArrayList;
import java.util.List;

public class Adapter<T> extends RecyclerView.Adapter<Adapter.ViewHolder> {

    private List<T> list;
    private List<T> filteredList;

    // Constructor
    public Adapter(List<T> list) {
        this.list = list;
        this.filteredList = new ArrayList<>(list);
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_imagen_nombre, parent, false);
        return new ViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        T object = filteredList.get(position);
        holder.bind(object);
    }

    @Override
    public int getItemCount() {
        return filteredList.size();
    }

    public void filter(String query) {
        this.filteredList.clear();
        if (query.isEmpty()) {
            this.filteredList.addAll(this.list);
        } else {
            for (T object: this.list) {
                if (object instanceof Categoria) {
                    if (((Categoria)object).getNombre().toLowerCase().contains(query.toLowerCase())) {
                        this.filteredList.add(object);
                    }
                } else if (object instanceof Servicio) {
                    if (((Servicio)object).getNombre().toLowerCase().contains(query.toLowerCase())) {
                        this.filteredList.add(object);
                    }
                }
            }
        }
        notifyDataSetChanged();
    }

    // ViewHolder
    static class ViewHolder extends RecyclerView.ViewHolder {
        ImageView imagen;
        TextView nombre;

        ViewHolder(View itemView) {
            super(itemView);
            this.imagen = itemView.findViewById(R.id.imagen);
            this.nombre = itemView.findViewById(R.id.nombre);
        }

        void bind(Object object) {
            if (object instanceof Categoria) {
                Categoria categoria = (Categoria) object;
                this.nombre.setText(categoria.getNombre());
                Glide.with(this.itemView.getContext())
                        .load(categoria.getUrlImagen())
                        .into(this.imagen);
                this.itemView.setOnClickListener(v -> {
                    Global.getInstance().categoria = categoria;
                    Intent intent = new Intent(this.itemView.getContext(), CategoriaActivity.class);
                    this.itemView.getContext().startActivity(intent);
                });
            } else if (object instanceof Servicio) {
                Servicio servicio = (Servicio) object;
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
}
