import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/libros',
      name: 'libros',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/libros.vue')
    },
    {
      path: '/autores',
      name: 'autores',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/autores.vue')
    },
    {
      path: '/libro/:id',
      name: 'libro',
      props: true,
      component: () => import('../views/LibroView.vue')
    },
    {
      path: '/nuevo_genero',
      name: 'nuevo_genero',
      component: () => import('../views/AgregaGeneroView.vue')
    },
    {
      path: '/editar_libro/:id',
      name: 'editar_libro',
      props: true,
      component: () => import('../views/EditarLibroView.vue')
    }
  ]
})

export default router
