<template>
  <div
    class="modal fade"
    id="exampleModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
    :class="{ show: showModal }"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Your Account</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="d-flex justify-content-center">
          <button
            type="button"
            class="btn btn-lg m-2"
            :class="{
              'btn-primary': tab === 'login',
              'btn-secondary': tab === 'register'
            }"
            @click.prevent="tab = 'login'"
          >
            login
          </button>
          <button
            type="button"
            class="btn btn-primary btn-lg m-2"
            :class="{
              'btn-primary': tab === 'register',
              'btn-secondary': tab === 'login'
            }"
            @click.prevent="tab = 'register'"
          >
            Register
          </button>
        </div>

        <div class="modal-body">
          <div class="container">
            <div class="container">
              <div class="alert alert-success alert-dismissible" role="alert" v-if="success">
                <strong>{{ success }}</strong
                >LoggedIn
                <button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="alert"
                  aria-label="Close"
                ></button>
              </div>
            </div>
            <!-- User Login form -->
            <form v-show="tab === 'login'" @click.prevent="login">
              <div class="mb-3">
                <label for="email" class="form-label">Email address</label>
                <input
                  type="email"
                  class="form-control"
                  aria-describedby="emailHelp"
                  name="email"
                  v-model="email"
                />
                <div id="emailHelp" class="form-text">
                  We'll never share your email with anyone else.
                </div>
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" v-model="password" name="password" />
              </div>
              <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="exampleCheck1" />
                <label class="form-check-label" for="exampleCheck1">Check me out</label>
              </div>
              <button type="submit" class="btn btn-primary">Submit</button>
            </form>
          </div>
          <div class="conatainer">
            <!-- Register from added manually -->
            <RegisterFrom v-show="tab === 'register'"></RegisterFrom>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import { mapState } from 'pinia'
import { mapStores } from 'pinia'
import useUserStore from '@/stores/user'

import RegisterFrom from '../components/RegisterForm.vue'

import useModalStore from '@/stores/modal'

export default {
  data() {
    return {
      tab: 'login',
      email: null,
      password: null,
      showModal: false,
      success: null
    }
  },
  computed: {
    ...mapState(useModalStore, ['btn-close']),
    ...mapStores(useUserStore)
  },
  components: {
    RegisterFrom
  },
  methods: {
    login() {
      const formData = {
        email: this.email,
        password: this.password,
        username: null
      }
      axios
        .post('http://127.0.0.1:8000/api/v1/login/', formData)
        .then((response) => {
          console.log(response.data.message)
          // this.username(response.data.username)


          this.success = 'Successfull LoggedIn!'

          this.$router.push('/profile')
          console.log(this.userStore.userLoggedIn)

          this.userLoggedIn = true

          console.log(this.userStore.userLoggedIn)

          // Perform any necessary actions after successful login
        })
        .catch((error) => {
          console.error(error.response.data.message)
          // Handle login error
        })
    },
    closeModal() {
      this.showModal = false
      console.log('closeModal')
    }
  }
}
</script>
