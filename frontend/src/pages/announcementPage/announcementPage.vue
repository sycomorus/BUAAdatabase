<template>
  <page-layout :avatar="currUser.avatar">
    <div slot="headerContent">
      <div class="title">{{'您好'}}，{{currUser.name}}，{{'欢迎来到家教综合服务平台'}}</div>
      <div class="title">{{notice}}</div>
    </div>
    <template>
          <a-card :loading="loading" :title="$t('dynamic')" :bordered="false">
          </a-card>
    </template>
  </page-layout>
</template>

<script>
import PageLayout from '@/layouts/PageLayout'
import {mapState} from 'vuex'

export default {
  name: 'announcementPage',
  components: {PageLayout},
  data () {
    return {
      loading: true,
      activities: [],
      notice: "本网站暂时处于建设之中，敬请期待"
    }
  },
  computed: {
    ...mapState('account', {currUser: 'user'}),
    ...mapState('setting', ['lang'])
  },
  created() {

  }
}
</script>

<style lang="less">
@import "index";
.page-layout {
    padding: 20px;
}
</style>
