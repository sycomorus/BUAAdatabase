<template>
  <common-layout>
    <div class="top">
      <div class="header">
        <img alt="logo" class="logo" src="@/assets/img/logo_black.png" />
        <span class="title">{{ systemName }}</span>
      </div>
      <div class="desc">一对一上门家教</div>
    </div>
    <div class="login">
      <a-tabs size="large" :tabBarStyle="{ textAlign: 'center' }" @change="onTabChange" style="padding: 0 2px;">
        <a-tab-pane tab="用户登录" key="1">
          <a-alert type="error" :closable="true" v-show="errorLogin" :message="errorLogin" showIcon
            style="margin-bottom: 24px;" />
          <a-form @submit="handleLogin" :form="loginForm">
            <a-form-item>
              <a-input autocomplete="autocomplete" size="large" placeholder="用户名"
                v-decorator="['name', { rules: [{ required: true, message: '请输入账户名', whitespace: true }] }]">
                <a-icon slot="prefix" type="user" />
              </a-input>
            </a-form-item>
            <a-form-item>
              <a-input size="large" placeholder="密码" autocomplete="autocomplete" type="password"
                v-decorator="['password', { rules: [{ required: true, message: '请输入密码', whitespace: true }] }]">
                <a-icon slot="prefix" type="lock" />
              </a-input>
            </a-form-item>
            <a-form-item>
              <a-button :loading="logging" style="width: 100%;margin-top: 24px" size="large" htmlType="submit"
                type="primary">确定</a-button>
            </a-form-item>
          </a-form>
        </a-tab-pane>
        <a-tab-pane tab="用户注册" key="2">
          <a-alert type="error" :closable="true" v-show="errorRegister" :message="errorRegister" showIcon
            style="margin-bottom: 24px;" />
          <a-form @submit="handleRegister" :form="registerForm">
            <a-form-item>
              <a-input autocomplete="autocomplete" size="large" placeholder="用户名"
                v-decorator="['registerName', { rules: [{ required: true, message: '请输入账户名', whitespace: true }] }]">
                <a-icon slot="prefix" type="user" />
              </a-input>
            </a-form-item>
            <a-form-item>
              <a-input size="large" placeholder="密码" autocomplete="autocomplete" type="password"
                v-decorator="['registerPassword', { rules: [{ required: true, message: '请输入密码', whitespace: true }] }]">
                <a-icon slot="prefix" type="lock" />
              </a-input>
            </a-form-item>
            <a-form-item>
              <a-input size="large" placeholder="确认密码" autocomplete="autocomplete" type="password"
                v-decorator="['confirmedPassword', { rules: [{ required: true, message: '请确认密码', whitespace: true }] }]">
                <a-icon slot="prefix" type="lock" />
              </a-input>
            </a-form-item>
            <a-form-item>
              <a-radio-group v-decorator="['role', { rules: [{ required: true, message: '请选择身份角色' }] }]">
                <a-radio value="teacher">我是老师</a-radio>
                <a-radio value="student">我是学生</a-radio>
              </a-radio-group>
            </a-form-item>
            <a-form-item>
              <a-button :loading="logging" style="width: 100%;margin-top: 24px" size="large" htmlType="submit"
                type="primary">确定</a-button>
            </a-form-item>
          </a-form>
        </a-tab-pane>
      </a-tabs>
    </div>
  </common-layout>
</template>

<script>
import CommonLayout from '@/layouts/CommonLayout'
import { login, register, getAvatar } from '@/services/user'
import { setAuthorization } from '@/utils/request'
import { mapMutations } from 'vuex'

export default {
  name: 'Login',
  components: { CommonLayout },
  data() {
    return {
      role: 'student',
      logging: false,
      name: '',
      errorLogin: '',
      errorRegister: '',
      currentTab: '1',
      loginForm: this.$form.createForm(this),
      registerForm: this.$form.createForm(this)
    }
  },
  computed: {
    systemName() {
      return this.$store.state.setting.systemName
    }
  },
  methods: {
    ...mapMutations('account', ['setRoles', 'setUser']),
    onTabChange(key) {
      this.currentTab = key;
    },
    handleLogin(e) {
      e.preventDefault();
      this.loginForm.validateFields((err) => {
        if (!err) {
          this.logging = true;
          this.name = this.loginForm.getFieldValue('name');
          const password = this.loginForm.getFieldValue('password');
          login(this.name, password).then(this.afterLogin);
        }
      });
    },
    handleRegister(e) {
      e.preventDefault();
      this.registerForm.validateFields((err) => {
        if (!err) {
          this.logging = true;
          this.name = this.registerForm.getFieldValue('registerName');
          const password = this.registerForm.getFieldValue('registerPassword');
          const confirmedPassword = this.registerForm.getFieldValue('confirmedPassword');
          const role = this.registerForm.getFieldValue('role');
          if (password !== confirmedPassword) {
            this.errorRegister = '两次密码输入不一致';
            this.logging = false;
            return;
          }
          register(this.name, password, role).then(this.afterRegister);
        }
      });
    },
    afterLogin(res) {
      this.logging = false
      const loginRes = res.data
      if (loginRes.code >= 0) {
        const roles = loginRes.data.roles
        getAvatar(loginRes.data.id).then(response => {
          if (response.data.code >= 0) {
            const avatar = response.data.avatar
            console.log(avatar)
            this.setRoles(roles)
            const user = { name: this.name, id: loginRes.data.id, avatar: avatar }
            this.setUser(user)
            setAuthorization({ token: loginRes.data.token })
            this.$router.push('/announcementPage')
            this.$message.success("欢迎回来", 3)
          } else {
            this.$error("未知错误")
          }
        })
      } else {
        this.errorLogin = '用户名或密码错误'
      }
    },
    afterRegister(res) {
      this.logging = false
      const registerRes = res.data
      if (registerRes.code >= 0) {
        const roles = registerRes.data.roles
        this.setRoles(roles)
        const user = { name: this.name, id: registerRes.data.id }
        this.setUser(user)
        setAuthorization({ token: registerRes.data.token })
        this.$router.push('/announcementPage')
        this.$message.success("欢迎加入家教综合服务平台", 3)
      } else {
        this.errorRegister = '用户名已被注册'
      }
    }
  }
}
</script>

<style lang="less" scoped>
.common-layout {
  .top {
    text-align: center;

    .header {
      height: 44px;
      line-height: 44px;

      a {
        text-decoration: none;
      }

      .logo {
        height: 44px;
        vertical-align: top;
        margin-right: 16px;
      }

      .title {
        font-size: 33px;
        color: @title-color;
        font-family: 'Myriad Pro', 'Helvetica Neue', Arial, Helvetica, sans-serif;
        font-weight: 600;
        position: relative;
        top: 2px;
      }
    }

    .desc {
      font-size: 14px;
      color: @text-color-second;
      margin-top: 12px;
      margin-bottom: 20px;
    }
  }

  .login {
    width: 368px;
    margin: 0 auto;

    @media screen and (max-width: 576px) {
      width: 95%;
    }

    @media screen and (max-width: 320px) {
      .captcha-button {
        font-size: 14px;
      }
    }

    .icon {
      font-size: 24px;
      color: @text-color-second;
      margin-left: 16px;
      vertical-align: middle;
      cursor: pointer;
      transition: color 0.3s;

      &:hover {
        color: @primary-color;
      }
    }
  }
}
</style>
