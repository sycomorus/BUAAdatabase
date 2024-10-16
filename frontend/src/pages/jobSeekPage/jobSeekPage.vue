<template>
  <page-layout :title="'广场'">
    <div>
      <!-- 其他代码保持不变 -->
      <a-card :bordered="false">
        <a-list itemLayout="vertical">
          <a-list-item :key="n" v-for="n in 10">
            <a-list-item-meta title="Alipay">
              <div slot="description">
                <a-tag>Ant Design</a-tag>
                <a-tag>设计语言</a-tag>
                <a-tag>蚂蚁金服</a-tag>
              </div>
            </a-list-item-meta>
            <div class="content">
              <div class="detail" :class="{ 'expanded': showFullContent }">
                {{ !shouldShowReadMore || showFullContent ? fullContent : truncatedContent }}
              </div>
              <div class="read-more" v-if="shouldShowReadMore && !showFullContent">
                <a @click="showFullContent = true">查看更多</a>
              </div>
              <div class="read-less" v-if="showFullContent">
                <a @click="showFullContent = false">收起</a>
              </div>
              <div class="author">
                <a>ICZER</a>
                <em>2018-08-05 22:23</em>
                <em>湖南省|衡阳市|雁峰区</em>
              </div>
            </div>
          </a-list-item>
        </a-list>
        <div class="pagination-container">
          <a-pagination :current="current1" :show-size-changer=false :total="50" @showSizeChange="onShowSizeChange" />
        </div>
      </a-card>
    </div>
  </page-layout>
</template>


<script>
import { mapState } from 'vuex'
import PageLayout from '@/layouts/PageLayout'

export default {
  name: 'jobSeekPage',
  components: { PageLayout },
  computed: {
    ...mapState('setting', ['layout', 'pageWidth']),
    truncatedContent() {
      return this.fullContent.slice(0, 80) + '...'; // 截断的文字
    },
    shouldShowReadMore() {
      // 判断是否需要显示“查看更多”按钮
      return this.fullContent.length > this.contentLimit;
    }
  },
  data() {
    return {
      current1: 3,
      showFullContent: false, // 控制是否展示全部内容
      fullContent: '段落示意：蚂蚁金服设计平台 ant.design，用dasdasdnwoqwd打打网球顶起顶起哦带你去哦我的看你发你as达到五千大军迫切的请大家轻拍的情节都跑擦技术大神解答商品定价阿松排第几',
      contentLimit: 80 // 显示“查看更多”按钮的文本长度限制
    }
  },
  methods: {
    onShowSizeChange(current, pageSize) {
      console.log(current, pageSize);
    }
  }
}
</script>


<style lang="less" scoped>
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


.pagination-container {
  text-align: center;
  /* 这将使内联块级元素（如 <a-pagination>）居中 */
}
</style>
