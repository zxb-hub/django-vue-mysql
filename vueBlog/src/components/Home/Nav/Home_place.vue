<template>
  <div class="place" id="place">
    <div style="width: 50%;float: left;">
      <h1>介绍:</h1>
      <h3><strong>厂址介绍:</strong></h3>
      <p>
        <strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;山顶竹器厂</strong>
        坐落于安徽省
        <a
          target="_blank"
          href="https://baike.baidu.com/item/%E5%B9%BF%E5%BE%B7/9990522?fromtitle=%E5%AE%89%E5%BE%BD%E7%9C%81%E5%B9%BF%E5%BE%B7%E5%8E%BF&fromid=7242365&fr=aladdin"
        >
          广德市
        </a>
      </p>
      <p>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;广德市，安徽省辖县级市，由宣城市代管。位于安徽省东南部，苏浙皖三省八县（市）交界处，介于北纬30°37′—31°12′，东经119°02′—119°
        40′之间，总面积2165平方千米。 广德市活立木总蓄积居全省第一、全国第六，是“中国竹子之乡”、“中国板栗之乡” ，被评为“全国绿化模范县” 、“全国经济林建设示范县”
        、“全国山区综合开发示范县” 、全省林业产业十强县（市）。2019年8月，广德撤县设市获批，由安徽省直辖宣城市代管。
        2019年10月8日，被评为2019年度全国综合实力百强县市、2019年度全国新型城镇化质量百强县市。
        2018年，广德市下辖6个镇、3个乡，另设有1个茶场，常住人口49.9万人，实现地区生产总值（GDP）260.1亿元，分产业看，第一产业增加值22.2亿元，第二产业增加值134.0亿元，第三产业增加值103.9亿元，三次产业结构为8.5：51.5：40.0，按常住人口计算，人均GDP52132元。
      </p>
    </div>
    <div id="place_Map" style="width: 40%;height: 300px;margin-top: 94px;float: left;margin-left: 45px;"></div>
  </div>
</template>

<script>
export default {
  name: 'HomePlace',
  data() {
    return {
      // return {
      // }
    };
  },
  // created: {

  // },
  mounted: function() {
    this.HomePlaceMap();
  },
  methods: {
    HomePlaceMap() {
      const map = new BMap.Map('place_Map'); // 创建地图实例
      const point = new BMap.Point(119.428047, 30.883667); // 创建点坐标
      map.centerAndZoom(point, 11); // 初始化地图，设置中心点坐标和地图级别
      const marker = new BMap.Marker(point);
      map.addOverlay(marker);
      map.enableScrollWheelZoom(true);
      map.addControl(new BMap.NavigationControl());
      map.addControl(new BMap.ScaleControl());
      map.addControl(new BMap.OverviewMapControl());
      map.addControl(new BMap.MapTypeControl()); // 开启鼠标滚轮缩放
    }
  }
};
</script>

<style>
.place {
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
