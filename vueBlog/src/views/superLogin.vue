<template>
  <div>
    <el-form :label-position="labelPosition" label-width="80px" :model="formLabelAlign">
      <el-form-item label="用户名"><el-input v-model="superUser.name"></el-input></el-form-item>
      <el-form-item label="密码"><el-input v-model="superUser.psw"></el-input></el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      labelPosition: 'right',
      superUser: {
        name: '',
        psw: ''
      }
    };
  },
  methods: {
    resetForm: function(formName) {
      this.$refs[formName].resetFields();
    }
  }
};
</script>

<style></style>
