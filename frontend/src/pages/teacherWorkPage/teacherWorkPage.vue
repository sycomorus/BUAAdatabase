<template>
    <page-layout>
        <a-card :bordered="false">
            <div>
                <a-tabs size="large" :tabBarStyle="{ textAlign: 'center' }" @change="onTabChange"
                    style="padding: 0 10px;">
                    <a-tab-pane key="1" tab="我的帖子">
                        <a-list item-layout="horizontal">
                            <a-list-item v-for="post in posts" :key="post.title">
                                <a-list-item-meta :title="item.title">
                                    <div slot="description">
                                        {{ post.content }}
                                    </div>
                                </a-list-item-meta>
                                <div slot="actions">
                                    <a-button type="link">详情</a-button>
                                    <a-button type="link">删除</a-button>
                                </div>
                            </a-list-item>
                        </a-list>
                    </a-tab-pane>
                    <a-tab-pane key="2" tab="我的学生">我的学生</a-tab-pane>
                    <a-tab-pane key="3" tab="我的通知">我的通知</a-tab-pane>
                </a-tabs>
            </div>
        </a-card>
    </page-layout>
</template>

<script>
import PageLayout from '@/layouts/PageLayout'
import { getUserPosts } from '@/services/user'
export default {
    name: 'teacherWorkPage',
    components: { PageLayout },
    created() {
        this.fetchUserPosts();
    },
    data() {
        return {
            activeKey: '1',
            posts: []
        }
    },
    methods: {
        onTabChange(key) {
            this.activeKey = key;
        },
        fetchUserPosts() {
            getUserPosts().then(res => {
                if (res.data.code >= 0) {
                    this.posts = res.data.data;
                }
                else {
                    console.error('获取帖子信息失败');
                }
            }).catch(error => {
                console.error('获取帖子信息失败:', error);
            });
        }

    },
}
</script>

<style lang="less" scoped>
.page-layout {
    padding: 20px;
}

.demo-loadmore-list {
    min-height: 350px;
}
</style>
