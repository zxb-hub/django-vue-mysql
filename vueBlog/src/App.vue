<template>
  <div id="app">
    <el-header><Header /></el-header>
    <el-main><router-view></router-view></el-main>
    <el-footer><Footer /></el-footer>
  </div>
</template>
<script>
import Footer from './components/commom/Footer.vue'

import Header from './components/commom/Header.vue'

export default {
  name: 'app',
  components: {
    Footer,
    Header,
  }
};
</script>
<style>
  #app{
    min-height: 663px;
  }
</style>
