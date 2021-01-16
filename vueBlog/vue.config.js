const webpack = require('webpack')

module.exports = {
  lintOnSave: false,
  devServer: {
    hot: true,
    open: true,
    port: 8080,
    host: "127.0.0.1"
  },
  chainWebpack: config => {
    config.plugin('provide').use(webpack.ProvidePlugin, [{
      $: 'jquery',
      jquery: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery'
    }])
  },
  devServer: {
      proxy: {
        '/api': {
          target: 'http://127.0.0.1:8000', //目标路径，别忘了加http和端口号
          changeOrigin: true, //是否跨域
          ws: true,
          pathRewrite: {
            '^/api': '' //重写路径
          }
        }
      }
    }
}
