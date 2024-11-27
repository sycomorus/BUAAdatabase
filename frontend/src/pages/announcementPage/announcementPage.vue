<template>
  <page-layout :avatar="currUser.avatar">
    <div slot="headerContent">
      <div class="title">{{ '您好' }}，{{ currUser.name }}，{{ '欢迎来到家教综合服务平台' }}</div>
    </div>
    <a-card :bordered="false" class = "announcement_card">
      <a-collapse :bordered="false" class="custom-collapse">
        <!-- 动态渲染公告 -->
        <a-collapse-panel v-for="(announcement, index) in announcements" :key="index">
          <template #header>
            <span class="announcement-title">
              {{ announcement.title || `公告 ${index + 1}` }}
            </span>
            <span class="announcement-date">{{ announcement.date }}</span>
          </template>
          <div class="announcement-content">
            <p>{{ announcement.content }}</p>
          </div>
        </a-collapse-panel>
      </a-collapse>
    </a-card>
  </page-layout>
</template>

<script>
import PageLayout from '@/layouts/PageLayout'
import { mapState } from 'vuex'
import { getAnnouncements } from '@/services/user'

export default {
  name: 'announcementPage',
  components: { PageLayout },
  data() {
    return {
      announcements: [],
    }
  },
  computed: {
    ...mapState('account', { currUser: 'user' }),
    ...mapState('setting', ['lang'])
  },
  created() {
    getAnnouncements().then(response => {
      if (response.data.code >= 0) {
        const data = response.data.data;
        this.announcements = data.announcements;
        console.log('获取公告成功:', this.announcements);
      } else {
        console.error('获取公告失败:', response.data.msg);
      }
    }).catch(error => {
      console.error('获取公告失败:', error);
      this.loading = false;
    });

  }
}
</script>

<style lang="less">
@import "index";

.page-layout {
  padding: 20px;
}

.custom-collapse {
  background-color: transparent !important;
  border: none !important;
}

.custom-collapse .ant-collapse-item {
  border: none !important;
  /* 去掉每个面板的边框 */
}

.custom-collapse .ant-collapse-header {
  background-color: transparent !important;
  border: none !important;
}

.custom-collapse .ant-collapse-content {
  background-color: transparent !important;
  border: none !important;
}

.announcement-title {
  position: relative;
  font-weight: bold;
  /* 粗体 */
  font-size: 16px;
  /* 调整字体大小 */
  display: block;
  /* 独占一行 */
}

.announcement-content {
  font-size: 14px;
  /* 调整字体大小 */
  max-height: 100px;
  /* 最大高度 */
  line-height: 1.5;
  /* 行高 */
  margin-top: 10px;
  /* 顶部外边距 */
  color: #444;
  /* 字体颜色 */
  // 左间距
  padding-left: 24px;
  // 左对齐
  text-align: left;
}

.announcement-date {
  position: absolute;
  // 显示在右下角
  bottom: 0;
  right: 0;
  font-size: 12px;
  /* 调整字体大小 */
  color: #999;
}

.announcement_card {
  width: 100%;
  max-width: 1200px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
</style>
