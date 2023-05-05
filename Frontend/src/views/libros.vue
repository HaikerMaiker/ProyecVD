<script setup>
    import {onMounted, ref} from 'vue'
    import axios from 'axios'
    import router from '../router';

    const data = ref([
        {
            id:"",
            titulo:"",
            sinopsis:"",
            autores: [],
            calificacion:"",
            calificaciones:"",
            fecha_publicacion:"",
            genero:"",
            num_pag:"",
            portada:""
        }
    ]);
    onMounted(
        axios.get('http://localhost:8000/api/libros')
        .then((result) => {
            console.log(result.data);
            data.value = result.data;
        })
        .catch((error) => {
            console.log(error)
        })
    )

    function goToBook(id){
        router.push({ name: 'libro', params: { id: id } })
    }

</script>

<template>
  <div class="container">
    <main>
        <h1>Libros</h1>
        <div v-for="(item,i) in data " v-bind:key="i" class="card" style="width: 18rem;" @click="goToBook(item.id)">
            <img :src="item.portada" class="card-img-top" alt="...">
            <div class="card-body">
                <!--<div class="col" v-for="(item,i) in data" :key="i" @click="goToBook(item.id)">-->
                    <h5 class="card-title">{{ item.titulo }}</h5>
                    <p class="card-text">Autor: {{ item.autores[0].nombre +" "+ item.autores[0].apellido}}</p>
                    <p class="card-text">Paginas: {{ item.num_pag }}</p>
                    <p class="card-text">{{ item.sinopsis }}</p>
                    <a href="#" class="btn btn-primary">{{item.autores[0].nombre +" "+ item.autores[0].apellido}}</a>
                <!--</div>-->
            </div>
        </div>
    </main>
  </div>
</template>


