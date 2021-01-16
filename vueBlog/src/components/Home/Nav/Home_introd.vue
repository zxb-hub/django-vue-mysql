<template>
  <div class="introd" id="introd">
    <div class="row" >
      <div class="col-xs-6 col-md-3" v-for="(i,k) in tableData" :key="k">
        <div class="thumbnail" style=" box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
          <a href="#" class="thumbnail">
            <img :src="i.src" :alt="i.name" style="height: 188.8px;">
          </a>
          <div class="caption">
            <h3>{{i.name}}</h3>
            <p>{{i.introd}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeIntrod',
  data() {
    return {
      tableData: [
        {
          date: '2020-05-02',
          name: '竹跳板',
          src:require('../../../assets/chanpin/tiaoban/tiaoban.jpg'),
          introd:'具体规格可定制,详情可联系郑先生'
        },
        {
          date: '2020-05-04',
          name: '竹木棒',
          src:require('../../../assets/chanpin/mubang/mubang2.jpg'),
          introd:'具体规格可定制,详情可联系郑先生'
        },
        {
          date: '2020-05-01',
          name: '炭化防腐木',
          src:require('../../../assets/chanpin/tanhua/tanhua.jpg'),
          introd:'具体规格可定制,详情可联系郑先生'
        },
        {
          date: '2020-05-03',
          name: '竹扇柄原料',
          src:require('../../../assets/chanpin/zhupian/zhupian.jpg'),
          introd:'具体规格可定制,详情可联系郑先生'
        },

      ]
      }

  },
};
</script>

<style>
.introd {
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
  display: block;
}
.row{
  margin-top: 10px;
}
.thumbnail img{
  height: 188.83px;
}
</style>
