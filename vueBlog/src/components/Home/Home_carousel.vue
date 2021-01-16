<template>
  <div id="carousel" class="carousel"><carousel :slides="slides" :inv="invTime"></carousel></div>
</template>

<script>
import carousel from '../commom/swiper/swiper.vue';
export default {
  data() {
    return {
      invTime: 10000,
      slides: [
        {
          src: require('../../assets/swiper/1.jpg'),
          title: '图1'
        },
        {
          src: require('../../assets/swiper/2.jpg'),
          title: '图2'
        },
        {
          src: require('../../assets/swiper/3.jpg'),
          title: '图3'
        },
        {
          src: require('../../assets/swiper/4.jpg'),
          title: '图4'
        },
        {
          src: require('../../assets/swiper/5.jpg'),
          title: '图5'
        }
      ]
    };
  },
  components: {
    carousel
  }
};
</script>

<style>
.carousel {
  width: 40%;
  height: 340px;
  float: right;
  margin-left: 13px;
  margin-top: 10px;
  margin-right: 15%;
  position: relative;
  background-color: #f9f9f9;
}
</style>
