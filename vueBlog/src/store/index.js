import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
// import Qs from 'qs';
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token')||'', //初始化token
    user: localStorage.getItem('user')||''
  },


  getters: {
    // !!将state.token强制转换为布尔值，若state.token存在且不为空(已登录)则返回true，反之返回false
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status
  },
  mutations: {
    auth_request(state) {
      state.status = 'loading';
    },
    auth_success(state, token) {
      state.status = 'success';
      localStorage.setItem('token', token)
      state.token = token;
    },
    success_usename(state, user) {
      state.user = user;
      localStorage.setItem('user', user)
    },
    auth_error(state) {
      state.status = 'error';
    },
    logout(state) {
      state.status = '';
      state.token = '';
      state.user = ''
    },




  },

  actions: {
    login({
      commit
    }, params) {
      //
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.get('/api/csrf').then(res => {
          // 先获取后台cookie
          let csrftoken = res.data.token;
          console.log('params1:',params)
          console.log('params2:',csrftoken)
          axios.post('/api/login', params, {
              headers: {
                'X-CSRFtoken': csrftoken,
                'Content-Type': 'application/x-www-form-urlencoded'
              }
            }).then(res => {
              localStorage.setItem('token', res.data.token)
              // 每次请求接口时，需要在headers添加对应的Token验证
              axios.defaults.headers.common['Authorization'] = res.data.token
              // 更新token
              commit('auth_success', res.data.token)
              commit('success_usename', res.data.name)
              resolve('完成')
            })
            .catch(err => {
              commit('auth_error')
              localStorage.removeItem('token')
              reject('失败', err)
              console.log(err)
            })
        })
      })
    },
    logout({
      commit
    },user) {
      console.log(user)
      // let param = {
      //   username : user
      // };
      // console.log(param)
      return new Promise((resolve,reject) => {
        // console.log('param2:',param),
        axios.get('/api/logout')
          .then(response => {
            localStorage.removeItem('token');
            localStorage.removeItem('user');
            // 移除之前在axios头部设置的token,现在将无法执行需要token的事务
            delete axios.defaults.headers.common['Authorization'];
            commit('logout')
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },


    signin({commit},data){
      return new Promise((resolve) => {
        localStorage.setItem('token', data.token)
        // 每次请求接口时，需要在headers添加对应的Token验证
        axios.defaults.headers.common['Authorization'] = data.token
        // 更新token
        commit('auth_success', data.token)
        commit('success_usename', data.name)
        resolve('完成')
        })
    }
  },
  modules: {},
});
