<template>
  <div class="splash-screen">
    <vue-progress-bar></vue-progress-bar>
  </div>
</template>

<script>
import VueProgressBar from 'vue-progressbar';

export default {
  components: {
    VueProgressBar,
  },
  mounted() {
    this.startProgressBar();
  },
  methods: {
    startProgressBar() {
      this.$Progress.start();

      // Simulate progress completion after a certain delay
      setTimeout(() => {
        this.$Progress.finish();
        this.redirectToHomePage();
      }, 3000); // Adjust the delay as per your preference
    },
    redirectToHomePage() {
      this.$router.push('/home');
    },
  },
};
</script>

<style>
/* Customize the splash screen styles as per your design */
.splash-screen {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f1f1f1;
}
</style>