<template>
  <page-layout :desc="'你可以在这个页面填写并发布招聘信息'" :title="'我要招聘'">
    <div class="form-container">
      <a-card :body-style="{ padding: '24px 32px' }" :bordered="false" class="form-card">
        <a-form :form="postForm">
          <a-form-item :label="'标题'" :labelCol="{ span: 6 }" :wrapperCol="{ span: 14 }" :required=false>
            <a-input :placeholder="'请输入标题'" v-decorator="['title', { rules: [{ required: true, message: '请输入标题', whitespace: true}], validateTrigger: 'onSubmit' }]" />
          </a-form-item>

          <a-form-item :label="'日期'" :labelCol="{ span: 6 }" :wrapperCol="{ span: 14 }" :required=false>
            <a-range-picker style="width: 100%" v-decorator="['dateRange', { rules: [{ type: 'array', message: '请选择日期', required: true }], validateTrigger: 'onSubmit' }]" />
          </a-form-item>

          <a-form-item :label="'科目'" :labelCol="{ span: 6 }" :wrapperCol="{ span: 14 }" :required=false>
            <a-select mode="tags" style="width: 100%" placeholder="请输入或选择科目" :options="subjectOptions" v-decorator="['subjects', { rules: [{ type: 'array', required: true, message: '请选择科目' }] }]" />
          </a-form-item>

          <a-form-item :label="'地址'" :labelCol="{ span: 6 }" :wrapperCol="{ span: 14 }" :required=false>
            <a-row :gutter="20">
              <a-col :span="10">
                <a-cascader :options="locationOptions" placeholder="请选择地址" change-on-select v-decorator="['location', { rules: [{ required: true, type: 'array', message: '请选择地址' }] }]" />
              </a-col>
              <a-col :span="14">
                <a-input :placeholder="'请输入详细地址'" v-decorator="['fullLocation', { rules: [{ required: true, message: '请输入详细地址', whitespace: true }] }]" />
              </a-col>
            </a-row>
          </a-form-item>

          <a-form-item :label="'联系方式'" :labelCol="{ span: 6 }" :wrapperCol="{ span: 14 }" :required=false>
            <a-row :gutter="20">
              <a-col :span="10">
                <a-input placeholder="电话号码（必填）" v-decorator="['telephoneNumber', { rules: [{ required: true, message: '请输入电话号码', whitespace: true }] }]" />
              </a-col>
              <a-col :span="14">
                <a-input placeholder="电子邮箱（选填）" v-decorator="['emailAddress']" />
              </a-col>
            </a-row>
          </a-form-item>

          <a-form-item :label="'详情'" :labelCol="{ span: 6 }" :wrapperCol="{ span: 14 }" :required=false>
            <a-textarea rows="4" :placeholder="'可以在这里描述你的具体要求，薪资水平，学生的学习情况等'" v-decorator="['content', { rules: [{ required: true, message: '请输入详情', whitespace: true }] }]" />
          </a-form-item>

          <a-form-item style="margin-top: 24px" :wrapperCol="{ span: 14, offset: 6 }" :required=false>
            <a-button type="primary" @click="handleSubmit" class="submit-button">{{ '提交' }}</a-button>
            <a-button style="margin-left: 8px" @click="handleSave">{{ '保存' }}</a-button>
          </a-form-item>
        </a-form>
      </a-card>
    </div>
  </page-layout>
</template>

<script>
import { sendPost, savePost, getSavedPost } from '@/services/user'
import PageLayout from '@/layouts/PageLayout'
import locationOptions from '@/assets/json/locationOptions.json'
import { mapState } from 'vuex'
import moment from 'moment';

export default {
  name: 'teacherPostPage',
  computed: {
    ...mapState('account', { currUser: 'user' }),
  },
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
    this.locationOptions = locationOptions;
    this.fetchSavedPost();
  },
  methods: {
    async fetchSavedPost() {
      try {
        const response = await getSavedPost(this.currUser.id);
        const resdata = response.data;

        if (resdata.code !== -1) {
          const { title, startDate, endDate, subjects, location, fullLocation, telephoneNumber, emailAddress, content } = resdata.data;
          this.postForm.setFieldsValue({
            title,
            dateRange: [startDate ? moment(startDate) : null, endDate ? moment(endDate) : null],
            subjects,
            location,
            fullLocation,
            telephoneNumber,
            emailAddress,
            content,
          });
        }
      } catch (error) {
        console.error('获取草稿失败', error);
      }
    },
    handleSubmit() {
      this.postForm.validateFields((errors, values) => {
        if (!errors) {
          const title = values.title;
          const dateRange = values.dateRange;
          const startDate = dateRange[0].format('YYYY-MM-DD');
          const endDate = dateRange[1].format('YYYY-MM-DD');
          const subjects = values.subjects;
          const location = values.location;
          const fullLocation = values.fullLocation;
          const telephoneNumber = values.telephoneNumber;
          const emailAddress = values.emailAddress;
          const content = values.content;
          sendPost(this.currUser.id, title, startDate, endDate, subjects, location, fullLocation, telephoneNumber, emailAddress, content).then(this.afterPost)
        } else {
          console.log('表单验证错误:', errors);
        }
      });
    },
    afterPost(res) {
      const resdata = res.data;
      if (resdata.code >= 0) {
        this.$message.success('发布成功');
        this.postForm.resetFields();
      } else {
        this.$message.error('发布失败，可能出现了网络波动');
      }
    },
    handleSave() {
      const values = this.postForm.getFieldsValue();
      const title = values.title || '';
      const dateRange = values.dateRange || [];
      const startDate = dateRange.length ? dateRange[0].format('YYYY-MM-DD') : '';
      const endDate = dateRange.length ? dateRange[1].format('YYYY-MM-DD') : '';
      const subjects = values.subjects || [];
      const location = values.location || [];
      const fullLocation = values.fullLocation || '';
      const telephoneNumber = values.telephoneNumber || '';
      const emailAddress = values.emailAddress || '';
      const content = values.content || '';

      savePost(this.currUser.id, title, startDate, endDate, subjects, location, fullLocation, telephoneNumber, emailAddress, content).then(this.afterSave);
    },

    afterSave(res) {
      const resdata = res.data;
      if (resdata.code >= 0) {
        this.$message.success('保存成功');
      } else {
        this.$message.error('保存失败，可能出现了网络波动');
      }
    }
  }
}
</script>

<style lang="less" scoped>
.page-layout {
  padding: 20px;
}

.form-container {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

.form-card {
  width: 100%;
  max-width: 1200px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.submit-button {
  background-color: #4CAF50; /* 绿色 */
  color: white;
  border: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #45a049; /* 深绿色 */
}
</style>
