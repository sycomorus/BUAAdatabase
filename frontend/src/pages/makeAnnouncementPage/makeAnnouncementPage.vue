<template>
    <page-layout :desc="'你可以在这个页面发布公告'" :title="'发布公告'">
        <div class="form-container">
            <a-card :body-style="{ padding: '24px 32px' }" :bordered="false" class="form-card">
                <a-form :form="postForm">
                    <a-form-item :label="'公告标题'" :labelCol="{ span: 7 }" :wrapperCol="{ span: 10 }" :required=false>
                        <a-input :placeholder="'请输入公告标题'"
                            v-decorator="['title', { rules: [{ required: true, message: '请输入公告标题', whitespace: true }], validateTrigger: 'onSubmit' }]" />
                    </a-form-item>

                    <a-form-item :label="'公告内容'" :labelCol="{ span: 7 }" :wrapperCol="{ span: 10 }" :required=false>
                        <a-textarea rows="12" :placeholder="'请输入公告内容'"
                            v-decorator="['content', { rules: [{ required: true, message: '请输入公告内容', whitespace: true }] }]" />
                    </a-form-item>

                    <a-form-item style="margin-top: 24px" :wrapperCol="{ span: 10, offset: 11 }" :required=false>
                        <a-button type="primary" @click="handleSubmit" class="submit-button">{{ '提交' }}</a-button>
                    </a-form-item>
                </a-form>
            </a-card>
        </div>
    </page-layout>
</template>

<script>
import { makeAnnouncement } from '@/services/user'
import PageLayout from '@/layouts/PageLayout'
import { mapState } from 'vuex'

export default {
    name: 'makeAnnouncementPage',
    computed: {
        ...mapState('account', { currUser: 'user' }),
    },
    components: { PageLayout },

    data() {
        return {
            postForm: this.$form.createForm(this)
        }
    },
    methods: {
        handleSubmit() {
            this.postForm.validateFields((errors, values) => {
                if (!errors) {
                    const title = values.title;
                    const content = values.content;
                    makeAnnouncement(this.currUser.id, title, content).then(this.afterPost)
                } else {
                    console.log('表单验证错误:', errors);
                }
            });
        },
        afterPost(res) {
            const resdata = res.data;
            console.log(resdata);
            if (resdata.code >= 0) {
                this.$message.success('发布成功');
                this.postForm.resetFields();
            } else {
                this.$message.error('发布失败，可能出现了网络波动');
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
    background-color: #4CAF50;
    /* 绿色 */
    color: white;
    border: none;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.submit-button:hover {
    background-color: #45a049;
    /* 深绿色 */
}
</style>