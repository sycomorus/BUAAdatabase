<template>
  <page-layout :title="'广场'">
    <div>
      <div :class="['search-head', layout, pageWidth]">
          <div class="search-input">
            <a-input-search class="search-ipt" style="width: 600px" placeholder="请输入..." size="large" enterButton="搜索">
              <a-icon slot="prefix" type="search" />
            </a-input-search>
          </div>
      </div>
      <div class="search-content">
        <router-view />
      </div>
      <search-form />
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
              <div class="detail">
                段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台
                ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。
              </div>
              <div class="author">
                <a-avatar size="small" src="https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png" />
                <a>ICZER</a>发布在
                <a href="https://github.com/iczer">https://github.com/iczer</a>
                <em>2018-08-05 22:23</em>
              </div>
            </div>
            <span slot="actions"><a-icon style="margin-right: 8px" type="star-o" />156</span>
            <span slot="actions"><a-icon style="margin-right: 8px" type="like-o" />1435</span>
            <span slot="actions"><a-icon style="margin-right: 8px" type="message" />4</span>
          </a-list-item>
        </a-list>
      </a-card>
    </div>
  </page-layout>
</template>

<script>
import { mapState } from 'vuex'
import SearchForm from './SearchForm'
import PageLayout from '@/layouts/PageLayout'
export default {
  name: 'jobSeekPage',
  components: { SearchForm, PageLayout},
  computed: {
    ...mapState('setting', ['layout', 'pageWidth']),
  },
  methods: {
    navigate() {
      this.$router.push('/jobSeekList')
    }
  }
}
</script>

<style lang="less" scoped>
.search-head {
  background-color: @base-bg-color;
  margin: -24px;
  padding-bottom: 20px; /* 增加底部内边距 */ 
  
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
    max-width: 720px;
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
</style>
