<template>
  <div>
    <el-input type="textarea" maxlength="30" show-word-limit :rows="1" placeholder="请输入标题" v-model="title"></el-input>
    <el-input type="textarea" :rows="1" maxlength="30" placeholder="上传作者/转载自" v-model="articleName"></el-input>
    <el-input type="textarea" :rows="5" placeholder="请输入内容" :autosize="{ minRows: 2, maxRows: 150 }" v-model="content"></el-input>
    <el-date-picker v-model="date" type="date" placeholder="选择日期"></el-date-picker>
    <el-button type="primary">上传<i class="el-icon-upload el-icon--right"></i></el-button>
  </div>

  <script>
    export default {
      name: 'addArticle',
      data() {
        return {
          title: '',
          articleName: '',
          content: '',
          date: ''
        };
      }
    };
  </script>

  <style></style>
</template>
