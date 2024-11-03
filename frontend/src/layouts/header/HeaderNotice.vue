<template>
  <a-dropdown :trigger="['click']" v-model="show">
    <div slot="overlay">
      <a-spin :spinning="loading">
        <a-tabs class="dropdown-tabs" :tabBarStyle="{textAlign: 'center'}" :style="{width: '297px'}">
          <a-tab-pane tab="通知" key="1">
            <a-list class="tab-pane">
              <a-list-item v-for="(notice, index) in notices" :key="index">
                <a-list-item-meta :title="notice.title" :description="notice.description"/>
              </a-list-item>
            </a-list>
          </a-tab-pane>
        </a-tabs>
      </a-spin>
    </div>
    <span  class="header-notice">
      <a-badge class="notice-badge" @click="clearNum" :count="newNum">
        <a-icon :class="['header-notice-icon']" type="bell" />
      </a-badge>
    </span>
  </a-dropdown>
</template>

<script>
import { getNotices } from '@/services/user'; // 确保引入你的API服务

export default {
  name: 'HeaderNotice',
  computed: {
    ...mapState("account", { currUser: "user" }),
  },
  data () {
    return {
      loading: false,
      show: false,
      notices: [],
      newNum: 0
    }
  },
  mounted () {
    this.fetchNotice();
  },
  methods: {
    fetchNotice () {
      if (this.loading) {
        this.loading = false;
        return;
      }
      if (this.show) return;

      this.loading = true;
      getNotices(this.currUser.id) // 调用 API 获取通知
        .then(response => {
          if (response.data.code >= 0) {
            this.notices = response.data.notices;
            this.newNum = response.data.newNum;
            this.loading = false;
          } else {
            console.error('获取通知失败:', response.data.message);
            this.loading = false;
          }
        })
        .catch(error => {
          console.error('获取通知失败:', error);
          this.loading = false;
        });
    },
    handleNoticeClick() {
      this.notices.newNum = 0; // 点击后将新通知数量设为0
      this.fetchNotice(); // 可选：重新获取通知
    },
    clearNum() {
      this.newNum = 0;
    }
  }
}
</script>

<style lang="less">
.header-notice {
  display: inline-block;
  transition: all 0.3s;
  span {
    vertical-align: initial;
  }
  .notice-badge {
    color: inherit;
    .header-notice-icon {
      font-size: 16px;
      padding: 4px;
    }
  }
}
.dropdown-tabs {
  background-color: @base-bg-color;
  box-shadow: 0 2px 8px @shadow-color;
  border-radius: 4px;
  .tab-pane {
    padding: 0 24px 12px;
    min-height: 250px;
  }
}
</style>
