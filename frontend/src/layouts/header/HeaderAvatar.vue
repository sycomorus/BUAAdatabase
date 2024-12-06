<template>
  <div>
    <a-dropdown>
      <div class="header-avatar" style="cursor: pointer">
        <span class="name">{{ user.name }}</span>
      </div>
      <a-menu :class="['avatar-menu']" slot="overlay">
        <!-- 条件渲染：仅当用户角色为 student 或 teacher 时显示 -->
        <template v-if="isStudentOrTeacher">
          <a-menu-item @click="toPersonalPage">
            <a-icon type="user" />
            <span>个人主页</span>
          </a-menu-item>
          <a-menu-item @click="toEditPersonalPage">
            <a-icon type="edit" />
            <span>编辑个人主页</span>
          </a-menu-item>
          <a-menu-divider />
          <a-menu-item @click="toResetPassword">
            <a-icon type="lock" />
            <span>修改密码</span>
          </a-menu-item>
        </template>
        <a-menu-item @click="logout">
          <a-icon style="margin-right: 8px;" type="poweroff" />
          <span>退出登录</span>
        </a-menu-item>
      </a-menu>
    </a-dropdown>
    <a-modal title="修改密码" :visible="isModalVisible" @ok="handleOk" @cancel="handleCancel">
      <a-form :form="passwordForm">
        <a-form-item :label="'旧密码'" :labelCol="{ span: 7 }" :wrapperCol="{ span: 10 }" :required=false>
          <a-input :placeholder="'请输入旧密码'" type="password"
            v-decorator="['oldPassword', { rules: [{ required: true, message: '请输入旧密码', whitespace: true }], validateTrigger: 'onSubmit' }]" />
        </a-form-item>
        <a-form-item :label="'新密码'" :labelCol="{ span: 7 }" :wrapperCol="{ span: 10 }" :required=false>
          <a-input :placeholder="'请输入新密码'" type="password"
            v-decorator="['newPassword', { rules: [{ required: true, message: '请输入新密码', whitespace: true }], validateTrigger: 'onSubmit' }]" />
        </a-form-item>
        <a-form-item :label="'确认密码'" :labelCol="{ span: 7 }" :wrapperCol="{ span: 10 }" :required=false>
          <a-input :placeholder="'请确认密码'" type="password"
            v-decorator="['confirmedPassword', { rules: [{ required: true, message: '请确认密码', whitespace: true }], validateTrigger: 'onSubmit' }]" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { logout,resetPassword } from '@/services/user'
import { mapState } from 'vuex'

export default {
  name: 'HeaderAvatar',
  computed: {
    ...mapGetters('account', ['user']),
    ...mapState('account', { currRoles: 'roles' }),
    ...mapState('account', { currUser: 'user' }),
    isStudentOrTeacher() {
      return this.currRoles.some(role => role.id === 'student' || role.id === 'teacher');
    }
  },
  data() {
    return {
      isModalVisible: false, // 控制 a-modal 显示状态的变量
      passwordForm: this.$form.createForm(this),
    };
  },
  methods: {
    logout() {
      logout()
      this.$router.push('/login')
    },
    toPersonalPage() {
      console.log(this.currRoles[0].id)
      if (this.currRoles[0].id === 'student') {
        this.$router.push({ name: '学生主页', params: { id: this.user.id } })
      } else if (this.currRoles[0].id === 'teacher') {
        this.$router.push({ name: '家教主页', params: { id: this.user.id } })
      }
    },
    toEditPersonalPage() {
      if (this.currRoles[0].id === 'student') {
        this.$router.push({ name: '编辑学生主页', params: { id: this.user.id } })
      } else if (this.currRoles[0].id === 'teacher') {
        this.$router.push({ name: '编辑家教主页', params: { id: this.user.id } })
      }
    },
    toResetPassword() {
      this.isModalVisible = true; // 显示 a-modal
    },
    handleOk() {
      this.passwordForm.validateFields((err, values) => {
        if (!err) {
          console.log('Received values of form: ', values);
          const { oldPassword, newPassword, confirmedPassword } = values;
          if (newPassword !== confirmedPassword) {
            this.$message.error('两次输入的密码不一致');
          } else {
            resetPassword(this.currUser.id, oldPassword, newPassword).then(res => {
              const data = res.data;
              if (data.code === 0) {
                this.$message.success('修改密码成功');
                this.passwordForm.resetFields();
                this.isModalVisible = false; // 隐藏 a-modal
                logout();
                this.$router.push('/login')
              } else {
                this.$message.error(data.message);
              }
            });
          }
        }
      });
    },
    handleCancel() {
      this.passwordForm.resetFields();
      this.isModalVisible = false; // 隐藏 a-modal
    },
  }
}
</script>

<style lang="less">
.header-avatar {
  display: inline-flex;

  .avatar,
  .name {
    align-self: center;
  }

  .avatar {
    margin-right: 8px;
  }

  .name {
    font-weight: 500;
  }
}

.avatar-menu {
  width: 150px;
}
</style>
