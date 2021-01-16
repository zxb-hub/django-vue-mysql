<template>
  <div class="background" style="width: 100%;min-height:500px;">
    <div class="logBox">
      <div v-if="showlogin">
        <el-form  label-width="80px">
          <h3>登录</h3>
          <el-divider></el-divider>
          <el-form-item label="用户名"><el-input class="SLin_el-input" v-model="name" type="text" placeholder="请输入用户名"></el-input></el-form-item>
          <el-form-item label="密码"><el-input class="SLin_el-input" v-model="psw" type="password" placeholder="请输入密码"></el-input></el-form-item>
          <el-button type="primary" @click="login" style="margin-left: 0;margin-top: 10px;">登录</el-button>
          <br />
          <el-link @click="change()" style='margin-top: 15px;'>没有账号?点此注册</el-link>
        </el-form>
      </div>
      <div v-if="showsignin">
        <el-form  label-width="80px">
          <h3>注册</h3>
          <el-divider></el-divider>
          <el-form-item label="用户名"><el-input v-model="name" class="SLin_el-input" type="text" placeholder="请输入用户名"></el-input></el-form-item>
          <el-form-item label="密码"><el-input v-model="psw" class="SLin_el-input" type="password" placeholder="请输入密码"></el-input></el-form-item>
          <el-form-item label="确认密码"><el-input v-model="is_psw" class="SLin_el-input" type="password" placeholder="请确认密码"></el-input></el-form-item>
          <el-form-item label="手机号"><el-input v-model="phone" class="SLin_el-input" type="password" placeholder="手机号" maxlength="11" minlength="11"></el-input></el-form-item>
          <el-button type="primary" @click="signin" style="margin: 0;">注册</el-button>
          <br />
          <el-link @click="change()">已有账号?点此登录</el-link>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from '../request/html.js';
import qs from 'qs';
import { Toast } from 'vant';
export default {
  name: 'SLin',
  data() {
    return {
      showsignin: false,
      showlogin: true,
      phone: '',
      psw: '',
      is_psw: '',
      name: ''
    };
  },
  methods: {
    login: function() {
      if (this.name == '' || this.psw == '') {
        Toast('请输入用户名及密码');
      } else {
        let params = {
          username: this.name,
          password: this.psw
        };
        this.$store
          .dispatch('login', params)
          .then(() => {
            if (this.$store.state.token) {
              this.$router.push({
                path: '/home'
              });
              Toast('登陆成功');
            } else {
              this.name = '';
              this.psw = '';
              Toast('用户名密码错误,请检查后重新登录');
            }
          })
          .catch(error => {
            console.log(error.response);
          });
      }
    },
    change: function() {
      this.showsignin = !this.showsignin;
      this.showlogin = !this.showlogin;
    },
    signin: function() {
      if (this.name == '' || this.psw == '') {
        Toast('请输入用户名及密码');
      } else if (this.phone.length != 11) {
        Toast('请输入正确手机号');
      } else if (this.psw != this.is_psw) {
        Toast('两次密码输入不一致,请确认后重新输入');
      } else {
        axios.get('/api/csrf').then(res => {
          // 先获取后台cookie
          let csrftoken = res.data.token;
          let data = {
            username: this.name,
            password: this.psw,
            phone: this.phone
          };
          axios.post('/api/signin', qs.stringify(data), { header: { 'X-CSRFtoken': csrftoken, 'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8' } }).then(res => {
            if (res.data.msg == 0) {
              this.$store.dispatch('signin',res.data)
              this.$router.push({ path: '/home' });
            } else if (res.data.msg == 1) {
              Toast( '用户名已存在,请重新选择用户名');
            } else if (res.data.msg == 2) {
              Toast('手机号已存在,请重新输入手机号');
            }
          });
        });
      }
    }
  }
};
</script>

<style>
.background {
  background-image: url(../assets/background-img/login.jpg);
  margin: 0;
}
.logBox {
  width: 424px;
  height: 452px;
  text-align: center;
  border-radius: 2em;
  position: absolute;
  top: 106px;
  left: 423px;
  background-color: rgba(255, 255, 255, 0.9);
}
.SLin_el-input{
  width: 80%;
}
.el-form {
  width: 100%;
  height: 354px;
}
.SLinInput {
  width: 262px;
  left: 0;
  float: left;
  margin-left: 2.625rem;
}
.demo-ruleForm p {
  width: 7.25rem;
  float: left;
  margin-top: 2rem;
}
.demo-ruleForm button {
  margin-left: 0px;
}
.el-form-item__label{
  width: 100px;
}
#el-link {
  top: 10px;
}
</style>
