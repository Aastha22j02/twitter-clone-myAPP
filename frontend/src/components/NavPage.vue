<template>
  <div class="container">
      <nav class="navbar navbar-expand-lg  bg-dark navbar-dark ">
        <div class="container-fluid">
          <span> <router-link class="navbar-brand fa fa-twitter" to="/">  Twitter APP </router-link> </span>
          <div class="collapse navbar-collapse" id="navbarNav">
            <div class="container">
              <div class="navbar-nav "> 
                <button v-if="!userLoggedIn" type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                      Login/Register
              </button>
              <button v-else type="button" class="btn btn-danger" >
                  Logout
              </button>
              </div>
            </div>
            <!-- login Modal -->
            <LoginForm></LoginForm>

          </div>
        </div>
      </nav>
  </div>      

</template>

<script>
import LoginForm from './LoginForm.vue'; 
import { mapStores } from 'pinia';

import useModalStore from '@/stores/modal'
import useUserStore from '@/stores/user'



export default {
  data(){
    return{
      userLoggedIn: false
    }
  },
  computed:{
    ...mapStores(useModalStore),
    ...mapStores(useUserStore)
  },
  components:{
    LoginForm,
  },
  methods:{
    toggleModal(){
      this.modalStore.isOpen = !this.modalStore.isOpen
      console.log(this.modalStore.isOpen)
      
    }
  }

}

</script>
