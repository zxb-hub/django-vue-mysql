<template>
  <div style="min-height: 800px;">
    <HomeAd></HomeAd>
    <HomeNews style='margin-top: 10px;'></HomeNews>
    <HomeCarousel style='margin-top: 10px;'></HomeCarousel>
    <HomeNav/>
  </div>
</template>

<script>
import HomeAd from '../components/Home/Home_ad.vue'

import HomeNews from '../components/Home/Home_news.vue'

import HomeNav from '../components/Home/Home_nav.vue'

import HomeCarousel from '../components/Home/Home_carousel.vue'

export default {
  name: 'Home',

  components: {
    HomeNav,
    HomeAd,
    HomeNews,
    HomeCarousel
  }
};
</script>

<style></style>
