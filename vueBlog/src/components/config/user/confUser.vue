<template>
  <div>
    <el-table :data="userData" border style="width: 100%">
      <el-table-column fixed prop="date" label="注册日期" width="150"></el-table-column>
      <el-table-column prop="username" label="姓名" width="120"></el-table-column>
      <el-table-column prop="phone" label="电话" width="120"></el-table-column>
      <el-table-column prop="super" label="权限" width="120"></el-table-column>
      <el-table-column fixed="right" label="操作" width="100">
        <template slot-scope="scope">
          <el-button type="primary" icon="el-icon-edit" circle></el-button>
          <el-button type="danger" icon="el-icon-delete" circle></el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-button type="primary" plain @click="adduser = true">新建用户</el-button>
    <el-dialog title="创建新用户" :visible.sync="adduser">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="用户名"><el-input v-model="name"></el-input></el-form-item>
        <el-form-item label="密码"><el-input v-model="psw"></el-input></el-form-item>
        <el-form-item label="手机号"><el-input v-model="phone"></el-input></el-form-item>
        <el-form-item label="特殊资源">
          <el-radio-group v-model="superuser">
            <el-radio label="普通用户"></el-radio>
            <el-radio label="超级用户"></el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">立即创建</el-button>
          <el-button>取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
export default{
  name:'addUser',
  data(){
    return{
      name:'',
      psw:'',
      phone:'',
      superuser:'',
      adduser:false
    }
  },
}
</script>

<style></style>
