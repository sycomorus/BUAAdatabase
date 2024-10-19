<template>
  <page-layout :title="'广场'">
    <div>
      <div :class="['search-head', layout, pageWidth]">
        <div class="search-input">
          <a-input-search class="search-ipt" style="width: 600px" placeholder="请输入搜索内容" size="large" enterButton="搜索"
            v-model="searchQuery" @search="searchPosts">
            <a-icon slot="prefix" type="search" />
          </a-input-search>
        </div>
      </div>
      <div class="search-content">
        <router-view />
      </div>
      <a-card :bordered="false">
        <a-list itemLayout="vertical">
          <a-list-item v-for="(post, index) in posts" :key="index" class="list-item">
            <router-link :to="{ name: '帖子详情', params: { id: post.id, showAccept: true } }" class="title-link">
              <a-list-item-meta :title="post.title">
                <div slot="description">
                  <a-tag v-for="tag in post.tags" :key="tag">{{ tag }}</a-tag>
                </div>
              </a-list-item-meta>
            </router-link>
            <div class="content">
              <div class="detail" :class="{ 'expanded': showFullContent === post.id }">
                {{ showFullContent === post.id || !shouldShowReadMore(post.content) ? post.content :
                  post.content.slice(0, 60) + '...' }}
              </div>
              <div class="read-more" v-if="shouldShowReadMore(post.content) && showFullContent !== post.id">
                <a @click="showFullContent = post.id">查看更多</a>
              </div>
              <div class="read-less" v-if="showFullContent === post.id">
                <a @click="showFullContent = null">收起</a>
              </div>
              <div class="author">
                <router-link :to="{ name: '学生主页', params: { id: post.authorId } }">
                  {{ post.author }}
                </router-link>
                <em>{{ post.date }}</em>
                <em>{{ post.location }}</em>
              </div>
            </div>
          </a-list-item>
        </a-list>
        <div class="pagination-container">
          <a-pagination :current="currentPage" :show-size-changer="false" :total="totalPosts" @change="onPageChange" />
        </div>
      </a-card>
    </div>
  </page-layout>
</template>

<script>
import { mapState } from 'vuex'
import PageLayout from '@/layouts/PageLayout'
import { getPosts } from '@/services/user'

export default {
  name: 'jobSeekPage',
  components: { PageLayout },
  computed: {
    ...mapState('setting', ['layout', 'pageWidth']),
    ...mapState('account', { currUser: 'user' })
  },
  created() {
    this.fetchPosts();
    console.log(this.currUser.id)
  },
  data() {
    return {
      currentPage: 1, // 当前页码
      totalPosts: 0, // 总帖子数量
      posts: [], // 帖子列表
      showFullContent: null, // 控制显示完整内容的帖子ID
      searchQuery: '', // 搜索内容
    }
  },
  methods: {
    fetchPosts() {
      getPosts(this.currUser.id, this.currentPage, this.searchQuery)
        .then(response => {
          this.posts = response.data.posts;
          this.totalPosts = response.data.total;
        })
        .catch(error => {
          console.error('获取帖子信息失败:', error);
        });
    },
    searchPosts() {
      this.currentPage = 1;
      this.fetchPosts();
    },
    shouldShowReadMore(content) {
      return content.length > 60;
    },
    onPageChange(page) {
      this.currentPage = page;
      this.fetchPosts();
    }
  }
}
</script>

<style lang="less" scoped>
.page-layout {
  padding: 20px;
}

.search-head {
  background-color: @base-bg-color;
  margin: -24px;
  padding-bottom: 20px;

  &.head.fixed {
    margin: -24px 0;
  }

  .search-input {
    text-align: center;
  }
}

.search-content {
  margin-top: 48px;
}

.extra {
  width: 272px;
  height: 1px;
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

  .author {
    color: @text-color-second;
    margin-top: 16px;
    line-height: 22px;

    &> :global(.ant-avatar) {
      vertical-align: top;
      margin-right: 8px;
      width: 20px;
      height: 20px;
      position: relative;
      top: 1px;
    }

    &>em {
      color: @disabled-color;
      font-style: normal;
      margin-left: 16px;
    }
  }
}

.list-item {
  transition: background-color 0.3s ease;
}

.title-link {
  display: block;
  /* 确保整个标题区域可点击 */
  transition: color 0.3s ease, text-decoration 0.3s ease;

  &:hover {
    color: #1890ff;
    /* 更改颜色 */
  }
}

.list-item:hover {
  background-color: rgba(240, 240, 240, 0.5);
  /* 背景色变化 */
}

.pagination-container {
  text-align: center;
}
</style>
