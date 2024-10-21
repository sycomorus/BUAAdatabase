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
          <a-list-item v-for="(post, index) in posts" :key="index" :title="post.title" class="list-item">
            <div class="title-link" @click="navigateToPost(post.id)">
              <a-list-item-meta :title="post.title">
                <div slot="description">
                  <a-tag v-for="tag in post.tags" :key="tag">{{ tag }}</a-tag>
                </div>
              </a-list-item-meta>
            </div>
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
                <router-link :to="{ name: '家教主页', params: { id: post.authorId } }">
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
  name: 'hirePage',
  components: { PageLayout },
  computed: {
    ...mapState('setting', ['layout', 'pageWidth']),
    ...mapState('account', { currUser: 'user' })
  },
  created() {
    this.fetchPosts();
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
      // 调用 getPosts 方法，获取当前用户的帖子列表，添加 searchQuery
      getPosts(this.currUser.id, this.currentPage, this.searchQuery)
        .then(response => {
          this.posts = response.data.posts; // 将返回的帖子列表存储到 posts 中
          this.totalPosts = response.data.total; // 获取总帖子数用于分页
        })
        .catch(error => {
          console.error('获取帖子信息失败:', error);
        });
    },
    searchPosts() {
      // 当用户点击搜索按钮时，重新获取数据
      this.currentPage = 1;
      this.fetchPosts();
    },
    shouldShowReadMore(content) {
      // 判断是否需要显示“查看更多”按钮
      return content.length > 60;
    },
    onPageChange(page) {
      // 当用户点击分页时，更新当前页面并重新获取数据
      this.currentPage = page;
      this.fetchPosts();
    },
    navigateToPost(postId) {
      this.$router.push({ name: '帖子详情', params: { id: postId, showAccept: true } });
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
  /* 增加底部内边距 */

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
    text-overflow: ellipsis; // 单行或有限行文本显示省略号
    white-space: normal; // 多行显示
    transition: max-height 0.3s ease, white-space 0.3s ease;

    &.expanded {
      max-height: none;
      overflow: visible; // 展开时取消 overflow 限制
      text-overflow: clip; // 展开时不再显示省略号
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
  }
}

.list-item:hover {
  background-color: rgba(240, 240, 240, 0.5);
  /* 背景色变化 */
}

.pagination-container {
  text-align: center;
  /* 这将使内联块级元素（如 <a-pagination>）居中 */
}
</style>
