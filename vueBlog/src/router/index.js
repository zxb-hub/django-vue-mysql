import Vue from 'vue';
import VueRouter from 'vue-router';


Vue.use(VueRouter);


const routes = [{
    path: '',
    redirect: '/home'
  },

  // 首页
  {
    path: '/home',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    children: [{
        path: 'exchange',
        name: 'exchange',
        component: () => import('../components/Home/Nav/Home_exchange.vue'),

      },
      {
        path: 'introd',
        name: 'introd',
        component: () => import('../components/Home/Nav/Home_introd.vue'),

      },
      {
        path: 'kilang',
        name: 'kilang',
        component: () => import('../components/Home/Nav/Home_kilang.vue'),

      },
      {
        path: '',
        name: 'place',
        component: () => import('../components/Home/Nav/Home_place.vue'),

      },
    ],

    meta: {
      isLogin: false
    }
  },

  // 登陆注册
  {
    path: '/SLin',
    name: 'SLin',
    component: () => import('../views/SLin.vue'),
    meta: {
      isLogin: false,
    }
  },

  // 新闻界面
  {
    path: '/news/:id',
    name: 'news',
    component: () => import('../views/News.vue'),
    children:[{
      path:'',
      component:() => import('../components/news/newsContent.vue')
    }],
    meta: {
      isLogin: true
    }
  },


  //管理员界面
  {
    path:'superUser',
    name:'superUser',
    component:() => import('../views/superLogin.vue'),
    meta:{
      isSuper:true
    },

  }
];

const router = new VueRouter({
  mode: 'history',
  routes,
  scrollBehavior (to, from, savedPosition) {
        return { x: 1000, y: 1000 }
    },
  
});

export default router;
