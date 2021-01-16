<template>
  <div class="Homenews">
    <el-card class="box-card" shadow='hover'>
      <div slot="header" class="clearfix"><span>新闻中心</span></div>
      <div v-for="(t, i) in news" :key="i" @click="goNews(t.pk, t.fields.title)" class="text item">{{ t.fields.title }}</div>
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
  name: 'HomeNews',
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
    goNews: function(id, title) {
      console.log('首页跳转id:',id)
      this.$router.push({
        path: 'news/'+id,
        query: {
          id: id
        }
      });
    },
    getPageData: function() {
      let id = this.pageId;
      // console.log('id:', id);
      axios
        .get('/api/addPage', { params: { pageId: id } })
        .then(res => {
          // console.log(res.data);
          this.news = res.data.newPage;
          // console.log(this.news);
          this.totalCount = res.data.totalCount;
          // console.log(this.totalCount);
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
    handleCurrentChange: function(val) {
      this.pageId = (val - 1) * 5;
      // console.log(this.pageId);
      this.getPageData();
    }
  }
};
</script>

<style>
.Homenews {
  margin-top: 10px;
  float: left;
  height: 340px;
  width: 29%;
  margin-left: 15%;
  background-color: #f9f9f9;
  position: relative;
}
.el-card__body{
  padding-top: 7px;

}
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 0px;
  cursor: pointer;
  height: 40px;
  margin-top: 5px;
  margin-bottom: 5px;
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
