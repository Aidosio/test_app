import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'welcome',
    component: () => import('../views/Welcome')
  },
  {
    path: '/:pages_slug/:content_slug/:id',
    name: 'Pages',
    component: () => import('../views/Pages')
  },
  {
    path: '/sections',
    name: 'Sections',
    component: () => import('../views/Sections')
  },
  {
    path: '/sections/:id',
    name: 'SectionsPage',
    component: () => import('../views/SectionsPage')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
