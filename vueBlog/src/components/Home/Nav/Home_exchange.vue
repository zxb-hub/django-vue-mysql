<template>
  <div class="exchange" id="exchange">
    <el-table :data="tableData" height="250" border style="width: 100%">
      <el-table-column prop="date" label="日期" width="180px"></el-table-column>
      <el-table-column prop="name" label="产品" width="180px"></el-table-column>
      <el-table-column prop="address" label="单价"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'HomeExchange',
  data() {
    return {
      tableData: [
        {
          date: '2020-05-02',
          name: '竹跳板',
          address: '可面议'
        },
        {
          date: '2020-05-04',
          name: '竹木棒',
          address: '可面议'
        },
        {
          date: '2020-05-01',
          name: '重竹地板原料',
          address: '可面议'
        },
        {
          date: '2020-05-03',
          name: '竹扇柄原料',
          address: '可面议'
        },
        {
          date:'2020-05-03',
          name:'青竹竿',
          address:'可面议'
        }
      ]
    };
  }
  // created: {

  // },
  // methods: {

  // },
};
</script>

<style>
.exchange {
  width: 68%;
  height: auto;
  min-height: 400px;
  float: left;
  margin-left: -9.5%;
  background-color: #f9f9f9;
  margin-top: 110px;
  padding-left: 18px;
  padding-right: 14px;
  position: absolute;
  border-radius: 1.5em;
  margin-bottom: 10px;

}
</style>
