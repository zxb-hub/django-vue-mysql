<template>
  <div class="signin" id="signin">
    <form action="signin" id="signinForm" class="signinForm" method="POST">
      <div><input type="text" placeholder="用户昵称" v-model="username" /></div>
      <div><input type="password" placeholder="设置密码" v-model="password" /></div>
      <div><input type="password" placeholder="确认密码" v-model="is_password" /></div>
      <input type="submit" class="button" value="提交" />
    </form>
  </div>
</template>

<script>
export default {
  name: 'signin',
  data() {
    return {
      username: '',
      password: '',
      is_password: ''
    };
  },
  
};
</script>

<style>
main.el-main {
  padding-top: 20px;
  padding-bottom: 0.125rem;
}
.signin {
  width: 100%;
  height: 100%;
  position: absolute;
}
.signinForm {
  width: 90%;
  margin-left: 5%;
  height: auto;
  margin-top: 2px;
}
.signinForm div {
  margin-bottom: 0px;
}
.signinForm input {
  height: 46px;
  width: 75%;
  margin-left: 0%;
  border: 2px solid #f8f9fa;
  background-color: rgba(255, 255, 255, 2);
  padding: 0.5rem 1.5rem;
  margin-top: 22px;
}
.signinForm input[type='submit'] {
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
