<template>
  <div class="kilang" id="kilang">
    <div style="width: 50%;float: left;">
      <div>
        <h3><strong>山鼎竹器厂</strong></h3>
        <p style="margin-top: 30px;">
          &nbsp;&nbsp;&nbsp;&nbsp;山鼎竹业成立于2013年，坐落于有着毛竹之乡的安徽省广德市。山鼎竹器厂具有工商注册资格，同时也是广德市柏垫镇商协会重要成员。
        </p>
        <p>
          &nbsp;&nbsp;&nbsp;&nbsp;本厂生产竹席,竹板，竹棒等竹器品，产品在供货量充足的基础上，质量也有保证，同时部分商品可接受定制，如需订制请提前联系，
          <strong>联系方式：13856381684，郑先生；</strong>
        </p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;同时厂内引进生物碳化炉，生产过程绿色环保，材料利用率高，产生污染少</p>
      </div>
    </div>
    <div id="Kilang_Map" style="width: 40%;height: 300px;margin-top: 94px;float: left;margin-left: 45px;"></div>
  </div>
</template>

<script>

export default {
  name: 'HomeKilang',
  data() {
    return {};
  },
  mounted:function() {
    this.HomeKilang();
  },

  methods: {
    HomeKilang: function() {
      var map = new BMap.Map('Kilang_Map');
      var point = new BMap.Point(119.277369, 30.761906);
      var marker = new BMap.Marker(point);
      map.centerAndZoom(point, 14);
      map.addOverlay(marker);
      map.enableScrollWheelZoom(true);
      map.addControl(new BMap.NavigationControl());
      map.addControl(new BMap.ScaleControl());
      map.addControl(new BMap.OverviewMapControl());
      map.addControl(new BMap.MapTypeControl());
    }
  },
};
</script>

<style>
.kilang {
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
</style>
