
import './assets/base.css'
// import './assets/tailwind.css'

import 'bootstrap'
import 'bootstrap/dist/js/bootstrap.js'
import 'bootstrap/dist/css/bootstrap.css'
// import VueProgressBar from 'vue-progressbar'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router/router.js'

const app = createApp(App)

app.use(createPinia())
app.use(router)
// app.use(VueProgressBar)
app.mount('#app')
