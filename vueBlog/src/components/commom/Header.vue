<template>
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
    <el-menu-item index="1"><router-link to="/">山鼎竹器网</router-link></el-menu-item>
    <el-submenu index="2">
      <template slot="title">
        大致浏览
      </template>
      <el-menu-item index="2-1"><router-link :to="{ name: 'place' }">厂址介绍</router-link></el-menu-item>
      <el-menu-item index="2-2"><router-link :to="{ name: 'kilang' }">工厂介绍</router-link></el-menu-item>
      <el-menu-item index="2-3"><router-link :to="{ name: 'introd' }">产品详情</router-link></el-menu-item>
      <el-menu-item index="2-4"><router-link :to="{ name: 'exchange' }">最新价格</router-link></el-menu-item>
    </el-submenu>
    <el-menu-item index="3" disabled>{{ this.$store.state.user }}</el-menu-item>
    <el-autocomplete
      placeholder="在本站搜索"
      v-model="search"
      :trigger-on-focus="false"
      :fetch-suggestions="querySearchAsync"
      @select="handleSelect"
      class="header_input"
    ></el-autocomplete>
    <el-button type="primary" icon="el-icon-search" @click="searchContent">搜索</el-button>
    <el-dropdown class="header_dropdown">
      <el-avatar icon="el-icon-user-solid" class="el-dropdown-link"></el-avatar>
      <el-dropdown-menu slot="dropdown" v-if="live">
        <el-dropdown-item>{{ this.$store.state.user }}</el-dropdown-item>
        <el-dropdown-item><span @click="logout">注销</span></el-dropdown-item>
      </el-dropdown-menu>
      <el-dropdown-menu slot="dropdown" v-else>
        <router-link to="/SLin"><el-dropdown-item>登录</el-dropdown-item></router-link>
        <router-link to="/SLin"><el-dropdown-item>注册</el-dropdown-item></router-link>
      </el-dropdown-menu>
    </el-dropdown>
  </el-menu>
</template>

<script>
import { Toast } from 'vant';
import axios from 'axios';
export default {
  name: 'Header',
  data() {
    return {
      username: '',
      live: false,
      activeIndex: '1',
      search: '',
      searchDate: [],
      Data: [],
      news: [],
      timeout: null
    };
  },
  updated() {
    this.tokenlogin();
  },
  methods: {
    //退出登陆状态
    logout: function() {
      let user = this.$store.state.user;
      // console.log('user', user);
      this.$store
        .dispatch('logout', user)
        .then(() => {
          Toast('注销成功');
          this.live = false;
        })
        .catch(err => {
          console.log(err);
        });
    },

    // 获取登陆状态
    tokenlogin: function() {
      if (localStorage.getItem('token')) {
        this.live = true;
        // console.log('获取登陆状态',localStorage.getItem('token'));
      } else {
        this.live = false;
      }
    },

    //数据库中调取文章
    getContent: function() {
      axios.get('/api/news').then(res => {
        let datas = res.data;
        // console.log(datas)
        for (let i in datas) {
          delete datas[i]['model'];
          datas[i].fields['id'] = datas[i].pk;
          datas[i].fields['value'] = datas[i].fields['title'];
          this.news.push(datas[i].fields);
        }
        console.log('search1:', this.news);
        var newL = this.news;
        for (let k in newL) {
          delete newL[k]['articleName'];
          delete newL[k]['content'];
          delete newL[k]['publishDate'];
          delete newL[k]['title'];
          this.searchDate.push(newL[k]);
        }
        console.log('search:', this.searchDate);
      });
    },

    //计算属性 模糊搜索
    querySearchAsync: function(queryString, cb) {
      var searchDate = this.searchDate;
      var results = queryString ? searchDate.filter(this.createStateFilter(queryString)) : searchDate;
      // cb(results);
      this.Data = results;
      console.log('res:', this.Data);

      clearTimeout(this.timeout);
      this.timeout = setTimeout(() => {
        cb(results);
      }, 3000 * Math.random());
    },
    createStateFilter: function(queryString) {
      return search => {
        return search.value.toLowerCase().indexOf(queryString.toLowerCase()) !== -1;
      };
    },
    handleSelect: function(item) {
      console.log(item);
    },
    //路由跳转
    searchContent: function() {
      if (this.search == '') {
        Toast('请输入想要搜索的文章');
      } else if (this.Data == '') {
        Toast('本站目前还没有相关文章,搜搜其他的吧');
      } else {
        let contentId = [];
        for (let i in this.Data) {
          contentId.push(this.Data[i].id);
        }
        this.$router.push({
          path: '/news/search',
          query: { id: contentId }
        });
      }
    }
  },

  mounted() {
    this.getContent();
    this.tokenlogin();
  },

  computed: {}
};
</script>

<style>
.el-autocomplete {
  width: 20%;
  margin-top: 12px;
  left: 59px;
}
.header_input {
  left: 225px;
}
.el-button {

  margin-left: 238px;
}
.el-avatar {
  top: 10px;
  overflow: initial;
}
.el-dropdown {
  width: 40px;
  left: 409px;
}
a {
  text-decoration: none;
}

</style>
