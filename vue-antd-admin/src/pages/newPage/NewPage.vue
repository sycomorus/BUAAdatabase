<template>
  <page-layout :avatar="currUser.avatar">
    <div slot="headerContent">
      <div class="title">{{ welcome.timeFix[lang] }}，{{ currUser.name }}，{{ welcome.message[lang] }}</div>
      <div>{{ currUser.position[lang] }}</div>
    </div>
    <template slot="extra">
      <head-info class="split-right" :title="123" content="56" />
      <head-info class="split-right" :title="$t('ranking')" content="8/24" />
      <head-info class="split-right" :title="$t('visit')" content="2,223" />
    </template>
  </page-layout>
</template>

<script>
import PageLayout from '@/layouts/PageLayout'
import HeadInfo from '@/components/tool/HeadInfo'
import { mapState } from 'vuex'
import { request, METHOD } from '@/utils/request'

export default {
  name: 'GreetingPage',
  components: { PageLayout, HeadInfo },
  data() {
    return {
      welcome: {
        timeFix: '',
        message: ''
      }
    }
  },
  computed: {
    ...mapState('account', { currUser: 'user' }),
    ...mapState('setting', ['lang'])
  },
  created() {
    request('/user/welcome', METHOD.GET).then(res => this.welcome = res.data)
  }
}
</script>

<style lang="less">
@import "index";
</style>