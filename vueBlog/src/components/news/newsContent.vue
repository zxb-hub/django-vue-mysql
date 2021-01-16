<template>
  <div class="content">
    <div class="panel panel-default">
      <div class="panel-heading">
        <h1 class="panel-title title">{{ news.title }}</h1>
      </div>
      <div class="panel-body">{{ news.content }}</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  
  // props:['newsid'],
  data() {
    return {
      news: [],
      newsId: ''
    };
  },
  created() {
    this.goRouter();
  },
  mounted() {
    this.getArticle(this.newsId)
  },
  methods: {
    //获取页面传值
    goRouter: function() {
      this.newsId = this.$route.query.id;
      // this.newsId = this.id
      console.log('this.newsId',this.newsId);
    },
    //获取文章详情
    getArticle:function(id){
      axios.get('/api/newsContent', {params:{ newsId: this.newsId }} ).then(res => {
        this.news = res.data[0].fields;
      });
    }
  },
  //监听 newsId 变化 ,发生改变更新数据
  // watch:{
  //   newsId: function(newVal,oldVal){
  //     this.goRouter(newVal);
  //     this.getArticle(newVal)
  //     console.log('this.newsId',newVal)
  //   }
  // }
};
</script>

<style>
  .title{

  }
</style>
