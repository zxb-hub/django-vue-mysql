<template>
  <div style="min-height: 100px;">
    <div class="ad">
      <img src="../../assets/ad/mxj2.png" @click="ad('http://mxj123.top/')" alt="抹香鲸工具箱" style="height: 100%;width: 19%;cursor:pointer" />
      <img src="../../assets/ad/mxj1.png" @click="ad('http://mxj123.top/')" alt="抹香鲸工具箱" style="width: 80.5%;height: 100%;cursor:pointer" />
    </div>
    <div class="ad" style="background-color: rgba(0,0,0,0.1);text-align: center;padding-top: 40px;margin-bottom:5px;"><span @click="ad('#')">招商广告</span></div>
  </div>
</template>

<script>
export default {
  name: 'HomeAd',
  data() {
    return {};
  },
  methods: {
    ad(a) {
      window.location.href = a;
    },
  },
};
</script>

<style>
.ad {
  height: 100px;
  width: 70%;
  float: left;
  margin-left: 15%;
  margin-top: 5px;
}
</style>
