<template>
  <page-layout :title="'你可以在这个页面填写并发布招聘信息'" >
    <div style="display: flex; justify-content: center;">
    <a-card :body-style="{padding: '24px 32px'}" :bordered="false" :style="{width: '1200px'}">
      <a-form>
        <a-form-item
          :label="'标题'"
          :labelCol="{span: 7}"
          :wrapperCol="{span: 10}"
        >
          <a-input :placeholder="'请输入标题'" />
        </a-form-item>
        <a-form-item
          :label="'日期'"
          :labelCol="{span: 7}"
          :wrapperCol="{span: 10}"
        >
          <a-range-picker style="width: 100%" picker= 'month'/>
        </a-form-item>
        <a-form-item
          :label="'科目'"
          :labelCol="{span: 7}"
          :wrapperCol="{span: 10}"
        >
          <a-select
            mode="tags"
            style="width: 100%"
            placeholder="请选择科目"
            :options="subjectOptions"
            v-model="selectedSubjects"
          />
        </a-form-item>
        <!-- 新的输入框，当选中'其它'时显示 -->
        <a-form-item
          v-if="selectedSubjects.includes('其它')"
          :label="'其它科目'"
          :labelCol="{span: 7}"
          :wrapperCol="{span: 10}"
        >
          <a-input v-model="otherSubject" placeholder="请输入其它科目" />
        </a-form-item>
        <a-form-item :label="'地址'" :labelCol="{span: 7}" :wrapperCol="{span: 10}">
          <a-row :gutter="20"> <!-- 设置列间间隔为16像素 -->
            <a-col :span="10">
              <a-cascader v-model="selectedLocation" :options="locationOptions" placeholder="请选择地址" change-on-select />
            </a-col>
            <a-col :span="14">
              <a-input :placeholder="'请输入详细地址'" />
            </a-col>
          </a-row>
        </a-form-item>
        <a-form-item :label="'联系方式'" :labelCol="{span: 7}" :wrapperCol="{span: 10}">
          <a-row :gutter="20">
            <a-col :span="10">
              <a-input placeholder="电话号码（必填）" />
            </a-col>
            <a-col :span="14">
              <a-input :placeholder="'电子邮件（选填）'" />
            </a-col>
          </a-row>
        </a-form-item>
        <a-form-item
          :label="'详情'"
          :labelCol="{span: 7}"
          :wrapperCol="{span: 10}"
        >
          <a-textarea rows="4" :placeholder="'可以在这里描述你的具体要求，薪资水平，学生的学习情况等'"/>
        </a-form-item>
        <a-form-item style="margin-top: 24px" :wrapperCol="{span: 10, offset: 7}">
          <a-button type="primary">{{'提交'}}</a-button>
          <a-button style="margin-left: 8px">{{'保存'}}</a-button>
        </a-form-item>
      </a-form>
    </a-card>
    </div>
  </page-layout>
</template>

<script>
import PageLayout from '@/layouts/PageLayout'
import locationOptions from '@/assets/json/locationOptions.json'

export default {
  name: 'studentPostPage',
  components: { PageLayout },
  data () {
    return {
      subjectOptions: [
        { value: '语文', label: '语文' },
        { value: '数学', label: '数学' },
        { value: '英语', label: '英语' },
        { value: '物理', label: '物理' },
        { value: '化学', label: '化学' },
        { value: '生物', label: '生物' },
        { value: '历史', label: '历史' },
        { value: '地理', label: '地理' },
        { value: '政治', label: '政治' },
        { value: '音乐', label: '音乐' },
        { value: '美术', label: '美术' },
        { value: '体育', label: '体育' },
        { value: '信息技术', label: '信息技术' },
        { value: '其它', label: '其他' }
      ],
      locationOptions: [],
      selectedLocation : [], // 用于存储选择的地点
      selectedSubjects: [], // 用于存储选择的科目
      otherSubject: '' // 存储"其它"科目时的输入
    }
  },
  created() {
    this.locationOptions = locationOptions; // 在组件创建时加载 JSON 数据
  },
  computed: {
    desc() {
      return this.$t('pageDesc')
    }
  }
}
</script>

<style scoped>
</style>
