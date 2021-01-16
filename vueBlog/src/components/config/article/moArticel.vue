<template>
  <el-table
        :data="Article"
        height="250"
        border
        style="width: 100%">
        <el-table-column
          prop="date"
          label="日期"
          width="180">
        </el-table-column>
        <el-table-column
          prop="name"
          label="姓名"
          width="180">
        </el-table-column>
        <el-table-column
          prop="address"
          label="地址">
        </el-table-column>
        <el-table-column
              fixed="right"
              label="操作"
              width="100">
              <template slot-scope="scope">
                <el-button type="primary" icon="el-icon-edit" circle></el-button>
              </template>
        </el-table-column>
      </el-table>
  </template>
</template>

<script>
  export default{
    name:"moArticle",
    data(){

    }
      }
</script>

<style>
</style>
