<template>
  <page-layout>
    <a-card :bordered="false">
      <div>
        <a-tabs size="large" :tabBarStyle="{ textAlign: 'center' }" @change="onTabChange" style="padding: 0 10px;">
          <a-tab-pane key="1" tab="家教列表">
            <a-list item-layout="horizontal">
              <a-list-item v-for="(teacher, index) in teachers" :key="index">
                <a-list-item-meta :title="teacher.name"></a-list-item-meta>
                <div slot="actions">
                  <router-link :to="{ name: '家教主页', params: { id: teacher.id } }">
                    <a-button type="link">家教主页</a-button>
                  </router-link>
                  <a-button type="link" @click="showDeleteMessageForTeacher(teacher.id)">删除</a-button>
                </div>
              </a-list-item>
            </a-list>
          </a-tab-pane>
          <a-tab-pane key="2" tab="学生列表">
            <a-list item-layout="horizontal">
              <a-list-item v-for="(student, index) in students" :key="index">
                <a-list-item-meta :title="student.name"></a-list-item-meta>
                <div slot="actions">
                  <router-link :to="{ name: '学生主页', params: { id: student.id } }">
                    <a-button type="link">学生主页</a-button>
                  </router-link>
                  <a-button type="link" @click="showDeleteMessageForStudent(student.id)">删除</a-button>
                </div>
              </a-list-item>
            </a-list>
          </a-tab-pane>
        </a-tabs>
      </div>
    </a-card>

    <a-modal :visible="deleteOpen" title="警告" @ok="handleDeleteOk" @cancel="handleDeleteCancel">
      <p>您确认要删除该用户吗？</p>
    </a-modal>
  </page-layout>
</template>

<script>
import { mapState } from 'vuex'
import PageLayout from '@/layouts/PageLayout'
import { getAllTeachers, getAllStudents, deleteUser } from '@/services/user'

export default {
  name: 'manageUserPage',
  computed: {
    ...mapState('account', { currUser: 'user' })
  },
  components: { PageLayout },
  created() {
    this.fetchAllTeachers();
    this.fetchAllStudents();
  },
  data() {
    return {
      deleteOpen: false,
      curUserId: null,
      isTeacher: null,
      teachers: [],
      students: []
    }
  },
  methods: {
    fetchAllTeachers() {
      getAllTeachers(this.currUser.id).then(res => {
        if (res.data.code >= 0) {
          this.teachers = res.data.teachers;
          console.log('获取家教信息成功:', this.teachers);
        } else {
          console.error('获取家教信息失败');
        }
      }).catch(error => {
        console.error('获取家教信息失败:', error);
      });
    },
    fetchAllStudents() {
      getAllStudents(this.currUser.id).then(res => {
        if (res.data.code >= 0) {
          this.students = res.data.students;
          console.log('获取学生信息成功:', this.students);
        } else {
          console.error('获取学生信息失败');
        }
      }).catch(error => {
        console.error('获取学生信息失败:', error);
      });
    },
    showDeleteMessageForTeacher(id) {
      this.deleteOpen = true;
      this.curUserId = id;
      this.isTeacher = true;
    },
    showDeleteMessageForStudent(id) {
      this.deleteOpen = true;
      this.curUserId = id;
      this.isTeacher = false;
    },
    handleDeleteOk() {
      this.deleteOpen = false;
      deleteUser(this.curUserId).then(res => {
        if (res.data.code >= 0) {
          if (this.isTeacher) {
            this.fetchAllTeachers();
          } else {
            this.fetchAllStudents();
          }
          console.log('删除用户成功');
        } else {
          console.error('删除用户失败');
        }
      }).catch(error => {
        console.error('删除用户失败:', error);
      });
    },
    handleDeleteCancel() {
      this.deleteOpen = false;
    }
  },
}
</script>

<style lang="less" scoped>
.page-layout {
  padding: 20px;
}

.content {
  .detail {
    line-height: 22px;
    max-width: 900px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: normal;
    transition: max-height 0.3s ease, white-space 0.3s ease;

    &.expanded {
      max-height: none;
      overflow: visible;
      text-overflow: clip;
    }
  }

  .read-more,
  .read-less {
    margin-top: 8px;
    cursor: pointer;
    color: @primary-color; // 使用主题颜色
  }
}

.demo-loadmore-list {
  min-height: 350px;
}
</style>
