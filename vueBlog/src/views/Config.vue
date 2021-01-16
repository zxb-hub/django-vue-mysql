<template>
  <div>
    <el-container style="height: 500px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <el-menu-item>
              <router-link>
                <i class="el-icon-message"></i>
                已注册用户管理
              </router-link>
            </el-menu-item>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-menu"></i>
              文章管理
            </template>
            <el-menu-item-group>
              <router-link><el-menu-item index="2-1">上传文章</el-menu-item></router-link>
              <router-link><el-menu-item index="2-2">修改文章</el-menu-item></router-link>
              <router-link><el-menu-item index="2-3">删除文章</el-menu-item></router-link>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown"><el-dropdown-item>注销并退出</el-dropdown-item></el-dropdown-menu>
          </el-dropdown>
          <span></span>
        </el-header>
        <el-main><router-view></router-view></el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script></script>

<style></style>
