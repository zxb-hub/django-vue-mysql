<template>
  <div class="nav" id="nav">
    <ul id="nav_ul">
      <router-link :to="{name:'place'}"><li>厂址介绍</li></router-link>
      <router-link :to="{name:'kilang'}"><li>工厂介绍</li></router-link>
      <router-link :to="{name:'introd'}"><li>产品详情</li></router-link>
      <router-link :to="{name:'exchange'}"><li>最新价格</li></router-link>
    </ul>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'HomeNav',
  data() {
    return {};
  }
};
</script>

<style>
.nav {
  margin-top: 15px;
  width: 50%;
  height: 530px;
  margin-left: 25%;
  float: left;
}

.nav ul {
  width: 100%;
  height: 100px;
  float: left;
  list-style: none;
}

.nav li {
  width: 25%;
  height: 100%;
  text-align: center;
  float: left;
  font-size: 1.5em;
  font-family: Arial, Helvetica, sans-serif;
  padding-top: 39px;
  cursor: pointer;
}

.li_change {
  background-color: #aaa;
}
</style>
