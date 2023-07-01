import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ProfileView from '../views/ProfileView.vue'


import SplashScreen from '../components/SplashScreen.vue'



const routes  = [
 {
  path: '/',
  name: 'home',
  component:  HomeView
 },
 {
  path: '/about',
  name: 'about',
  component: AboutView
 },
 {
  path: '/profile',
  name: 'profile',
  component: ProfileView
 },
 {
  path: '/splashscreen',
  name: 'splashscreen',
  component: SplashScreen
 }

]

const router = createRouter({

  history: createWebHistory(),
  routes,
})


export default router