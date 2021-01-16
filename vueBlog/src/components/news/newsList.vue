<template>
  <div class="news">
    <el-card class="box-card" shadow="hover">
      <div slot="header" class="clearfix"><span>最近文章</span></div>
      <div v-for="(t, i) in news" :key="i" @click="goNews(t.pk)" class="text item">{{ t.fields.title }}</div>
      <div class="block">
        <el-pagination
          small
          v-if="value"
          :page-size="5"
          @next-click="handleCurrentChange"
          @prev-click="handleCurrentChange"
          @current-change="handleCurrentChange"
          layout="prev, pager, next"
          :total="totalCount"
        ></el-pagination>
      </div>
    </el-card>
  </div>
</template>

<script>
import axios from 'axios'; //导入封装的axios
export default {
  inject:['reload'],
  name: 'newsList',
  data() {
    return {
      value: false,
      news: [], //返回的数据列表
      totalCount: 0, //总条数
      totalPage: 0, //总页数
      pageNo: 1, //当前页码
      pageId: 0
    };
  },

  created: function() {
    this.getPageData();
  },

  methods: {
    //跳转
    goNews: function(id) {
      this.$router.push({
        path:''+id,
        query: {
          id: id
        }
      });
      this.reload()
    },
    //获取分页
    getPageData: function() {
      let id = this.pageId;
      // console.log('id:', id);
      axios
        .get('/api/addPage', { params: { pageId: id } })
        .then(res => {
          // console.log(res.data);
          this.news = res.data.newPage;
          // console.log('this.news', this.news);
          this.totalCount = res.data.totalCount;
          // console.log('this.totalCount', this.totalCount);
          this.totalPage = res.data.totalPage;
          // console.log(this.totalPage);
          if (this.totalPage > 1) {
            this.value = true;
          }
        })
        .catch(error => {
          console.log(err);
        });
    },
    //点击切换分页
    handleCurrentChange: function(val) {
      this.pageId = (val - 1) * 5;
      console.log(this.pageId);
      this.getPageData();
    },


  }
};
</script>

<style>
.news {
  margin-top: 5px;
  float: left;
  min-height: 342px;
  width: 85%;
  margin-left: 15%;
  background-color: #f9f9f9;
  position: relative;
}
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
  cursor: pointer;
}
.item:hover {
  color: #87dc49;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: '';
}
.clearfix:after {
  clear: both;
}
.box-card {
  width: 100%;
  height: 100%;
}
</style>
