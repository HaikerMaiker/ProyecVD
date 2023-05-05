<script setup>
    import {onMounted, ref} from 'vue'
    import axios from 'axios'
    import router from '../router';

    const props = defineProps(['id'])
    const libro = ref('')
    onMounted(()=>{
        axios
        .get('http://localhost:8000/api/libros/'+props.id+'/')
        .then(result => {
            console.log(result.data)
            libro.value = result.data
        })
        .catch(error => {
            console.log(error)
        })
    })

    function eliminarLibro(){
        axios.delete('http://localhost:8000/api/libros/'+libro.value.id)
        .then(()=>{
            router.push({ name: 'libros' });
        })
        .catch(error => {
            console.log(error)
        })
    }

    function editarLibro(){
        router.push({ name: 'editar_libro', params: { id: props.id }});
    }
</script>


<template>
    <div class="container">
        <h1 class="mt-5">{{libro.titulo}}</h1>
        <img :src="libro.portada">
        <p>
            Autor: {{libro.autores[0].nombre +" "+ libro.autores[0].apellido}} <br/>
            Páginas: {{libro.num_pag}} <br/>
            Género: {{libro.genero.nombre}} <br/>
        </p>
        <p>Sinopsis: {{libro.sinopsis}}</p>
        <button class="btn btn-primary" @click="eliminarLibro()">Eliminar</button>
        <button class="btn btn-primary" @click="editarLibro()">Editar</button>
    </div>
</template>