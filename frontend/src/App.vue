<script setup lang="ts">
import Navbar from "./components/Navbar.vue";
import FormPass from "./components/Form.vue";
import Footer from "./components/Footer.vue";
</script>

<template>
    <Navbar />
    <div style="margin-top: 50px;" class="h-100">
      <div class="container">
        <div class="row">
          <div class="col-md-6 d-none d-md-grid d-lg-grid d-xl-grid d-xxl-grid">
            <img src="./assets/img/11608454_4673524.svg" alt="ayudaa">
          </div>
          <div class="col-md-6 d-flex justify-content-center align-items-center">
            <FormPass />
          </div>
        </div>
      </div>
    </div>
    <Footer/>
</template>
