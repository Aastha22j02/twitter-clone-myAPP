<template>

<NavPage></NavPage>
<router-view></router-view>
<!-- <Welcomepage></Welcomepage> -->


</template>

<script>

import NavPage from './components/NavPage.vue';
import Welcomepage from './components/WelcomePage.vue'
// import LoginSignup from './components/LoginSignup.vue';


export default{

  components:{
    NavPage,
    Welcomepage,
    // LoginSignup,
  }
}

</script>







