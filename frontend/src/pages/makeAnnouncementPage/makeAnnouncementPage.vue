<template>
    <page-layout>
        <div class="button-container">
            <a-button type="primary" @click="setAnnouncement" class="large-button">发布公告</a-button>
        </div>
        <a-modal
            :visible="drawerOpen"
            title="发布公告"
            @cancel="closeDrawer"
            @ok="submitAnnouncement"
            centered
            okText="提交"
            cancelText="取消"
        >
            <form @submit.prevent="submitAnnouncement">
                <a-form-item label="请输入公告内容">
                    <a-textarea v-model="comment" placeholder="请输入公告内容" auto-size />
                </a-form-item>
            </form>
        </a-modal>
    </page-layout>
</template>

<script>
import { mapState } from 'vuex'
import PageLayout from '@/layouts/PageLayout'
import { makeAnnouncement } from '@/services/user'

export default {
    name: 'makeAnnouncementPage',
    computed: {
        ...mapState('account', { currUser: 'user' })
    },
    components: { PageLayout },
    data() {
        return {
            drawerOpen: false,
            comment: ""
        }
    },
    methods: {
        closeDrawer() {
            this.drawerOpen = false;
            this.comment = '';
        },
        setAnnouncement() {
            this.drawerOpen = true;
        },
        submitAnnouncement() {
            if (!this.comment) {
                this.$message.error('公告不能为空！');
                return;
            }
            console.log('公告内容:', this.comment);
            makeAnnouncement(this.currUser.id, this.comment).then(res => {
                if (res.data.code >= 0) {
                    console.log('发布公告成功');
                    this.closeDrawer(); // 提交后关闭抽屉
                } else {
                    console.error('发布公告失败');
                }
            }).catch(error => {
                console.error('发布公告失败:', error);
            });
        },
    },
}
</script>

<style lang="less" scoped>
.page-layout {
    padding: 20px;
}
.button-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 40vh; /* 使容器高度占满整个视口 */
}
.large-button {
    font-size: 23px; /* 增大字体大小 */
    padding: 40px 80px; /* 增加内边距，使按钮看起来更大 */
    border-radius: 10px; /* 圆角 */
    text-align: center; /* 文字水平居中 */
    line-height: 0.5; /* 调整行高，使文字垂直居中 */
    width: 250px; /* 设置固定宽度，确保按钮大小一致 */
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

    .read-more,
    .read-less {
        margin-top: 8px;
        cursor: pointer;
        color: @primary-color; // 使用主题颜色
    }
}

.demo-loadmore-list {
    min-height: 350px;
}
</style>