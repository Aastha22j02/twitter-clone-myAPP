<template>
    
<main>
  <div class="container py-4">
    <div class="p-5 mb-4 bg-body-tertiary rounded-3">
      <div class="container-fluid py-5">
        <h1 class="display-5 fw-bold">Welcome to the Twitter App</h1>
        <p class="col-md-8 fs-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit, voluptate officia ad ducimus illo officiis sequi cum dolor quas voluptatibus?
             Accusamus quia sequi est deleniti dolorem. Dicta assumenda provident nesciunt.</p>
             
        <button class="btn btn-primary btn-lg" type="button" @click="togglefrom">Register to view more</button>
      </div>
    </div>

    <div class="row align-items-md-stretch">
      <div class="col-md-6">
        <div class="h-100 p-5 text-bg-dark rounded-3">
          <h2>Twitter App Functionality</h2>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Asperiores, a. Nostrum fugit delectus excepturi accusamus commodi inventore perf
            erendis enim, officiis culpa ducimus quas animi aliquid laborum unde? Repellendus, hic eligendi?</p>
          <button class="btn btn-outline-light" type="button">View Functionality</button>
        </div>
      </div>
      <div class="col-md-6">
        <div class="h-100 p-5 bg-body-tertiary border rounded-3">
          <h2>Explore Twitter App</h2>
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. A doloribus eius itaque voluptatem vitae quis deleniti 
            optio voluptas ex neque ipsa saepe, veniam laboriosam, quam adipisci hic modi accusamus earum?</p>
          <button class="btn btn-outline-secondary" type="button">Explore</button>
        </div>
      </div>
    </div>


  </div>
</main>

<div class="container">

    <form  v-if="showFrom" action="">

<label for="">Name</label>
</form>
</div>
</template>

<style>
.bd-placeholder-img {
  font-size: 1.125rem;
  text-anchor: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
}

@media (min-width: 768px) {
  .bd-placeholder-img-lg {
    font-size: 3.5rem;
  }
}

.b-example-divider {
  width: 100%;
  height: 3rem;
  background-color: rgba(0, 0, 0, .1);
  border: solid rgba(0, 0, 0, .15);
  border-width: 1px 0;
  box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
}

.b-example-vr {
  flex-shrink: 0;
  width: 1.5rem;
  height: 100vh;
}

.bi {
  vertical-align: -.125em;
  fill: currentColor;
}

.nav-scroller {
  position: relative;
  z-index: 2;
  height: 2.75rem;
  overflow-y: hidden;
}

.nav-scroller .nav {
  display: flex;
  flex-wrap: nowrap;
  padding-bottom: 1rem;
  margin-top: -1px;
  overflow-x: auto;
  text-align: center;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
}

.btn-bd-primary {
  --bd-violet-bg: #712cf9;
  --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

  --bs-btn-font-weight: 600;
  --bs-btn-color: var(--bs-white);
  --bs-btn-bg: var(--bd-violet-bg);
  --bs-btn-border-color: var(--bd-violet-bg);
  --bs-btn-hover-color: var(--bs-white);
  --bs-btn-hover-bg: #6528e0;
  --bs-btn-hover-border-color: #6528e0;
  --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
  --bs-btn-active-color: var(--bs-btn-hover-color);
  --bs-btn-active-bg: #5a23c8;
  --bs-btn-active-border-color: #5a23c8;
}
.bd-mode-toggle {
  z-index: 1500;
}
</style>

<script>

export default{
  methods:{

    togglefrom(){
      this.showFrom = !this.showFrom
    }
  }
}

</script>