<template>
    <page-layout>
        <a-card :bordered="false">
            <div>
                <a-tabs size="large" :tabBarStyle="{ textAlign: 'center' }" @change="onTabChange"
                    style="padding: 0 10px;">
                    <a-tab-pane :key=1 tab="我的帖子">
                        <a-list item-layout="horizontal">
                            <a-list-item v-for="post in posts" :key="post.id">
                                <a-list-item-meta :title="post.title">
                                    <div slot="description">
                                        <div class="content">
                                            <div class="detail" :class="{ 'expanded': showFullContent === post.id }">
                                                {{ showFullContent === post.id || !shouldShowReadMore(post.content) ? post.content :
                                                post.content.slice(0, 60) + '...' }}
                                            </div>
                                            <div class="read-more" v-if="shouldShowReadMore(post.content) && showFullContent !== post.id">
                                                <a @click="showFullContent = post.id">显示更多</a>
                                            </div>
                                            <div class="read-less" v-if="showFullContent === post.id">
                                                <a @click="showFullContent = null">收起</a>
                                            </div>
                                        </div>
                                    </div>
                                </a-list-item-meta>
                                <div slot="actions">
                                    <router-link :to="{ name: '帖子详情', params: { id: post.id, showAccept: false } }">
                                        <a-button type="link">详情</a-button>
                                    </router-link>
                                    <a-button type="link" @click="showDeleteMessage(post.id)">删除</a-button>
                                </div>
                            </a-list-item>
                        </a-list>
                    </a-tab-pane>
                    <a-tab-pane key="2" tab="我的学生">我的学生</a-tab-pane>
                    <a-tab-pane key="3" tab="我的通知">我的通知</a-tab-pane>
                </a-tabs>
            </div>
        </a-card>
        <a-modal :visible="deleteOpen" title="您确定要删除这个帖子吗?" @ok="handleDeleteOk" @cancel="handleDeleteCancel">
            <p>123</p>
        </a-modal>
    </page-layout>
</template>

<script>
import { mapState } from 'vuex'
import PageLayout from '@/layouts/PageLayout'
import { getUserPosts,deletePost } from '@/services/user'

export default {
    name: 'teacherWorkPage',
    computed: {
        ...mapState('account', { currUser: 'user' })
    },
    components: { PageLayout },
    created() {
        this.fetchUserPosts();
    },
    data() {
        return {
            activeKey: 1,
            posts: [],
            showFullContent: null, // 控制显示完整内容的帖子ID
            deleteOpen: false,
            curPostId: null
        }
    },
    methods: {
        onTabChange(key) {
            this.activeKey = key;
        },
        fetchUserPosts() {
            getUserPosts(this.currUser.id).then(res => {
                if (res.data.code >= 0) {
                    this.posts = res.data.posts;
                    console.log('获取帖子信息成功:', this.posts);
                }
                else {
                    console.error('获取帖子信息失败');
                }
            }).catch(error => {
                console.error('获取帖子信息失败:', error);
            });
        },
        shouldShowReadMore(content) {
            return content.length > 60; // 判断内容长度
        },
        showDeleteMessage(id) {
            this.deleteOpen = true;
            this.curPostId = id;
        },
        handleDeleteOk() {
            this.deleteOpen = false;
            deletePost(this.curPostId).then(res => {
                if (res.data.code >= 0) {
                    this.fetchUserPosts();
                    console.log('删除帖子成功');
                }
                else {
                    console.error('删除帖子失败');
                }
            }).catch(error => {
                console.error('删除帖子失败:', error);
            });
        },
        handleDeleteCancel() {
            this.deleteOpen = false;
        }
    },
}
</script>

<style lang="less" scoped>
.page-layout {
    padding: 20px;
}

.content {
    .detail {
        line-height: 22px;
        max-width: 900px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: normal;
        transition: max-height 0.3s ease, white-space 0.3s ease;

        &.expanded {
            max-height: none;
            overflow: visible;
            text-overflow: clip;
        }
    }

    .read-more, .read-less {
        margin-top: 8px;
        cursor: pointer;
        color: @primary-color; // 使用主题颜色
    }
}

.demo-loadmore-list {
    min-height: 350px;
}
</style>
