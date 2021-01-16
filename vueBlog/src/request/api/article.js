import base from './base.js'
import axios from '../html.js'

const article={
  //新闻列表
  articleList(){
    return axios.get('${base.news}')
  },
  //新闻内容
  articleContent(params){
    return axios.get('${base.newsContent}'),{
      params:params
    }
  },
  //登录
  login(parmas){
    return axios.post('${base.login}'),{
      params:params
    }
  }
}


export default article;
