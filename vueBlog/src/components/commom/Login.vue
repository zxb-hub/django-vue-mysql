<template>
  <div class="login" id="login">
    <form class="loginForm" action="loginJudge" method="POST">
      <div>
        <input type="text" name="username" id="login_usn" placeholder="请输入用户名" />
        <div class="login_alert" style="color: red;"></div>
      </div>
      <div>
        <input type="password" name="password" id="login_psw" placeholder="请输入密码" />
        <div class="login_alert" style="color: red;"></div>
      </div>
      <input type="submit" class="button" value="提交" />
    </form>
  </div>
</template>

<script></script>

<style>
.login {
  width: 100%;
  height: 100%;
  position: absolute;
}
.loginForm {
  height: 100%;
  margin-top: 2px;
  width: 90%;
  margin-left: 5%;
}
.loginForm div {
  margin-bottom: 1.5em;
}
.loginForm input {
  height: 46px;
  width: 84%;
  margin-left: 0%;
  border: 2px solid #f8f9fa;
  background-color: rgba(255, 255, 255, 2);
  padding: 0.5rem 1.5rem;
  margin-top: 23px;
}
.loginForm input[type='submit'] {
  border: 2px solid #87dc49 !important;
  background-color: #87dc49;
  font-size: 16px;
  border-radius: 4px;
  padding: 8px 30px;
  width: 110px;
  height: 40px;
  margin-left: 0px;
  cursor: pointer;
  margin-bottom: 1cm;
}
</style>
