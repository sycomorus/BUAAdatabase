<template>
  <a-card :body-style="{padding: '24px 32px'}" :bordered="false">
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
          placeholder="Tags Mode"
          :options="subjectOptions"
          v-model="selectedSubjects"
        />
      </a-form-item>
      <!-- 新的输入框，当选中'其它'时显示 -->
      <a-form-item
        v-if="selectedSubjects.includes('Others')"
        :label="'其它科目'"
        :labelCol="{span: 7}"
        :wrapperCol="{span: 10}"
      >
        <a-input v-model="otherSubject" placeholder="请输入其它科目" />
      </a-form-item>
      <a-form-item
        :label="'地址'"
        :labelCol="{span: 7}"
        :wrapperCol="{span: 10}"
        >
      <a-cascader v-model="selectedLocation" :options="locationOptions" placeholder="请选择地址" change-on-select />
      </a-form-item>
      <a-form-item
        :label="$t('describe')"
        :labelCol="{span: 7}"
        :wrapperCol="{span: 10}"
      >
        <a-textarea rows="4" :placeholder="$t('describeInput')"/>
      </a-form-item>
      <a-form-item
        :label="$t('metrics')"
        :labelCol="{span: 7}"
        :wrapperCol="{span: 10}"
      >
        <a-textarea rows="4" :placeholder="$t('metricsInput')"/>
      </a-form-item>
      <a-form-item
        :label="$t('customer')"
        :labelCol="{span: 7}"
        :wrapperCol="{span: 10}"
        :required="false"
      >
        <a-input :placeholder="$t('customerInput')"/>
      </a-form-item>
      <a-form-item
        :label="$t('critics')"
        :labelCol="{span: 7}"
        :wrapperCol="{span: 10}"
        :required="false"
      >
        <a-input :placeholder="$t('criticsInput')"/>
      </a-form-item>
      <a-form-item
        :label="$t('weight')"
        :labelCol="{span: 7}"
        :wrapperCol="{span: 10}"
        :required="false"
      >
        <a-input-number :min="0" :max="100"/>
        <span>%</span>
      </a-form-item>
      <a-form-item
        :label="$t('disclosure')"
        :labelCol="{span: 7}"
        :wrapperCol="{span: 10}"
        :required="false"
        :help="$t('disclosureDesc')"
      >
        <a-radio-group v-model="value">
          <a-radio :value="1">{{$t('public')}}</a-radio>
          <a-radio :value="2">{{$t('partially')}}</a-radio>
          <a-radio :value="3">{{$t('private')}}</a-radio>
        </a-radio-group>
        <a-select mode="multiple" v-if="value === 2">
          <a-select-option value="4">{{$t('colleague1')}}</a-select-option>
          <a-select-option value="5">{{$t('colleague2')}}</a-select-option>
          <a-select-option value="6">{{$t('colleague3')}}</a-select-option>
        </a-select>
      </a-form-item>
      <a-form-item style="margin-top: 24px" :wrapperCol="{span: 10, offset: 7}">
        <a-button type="primary">{{'提交'}}</a-button>
        <a-button style="margin-left: 8px">{{'保存'}}</a-button>
      </a-form-item>
    </a-form>
  </a-card>
</template>

<script>
import locationOptions from './locationOptions.json'

export default {
  name: 'BasicForm',
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
