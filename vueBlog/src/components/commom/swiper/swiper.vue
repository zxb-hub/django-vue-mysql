<template>
  <div class="slide-show" @mouseover="clear" @mouseout="run">
    <div class="slide-img">
      <span class="carousel_btn left" v-show="showBtn" @click="goto(nextIndex)">&gt;</span>
      <a>
        <transition name="slide-trans"><img v-if="isShow" :src="slides[nowIndex].src" /></transition>
        <transition name="slide-trans-old"><img v-if="!isShow" :src="slides[nowIndex].src" /></transition>
      </a>
      <span class="carousel_btn right" v-show="showBtn" @click="goto(prevIndex)">&lt;</span>
      <ul class="slide-pages">
        <li v-for="(item, index) in slides" @click="goto(index)">
          <a :class="{ on: index === nowIndex }">{{ index + 1 }}</a>
        </li>
      </ul>
    </div>
    <h2>{{ slides[nowIndex].title }}</h2>
  </div>
</template>

<script>
export default {
  props: {
    slides: {
      type: Array,
      default: []
    },
    inv: {
      type: Number,
      default: 1000
    }
  },
  data() {
    return {
      nowIndex: 0,
      isShow: true,
      showBtn: false
    };
  },
  computed: {
    prevIndex() {
      if (this.nowIndex === 0) {
        return this.slides.length - 1;
      } else {
        return this.nowIndex - 1;
      }
    },
    nextIndex() {
      if (this.nowIndex === this.slides.length - 1) {
        return 0;
      } else {
        return this.nowIndex + 1;
      }
    }
  },
  methods: {
    goto(index) {
      this.isShow = false;
      setTimeout(() => {
        this.isShow = true;
        this.nowIndex = index;
      }, 10);
    },
    run() {
      this.invId = setInterval(() => {
        this.goto(this.nextIndex);
      }, this.inv);
      this.showBtn = false;
    },
    clear() {
      clearInterval(this.invId);
      this.showBtn = true;
    }
  },
  mounted() {
    this.run();
  }
};
</script>

<style scoped>
.carousel_btn {
  width: 30px;
  height: 90px;
  background-color: rgba(0, 0, 0, 0.5);
  text-align: center;
  margin-top: 69px;
  z-index: 3;
  position: absolute;
  cursor: pointer;
  padding-top: 32px;
}
.right {
  float: right;
}
.left {
  float: left;
  left: 493px;
}
.slide-trans-enter-active {
  transition: transform 0.5s;
}
.slide-trans-enter {
  opacity: 0;
  transform: translateX(100%);
}
.slide-trans-old-leave-active {
  transition: transform 0.5s;
}
.slide-trans-old-leave-to {
  transform: translateX(-100%);
}
.slide-trans-old-leave {
  transform: translateX(-100%);
}
.slide-show {
  position: relative;
  width: 524px;
  height: 302px;
  overflow: hidden;
}
.slide-show li {
  list-style: none;
}
.slide-show h2 {
  position: absolute;
  top:242px;
  margin-top: 0;
  width: 100%;
  height: 100%;
  color: #fff;
  background: #000;
  opacity: 0.5;
  bottom: 0;
  height: 30px;
  text-align: left;
  padding-left: 15px;
}
.slide-img {
  width: 100%;
}
.slide-img img {
  width: 100%;
  height: 80%;
  position: absolute;
  z-index: 1;
  top: 0;
  left: 0;
}
.slide-pages {
  position: absolute;
  z-index: 2;
  top: 209px;
  bottom: 10px;
  right: 15px;
}
.slide-pages li {
  display: inline-block;
  padding: 0 10px;
  cursor: pointer;
  color: #fff;
}
.slide-pages li .on {
  text-decoration: underline;
}
</style>
