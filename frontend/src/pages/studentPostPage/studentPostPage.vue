<template>
  <page-layout :title="'你可以在这个页面填写并发布招聘信息'">
    <div style="display: flex; justify-content: center;">
      <a-card :body-style="{ padding: '24px 32px' }" :bordered="false" :style="{ width: '1200px' }">
        <a-form :form="postForm">
          <a-form-item :label="'标题'" :labelCol="{ span: 7 }" :wrapperCol="{ span: 10 }" :required="false">
            <a-input :placeholder="'请输入标题'"
              v-decorator="['title', { rules: [{ required: true, message: ' ', whitespace: true}], validateTrigger: 'onSubmit' }]" />
          </a-form-item>
          <a-form-item :label="'日期'" :labelCol="{ span: 7 }" :wrapperCol="{ span: 10 }" :required="false">
            <a-range-picker style="width: 100%"
              v-decorator="['dateRange', { rules: [{ type: 'array', message: ' ', required: true, whitespace: true}], validateTrigger: 'onSubmit' }]" />
          </a-form-item>
          <a-form-item :label="'科目'" :labelCol="{ span: 7 }" :wrapperCol="{ span: 10 }" :required="false">
            <a-select mode="tags" style="width: 100%" placeholder="请输入或选择科目" :options="subjectOptions"
              v-decorator="['subjects', { rules: [{ type: 'array',required: true, message: ' ', message: ' ', whitespace: true}], validateTrigger: 'onSubmit' }]"/>
          </a-form-item>
          <a-form-item :label="'地址'" :labelCol="{ span: 7 }" :wrapperCol="{ span: 10 }" :required="false">
            <a-row :gutter="20"> <!-- 设置列间间隔为16像素 -->
              <a-col :span="10">
                <a-cascader :options="locationOptions" placeholder="请选择地址" change-on-select
                v-decorator="['location', { rules: [{ required: true, type: 'array', message: ' ', validateTrigger: 'onSubmit' }] }]"/>
              </a-col>
              <a-col :span="14">
                <a-input :placeholder="'请输入详细地址'" v-decorator="['fullLocation', { rules: [{ required: true, message: ' ', whitespace: true}], validateTrigger: 'onSubmit'}]"/>
              </a-col>
            </a-row>
          </a-form-item>
          <a-form-item :label="'联系方式'" :labelCol="{ span: 7 }" :wrapperCol="{ span: 10 }" :required="false">
            <a-row :gutter="20">
              <a-col :span="10">
                <a-input placeholder="电话号码（必填）" v-decorator="['teltphoneNumber', { rules: [{ required: true, message: ' ', whitespace: true}], validateTrigger: 'onSubmit'}]"/>
              </a-col>
              <a-col :span="14">
                <a-input placeholder="电子邮箱（选填)" v-decorator="['emailAddress', { rules: [{ required: false, message: ' ', whitespace: true}], validateTrigger: 'onSubmit'}]"/>
              </a-col>
            </a-row>
          </a-form-item>
          <a-form-item :label="'详情'" :labelCol="{ span: 7 }" :wrapperCol="{ span: 10 }" :required = 'false'>
            <a-textarea rows="4" :placeholder="'可以在这里描述你的具体要求，薪资水平，学生的学习情况等'" v-decorator="['content', { rules: [{ required: true, message: ' ', whitespace: true}], validateTrigger: 'onSubmit'}]" />
          </a-form-item>
          <a-form-item style="margin-top: 24px" :wrapperCol="{ span: 10, offset: 7 }">
            <a-button type="primary" @click="handleSubmit">{{ '提交' }}</a-button>
            <a-button style="margin-left: 8px">{{ '保存' }}</a-button>
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
  data() {
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
        { value: '信息技术', label: '信息技术' }
      ],
      postForm: this.$form.createForm(this),
      locationOptions: [],
    }
  },
  created() {
    this.locationOptions = locationOptions; // 在组件创建时加载 JSON 数据
  },
  methods: {
    handleSubmit() {
      // 验证表单字段
      this.postForm.validateFields((errors, values) => {
        if (!errors) {
          // 表单验证通过，提交数据
          console.log('表单数据:', values);
        } else {
          console.log('表单验证错误:', errors);
        }
      });
    }
  }
}
</script>
