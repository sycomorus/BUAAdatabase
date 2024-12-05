<template>
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
      </template>
      <a-menu-item @click="logout">
        <a-icon style="margin-right: 8px;" type="poweroff" />
        <span>退出登录</span>
      </a-menu-item>
    </a-menu>
  </a-dropdown>
</template>

<script>
import { mapGetters } from 'vuex'
import { logout } from '@/services/user'
import { mapState } from 'vuex'

export default {
  name: 'HeaderAvatar',
  computed: {
    ...mapGetters('account', ['user']),
    ...mapState('account', { currRoles: 'roles' }),
    isStudentOrTeacher() {
      return this.currRoles.some(role => role.id === 'student' || role.id === 'teacher');
    }
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
    }
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
