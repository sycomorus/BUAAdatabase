<template>
  <page-layout>
    <a-card :bordered="false">
      <div>
        <a-tabs size="large" :tabBarStyle="{ textAlign: 'center' }" @change="onTabChange" style="padding: 0 10px;">
          <a-tab-pane :key="1" tab="我的帖子">
            <a-list item-layout="horizontal">
              <a-list-item v-for="(post, index) in posts" :key="index">
                <a-list-item-meta :title="post.title">
                  <div slot="description">
                    <div class="content">
                      <div class="detail" :class="{ 'expanded': showFullContent === post.id }">
                        {{ showFullContent === post.id || !shouldShowReadMore(post.content) ?
                          post.content :
                          post.content.slice(0, 60) + '...' }}
                      </div>
                      <div class="read-more" v-if="shouldShowReadMore(post.content) && showFullContent !== post.id">
                        <a @click="showFullContent = post.id">显示更多</a>
                      </div>
                      <div class="read-less" v-if="showFullContent === post.id">
                        <a @click="showFullContent = null">收起</a>
                      </div>
                    </div>
                  </div>
                </a-list-item-meta>
                <div slot="actions">
                  <router-link :to="{ name: '帖子详情', params: { id: post.id, showAccept: false } }">
                    <a-button type="link">详情</a-button>
                  </router-link>
                  <a-button type="link" @click="showDeleteMessage(post.id)">删除</a-button>
                </div>
              </a-list-item>
            </a-list>
          </a-tab-pane>
          <a-tab-pane key="2" tab="我的家教">
            <a-list item-layout="horizontal">
              <a-list-item v-for="(teacher, index) in teachers" :key="index">
                <a-list-item-meta :title="teacher.name"></a-list-item-meta>
                <div slot="actions">
                  <router-link :to="{ name: '家教主页', params: { id: teacher.id } }">
                    <a-button type="link">家教主页</a-button>
                  </router-link>
                  <a-button type="link" @click="setComment(teacher.id)">发表评价</a-button>
                  <a-button type="link" @click="showUnlinkStudentMessage(teacher.id)">解除师生关系</a-button>
                </div>
              </a-list-item>
            </a-list>
          </a-tab-pane>
          <a-tab-pane key="3" tab="我的待办">
            <a-list item-layout="horizontal">
              <a-list-item v-for="(todo, index) in todos" :key="index">
                <div>
                  您发布的招聘帖
                  <router-link :to="{ name: '帖子详情', params: { id: todo.postId, showAccept: false } }">“{{
                    todo.postTitle }}”</router-link>
                  被用户<router-link :to="{ name: '家教主页', params: { id: todo.accepterId } }">“{{ todo.accepterName
                    }}”</router-link>
                  所接受
                </div>
                <div slot="actions">
                  <a-button type="link" @click="showAcceptMessgae(todo.accepterId)">接受</a-button>
                  <a-button type="link" @click="showRefuseMessage(todo.accepterId)">拒绝</a-button>
                </div>
              </a-list-item>
            </a-list>
          </a-tab-pane>
          <a-tab-pane key="4" tab="我的学习资料">
            <a-list item-layout="horizontal">
              <a-list-item v-for="(material, index) in learningMaterials" :key="index">
                <a-list-item-meta :title="material.filename">
                  <div slot="description">来自<strong>{{ material.publisher}}</strong>   {{material.date }}</div>
                </a-list-item-meta>
                <div slot="actions">
                <a :href = material.downloadLink tatget="_blank">
                  <a-button type="link">下载</a-button>
                </a>
                </div>
              </a-list-item>
            </a-list>
          </a-tab-pane>
        </a-tabs>
      </div>
    </a-card>

    <!-- 删除帖子模态框 -->
    <a-modal :visible="deleteOpen" title="警告" @ok="handleDeleteOk" @cancel="handleDeleteCancel">
      <p>您确认要删除该帖子吗？</p>
    </a-modal>

    <!-- 解除师生关系模态框 -->
    <a-modal :visible="unlinkOpen" title="警告" @ok="handleUnlinkOk" @cancel="handleUnlinkCancel">
      <p>您确认要解除与该家教的关系吗？</p>
    </a-modal>
    <!-- 接受学生求职请求模态框 -->
    <a-modal :visible="acceptOpen" title="提示" @ok="handleAcceptOk" @cancel="handleAcceptCancel">
      <p>您确认要接受该用户的请求吗？</p>
    </a-modal>
    <!-- 拒绝学生求职请求模态框 -->
    <a-modal :visible="refuseOpen" title="提示" @ok="handleRefuseOk" @cancel="handleRefuseCancel">
      <p>您确认要拒绝该用户的请求吗？</p>
    </a-modal>
    <!-- 发布评价抽屉 -->
    <a-drawer :visible="drawerOpen" class="custom-class" root-class-name="root-class-name"
      :root-style="{ color: 'blue' }" style="color: red" title="发布评价" placement="right" @close="closeDrawer">
      <form @submit.prevent="submitComment">
        <a-form-item label="星级">
          <a-rate v-model=rate allow-half />
        </a-form-item>
        <a-form-item label="评价">
          <a-textarea v-model=comment placeholder="请输入你的评价" auto-size />
        </a-form-item>
        <a-form-item>
          <a-button type="primary" html-type="submit">提交</a-button>
        </a-form-item>
      </form>
    </a-drawer>
  </page-layout>
</template>

<script>
import { mapState } from 'vuex'
import PageLayout from '@/layouts/PageLayout'
import { getUserPosts, deletePost, getTeachers, unlink, submitComment, getTodos, link, refuseLink, getLearningMaterials } from '@/services/user'

export default {
  name: 'studentWorkPage',
  computed: {
    ...mapState('account', { currUser: 'user' })
  },
  components: { PageLayout },
  created() {
    this.fetchUserPosts();
    this.fetchTeachers();
    this.fetchTodos();
    this.fetchLearningMaterials();
  },
  data() {
    return {
      activeKey: 1,
      posts: [],
      showFullContent: null, // 控制显示完整内容的帖子ID
      deleteOpen: false,
      unlinkOpen: false, // 控制解除师生关系模态框
      curPostId: null,
      curTeacherId: null,
      teachers: [],
      drawerOpen: false,
      rate: 4.5,
      comment: "",
      todos: [],
      learningMaterials: [],
      curAccepterId: null,
      curRefuseId: null,
      acceptOpen: false,
      refuseOpen: false
    }
  },
  methods: {
    onTabChange(key) {
      this.activeKey = key;
    },
    fetchTodos() {
      getTodos(this.currUser.id).then(res => {
        if (res.data.code >= 0) {
          this.todos = res.data.todos;
          console.log('获取待办事项成功:', this.todos);
        } else {
          console.error('获取待办事项失败');
        }
      }).catch(error => {
        console.error('获取待办事项失败:', error);
      });
    },
    fetchTeachers() {
      getTeachers(this.currUser.id).then(res => {
        if (res.data.code >= 0) {
          this.teachers = res.data.teachers;
          console.log('获取学生信息成功:', this.teachers);
        } else {
          console.error('获取学生信息失败');
        }
      }).catch(error => {
        console.error('获取学生信息失败:', error);
      });
    },
    fetchUserPosts() {
      getUserPosts(this.currUser.id).then(res => {
        if (res.data.code >= 0) {
          this.posts = res.data.posts;
          console.log('获取帖子信息成功:', this.posts);
        } else {
          console.error('获取帖子信息失败');
        }
      }).catch(error => {
        console.error('获取帖子信息失败:', error);
      });
    },
    fetchLearningMaterials() {
      getLearningMaterials(this.currUser.id).then(res => {
        if (res.data.code >= 0) {
          this.learningMaterials = res.data.materials;
          console.log('获取学习资料成功:', this.learningMaterials);
        } else {
          console.error('获取学习资料失败');
        }
      }).catch(error => {
        console.error('获取学习资料失败:', error);
      });
    },
    shouldShowReadMore(content) {
      return content.length > 60; // 判断内容长度
    },
    showDeleteMessage(id) {
      this.deleteOpen = true;
      this.curPostId = id;
    },
    handleDeleteOk() {
      this.deleteOpen = false;
      deletePost(this.curPostId).then(res => {
        if (res.data.code >= 0) {
          this.fetchUserPosts();
          console.log('删除帖子成功');
        } else {
          console.error('删除帖子失败');
        }
      }).catch(error => {
        console.error('删除帖子失败:', error);
      });
    },
    handleDeleteCancel() {
      this.deleteOpen = false;
    },
    showUnlinkStudentMessage(id) {
      this.unlinkOpen = true;
      this.curTeacherId = id;
    },
    handleUnlinkOk() {
      this.unlinkOpen = false;
      unlink(this.curTeacherId, this.currUser.id).then(res => {
        if (res.data.code >= 0) {
          this.fetchStudents(); // 刷新学生列表
          console.log('解除师生关系成功');
        } else {
          console.error('解除师生关系失败');
        }
      }).catch(error => {
        console.error('解除师生关系失败:', error);
      });
    },
    handleUnlinkCancel() {
      this.unlinkOpen = false;
    },
    closeDrawer() {
      this.drawerOpen = false;
      this.rate = 0;
      this.comment = '';
    },
    setComment(id) {
      this.drawerOpen = true;
      this.curTeacherId = id;
    },
    submitComment() {
      if (!this.rate || !this.comment) {
        this.$message.error('评分不能为0且评价不能为空！');
        return;
      }
      console.log('评分:', this.rate);
      console.log('评价内容:', this.comment);
      // 这里可以添加实际的提交逻辑
      submitComment(this.currUser.id, this.currUser.name, this.curTeacherId, this.rate, this.comment).then(res => {
        if (res.data.code >= 0) {
          console.log('发布评价资料成功');
          this.closeDrawer(); // 提交后关闭抽屉
          this.fileName = ''; // 重置输入
          this.downloadLink = ''; // 重置输入
          this.$message.success('发布评价成功');
        }
      }).catch(error => {
        console.error('发布学习资料失败:', error);
      });
    },
    showAcceptMessgae(id) {
      this.curAccepterId = id;
      this.acceptOpen = true;
    },
    handleAcceptOk() {
      this.acceptOpen = false;
      link(this.curAccepterId, this.currUser.id).then(res => {
        if (res.data.code >= 0) {
          this.fetchTodos(); // 刷新待办事项
          console.log('接受学生求职请求成功:', this.curAccepterId);
        } else {
          console.error('接受学生求职请求失败');
        }
      }).catch(error => {
        console.error('接受学生求职请求失败:', error);
      });
    },
    handleAcceptCancel() {
      this.acceptOpen = false;
    },
    showRefuseMessage(id) {
      this.curRefuseId = id;
      this.refuseOpen = true;
    },
    handleRefuseOk() {
      this.refuseOpen = false;
      // 这里可以添加实际的拒绝逻辑
      refuseLink(this.curRefuseId, this.currUser.id).then(res => {
        if (res.data.code >= 0) {
          this.fetchTodos(); // 刷新待办事项
          console.log('拒绝学生求职请求成功:', this.curRefuseId);
        } else {
          console.error('拒绝学生求职请求失败');
        }
      }).catch(error => {
        console.error('拒绝学生求职请求失败:', error);
      });
      console.log('拒绝学生求职请求:', this.curRefuseId);
    },
    handleRefuseCancel() {
      this.refuseOpen = false;
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
