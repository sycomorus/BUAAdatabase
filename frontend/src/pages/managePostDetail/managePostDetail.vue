<template>
    <page-layout :title="post.title" :desc="post.startDate + ' 至 ' + post.endDate">
        <a-card class="post-detail-card">
            <div class="post-content">
                <h2>{{ post.title }}</h2>
                <div class="post-meta">
                    <span class="author">
                        {{ post.author }}
                    </span>
                    <span class="date">{{ post.startDate }} - {{ post.endDate }}</span>
                </div>

                <div class="post-location">
                    <strong>地址：</strong>
                    <span>{{ post.location.join(', ') }}</span>
                    <span v-if="post.fullLocation">（{{ post.fullLocation }}）</span>
                </div>

                <div class="contact-info">
                    <strong>联系方式：</strong>
                    <div>
                        <span>电话：{{ post.telephoneNumber }}</span>
                        <span v-if="post.emailAddress">邮箱：{{ post.emailAddress }}</span>
                    </div>
                </div>

                <div class="subjects">
                    <strong>科目：</strong>
                    <span v-for="subject in post.subjects" :key="subject" class="subject">{{ subject }}</span>
                </div>
                <a-divider />
                <div class="post-body">
                    <p>{{ post.content }}</p>
                </div>
            </div>
            <a-divider />
            <a-space wrap class="button-container">
                <a-button v-if="$route.params.showDelete !== false" type="primary" @click="showModal">删除</a-button>
                <a-button type="dashed" @click="goBack">返回</a-button>
            </a-space>
        </a-card>
        <a-modal :visible="open" title="你确定要删除这篇帖子吗?" @ok="handleOk" @cancel="handleCancel">
            <p><strong>该操作无法撤销</strong></p>
        </a-modal>
    </page-layout>
</template>

<script>
import PageLayout from '@/layouts/PageLayout'
import { getPost, deletePost} from '@/services/user'

export default {
    name: 'managePostDetail',
    components: { PageLayout },
    data() {
        return {
            post: {},
            open: false
        }
    },
    created() {
        console.log(this.$route.params.id);
        this.fetchPostDetail();
    },
    methods: {
        showModal() {
            this.open = true;
        },
        handleOk() {
            this.open = false;
            deletePost(this.post.id).then(response => {
                if (response.data.code >= 0) {
                    this.$message.success('删除帖子成功');
                } else {
                    this.$message.error('删除帖子失败');
                }
            }).catch(error => {
                console.error('删除帖子失败:', error);
            });
            this.goBack();
        },
        handleCancel() {
            this.open = false;
        },
        goBack() {
            this.$router.go(-1); // 返回到上一个页面
        },
        fetchPostDetail() {
            const postId = this.$route.params.id; // 从路由参数获取帖子 ID
            getPost(postId)
                .then(response => {
                    if (response.data.code >= 0) {
                        this.post = response.data.data;
                    } else {
                        console.error('获取帖子详情失败:', response.data.msg);
                    }
                })
                .catch(error => {
                    console.error('获取帖子详情失败:', error);
                });
        }
    }
}
</script>

<style lang="less" scoped>
.button-container {
    display: flex; // 使用 flexbox
    justify-content: center; // 水平居中
    margin-top: 20px; // 可以调整上边距
    gap: 16px; // 设置按钮之间的间距
}

.post-detail-card {
    padding: 20px;
    border-radius: 8px;
    background-color: #f9f9f9;
}

.post-content {
    h2 {
        font-size: 24px;
        margin-bottom: 16px;
    }

    .post-meta {
        color: #888;
        font-size: 14px;
        margin-bottom: 16px;

        .author {
            margin-right: 10px;
        }
    }

    .post-location {
        font-size: 16px;
        margin-bottom: 16px;
    }

    .contact-info {
        font-size: 16px;
        margin-bottom: 16px;

        span {
            display: block;
        }
    }

    .subjects {
        margin-bottom: 16px;

        .subject {
            display: inline-block;
            background-color: #e6f7ff;
            border-radius: 4px;
            padding: 4px 8px;
            margin-right: 5px;
        }
    }

    .post-body {
        font-size: 16px;
        line-height: 1.5;
    }
}
</style>