<template>
  <div class="container">
    <div class="alert alert-success alert-dismissible" role="alert" v-if="success">
      <strong>{{ success }}</strong> Go to login page
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    <form @submit.prevent="registerFrom">
      <div class="mb-3">
        <label for="Name" class="form-label">Name</label>
        <input type="text" class="form-control" v-model="name" name="Name" />
      </div>

      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" v-model="email" name="email" />
      </div>

      <div class="mb-3">
        <label for="Age" class="form-label">Age</label>
        <input type="number" class="form-control" v-model="age" name="Age" />
      </div>

      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" v-model="password" name="password" />
      </div>
      <div class="mb-3">
        <label for="cpassword" class="form-label">Confirm Password</label>
        <input type="password" class="form-control" v-model="cpassword" name="cpassword" />
      </div>

      <button type="submit" class="btn btn-primary">Register</button>
    </form>
    <!-- <div class="">Danger with contrasting color</div> -->
    <div class="conatier text-danger" v-if="error">
      <strong> {{ error }}</strong>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      name: null,
      email: null,
      age: null,
      password: null,
      cpassword: null,
      error: null,
      success: null
    }
  },
  methods: {
    registerFrom() {
      if (!this.name || !this.email || !this.age || !this.password || !this.cpassword) {
        this.error = 'Please add all fields'
      } else {
        const formData = {
          name: this.name,
          email: this.email,
          age: this.age,
          password: this.password,
          cpassword: this.cpassword
        }
        this.saveFormData(formData)
        // this.checkEmailUnique(formData);
      }
    },
    checkEmailUnique(formData) {
      axios.get(`http://127.0.0.1:8000/api/v1/check-email/?email=${formData.email}`)
        .then((response) => {
          const isUnique = response.data.is_unique
          if (isUnique) {
            this.registerFrom(formData)
          } else {
            this.error = 'Email is already taken'
          }
        })
        .catch(error =>{
            console.error(error);
        })
    },
    saveFormData(formData) {
      axios
        .post('http://127.0.0.1:8000/api/v1/users/', formData)
        .then((response) => {
          console.log(response.data)
          this.success = 'Registration successfull'
        })
        // .then(()=>{
        //     this.$router.push({
        //         name: 'home'
        //     })
        // })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>
