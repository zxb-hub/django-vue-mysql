<template>
  <div>
    <el-container>
      <keep-alive>
        <el-aside style="margin-top: 10px;"><newsList @newsId="getNewId"></newsList></el-aside>
      </keep-alive>
      <el-main class="main">
        <router-view :id="newsId" v-if="contentAlive"></router-view>
        <!-- <newsContent :newsid='newsId' v-if='contentAlive'></newsContent> -->
      </el-main>
    </el-container>
  </div>
</template>

<script>
import newsList from '../components/news/newsList.vue';
// import newsContent from '../components/news/newsContent.vue';
import axios from 'axios';
//
export default {
  name: 'news',
  provide() {
    return {
      reload: this.reload
    };
  },
  data() {
    return {
      newsId: '',
      contentAlive: true
    };
  },
  components: {
    newsList: newsList
    // newsContent
  },

  created() {
    this.goRouter();
  },
  mounted() {
    this.goRouter();
  },
  // beforeRouteUpdate(){
  //   this.goRouter()
  // },
  methods: {
    getNewId: function(data) {
      this.newsId = data;
    },

    goRouter: function() {
      this.newsId = this.$route.query.id;
      // console.log('this.newsId:',this.newsId)
    },

      reload:function (){
           this.contentAlive = false
           this.$nextTick(function(){
              this.contentAlive = true
           })
        }
  }
};
</script>

<style>
.el-container {
  min-height: 452px;
}
.main {
  width: 80%;
}
.newsList {
  width: 85%;
  min-height: 250px;
  background-color: #f9f9f9;
  line-height: 22px;
  margin-left: 15%;
}
.newsList ul {
  float: left;
  margin-left: 10px;
}
.newsList li {
  list-style: none;
  cursor: pointer;
}
.panel-body {
  min-height: 100%;
}
</style>
