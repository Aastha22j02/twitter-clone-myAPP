<template>
  <div class="container">
      <nav class="navbar navbar-expand-lg  bg-dark navbar-dark ">
        <div class="container-fluid">
          <span> <router-link class="navbar-brand" to="/">Twitter</router-link> </span>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <span> <router-link class="nav-link active" aria-current="page" :to="{name: 'home' }">Home</router-link> </span>
              </li>
              <li class="nav-item">
               <span><router-link class="nav-link active" aria-current="page" :to="{name: 'about'}">About</router-link></span> 
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Settings</a>
              </li>
            </ul>
            <div class="container">
              <div class="navbar-nav">
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                      Login/Register
              </button>
               <!-- <button class=" modal fade"  id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" @click.prevent="toggleModal">Login/Register</button>          -->
              </div>
            </div>
            <!-- Modal -->
            <LoginSignup></LoginSignup>

          </div>
        </div>
      </nav>

</div>      

</template>

<script>
import LoginSignup from './LoginForm.vue'; 
import { mapStores } from 'pinia';

import useModalStore from '@/stores/modal'


export default {
  computed:{
    ...mapStores(useModalStore),
  },
  components:{
    LoginSignup,
  },
  methods:{
    toggleModal(){
      this.modalStore.isOpen = !this.modalStore.isOpen
      console.log(this.modalStore.isOpen)
    }
  }

}



// export default{
//   methods:{
//     loginwindow(){
//       const width = 100;
//       const height = 200;
//       const left = window.innerWidth / 2 - width / 2;
//       const top = window.innerHeight / 2 - height / 2;

//       window.open('/about', '_blank',`width=${width}, highth=${height},left=${left},top=${top}`);
//     }
//   }
// }
</script>
