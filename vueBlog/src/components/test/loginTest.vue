<template>
  <div class="logTitle" id="logTitle">
    <ul>
      <router-link :to="{ name: 'Login' }">
        <li id="loginSpan" @click="titleChange()"  :class="{loginSpanChange:show }">
          <span><strong>登录</strong></span>
        </li>
      </router-link>
      <router-link :to="{ name: 'Signin' }">
        <li id="signinSpan" @click="titleChange()"  :class="{ loginSpanChange:!show }">
          <span><strong>注册</strong></span>
        </li>
      </router-link>
    </ul>
  </div>
  <div class="logSign"><router-view></router-view></div>
</template>

<script>
</script>

<style>
  .logTitle {
    width: 100%;
    height: 59px;
    font-size: 5px;
    border-top-left-radius: 2em;
    border-top-right-radius: 2em;
  }
  .logTitle ul {
    border-top-left-radius: 2em;
    border-top-right-radius: 2em;
    float: left;
    list-style: none;
    font-size: 5px;
    width: 100%;
    height: 100%;
    text-align: center;
    padding-left: 0;
    margin-top: 0px;
    background-color: rgba(255, 255, 255, 0.8);
  }
  .logTitle ul li {
    width: 50%;
    height: 100%;
    margin-left: 0px;
    margin-top: 0;
    float: left;
    cursor: pointer;
    border-top-left-radius: 2em;
    border-top-right-radius: 2em;
  }
  .loginSpanChange {
    background-color: #ffffff;
  }
  .logTitle span {
    font-size: 6em;
  }
  .logSign {
    position: absolute;
    width: 424px;
    height: 341px;
    background-color: rgba(255, 255, 255, 0.8);
    border-bottom-left-radius: 2em;
    border-bottom-right-radius: 2em;
  }
</style>
