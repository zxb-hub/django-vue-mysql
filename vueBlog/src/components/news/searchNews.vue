<template>
  <div>
    <div v-for="(i, k) in item" :key='k'>
      <el-card shadow="hover">
        <span>{{ i.title }}</span>
        <span>{{ i.content | contentF }}</span>
        <span>{{ i.time }}</span>
      </el-card>
    </div>
  </div>
</template>
<script>
  import axios from 'axios';
export default {
  name: 'newContent',
  data() {
    return {
      newsId:[],
      item:[]
    };
  },
  props: {
    news: []
    
  },

  //过滤器
  filters: {
    contentF: function(value) {
      if (!value) {
        return '';
      }
      if (value.length > 32) {
        return value.slice(0, 32) + '...';
      }
      return value;
    }
  },

  created() {
    this.goRouter()
  },
  methods:{
    //获取路由传过来的搜索文章的id
    goRouter: function() {
      this.newsId = this.$route.params.id;
      console.log('获取路由传过来的搜索文章的id',this.newsId);
    },

    //axios请求数据
    getNews:function(){
      id = toString(this.newsId)
      axios.get('/api/newsContent',{newsId:id}).then(res=>{
        this.item = res.data
      })
    }
  }
};
</script>

<style></style>
