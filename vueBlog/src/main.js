import $ from 'jquery';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import 'element-ui/lib/theme-chalk/index.css';
import Vue from 'vue';
import ElementUI from 'element-ui';
import App from './App.vue';
import router from './router';
import store from './store';
import Axios from 'axios';
import { Toast } from 'vant';


Vue.config.productionTip = false; // 阻止启动生产消息

Vue.use(ElementUI);


Vue.prototype.$axios = Axios
let getCookie = function (cookie) {
    let reg = /csrftoken=([\w]+)[;]?/g
    return reg.exec(cookie)[1]
}
Axios.interceptors.request.use(
  function(config) {
    let cookie = document.cookie;
    if (cookie && config.method == 'post') {
      config.headers['X-CSRFToken'] = getCookie(cookie);
    }
    return config;
  },
)

router.beforeEach((to, from, next) => {
  // 检测路由配置中是否有isLogin这个meta属性
  if (to.matched.some(record => record.meta.isLogin)) {
    // 判断是否已登录
    if (store.getters.isLoggedIn) {
      next();
      return;
    }else{
      Toast("请先登录")
      next('/SLin');// 未登录则跳转到登录界面
    }
  } else {
    next()
  }
})
new Vue({
  router,
  $,
  store:store,
  render: (h) => h(App),
}).$mount('#app');
