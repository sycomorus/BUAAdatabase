<template>
    <page-layout>
        <div slot="headerContent">
            <div class="title">{{ userName }}</div>
            <div class="sub-title">{{userPersonalSignature}}</div>
        </div>
        <template slot="extra">
            <head-info class="split-right" title="评分" :content="userRate"/>
            <head-info class="split-right" title="评分人数" :content="userRateNum"/>
        </template>
        <a-card :bordered="false" class="user-info-card">
            <a-row :gutter="16">
                <a-col :span="8">
                    <div class="user-info-label">性别</div>
                    <div class="user-info-content">{{ userGender }}</div>
                </a-col>
                <a-col :span="8">
                    <div class="user-info-label">年龄</div>
                    <div class="user-info-content">{{ userAge }}</div>
                </a-col>
                <a-col :span="8">
                    <div class="user-info-label">学历</div>
                    <div class="user-info-content">{{ userDegree }}</div>
                </a-col>
            </a-row>
            <a-divider class="custom-divider" />
            <a-row :gutter="16">
                <a-col :span="8">
                    <div class="user-info-label">邮箱:</div>
                    <div class="user-info-content">{{ userEmail }}</div>
                </a-col>
                <a-col :span="8">
                    <div class="user-info-label">电话:</div>
                    <div class="user-info-content">{{ userTelephone }}</div>
                </a-col>
                <a-col :span="8">
                    <div class="user-info-label">地址:</div>
                    <div class="user-info-content">{{ userAddress }}</div>
                </a-col>
            </a-row>
        </a-card>
        <a-card :bordered="false" class="user-bio-card">
            <a-row gutter="16">
                <a-col span="24">
                    <div class="user-info-label">个人简介:</div>
                    <div class="user-info-content">{{ userIntro }}</div>
                </a-col>
            </a-row>
        </a-card>
        <a-card v-if="userComments.length > 0" :bordered="false" class="user-bio-card">
            <div class="user-info-label">用户评论:</div>
            <div v-for="comment in userComments" :key="comment.id">
                <a-comment>
                    <div slot="author" class="author-rating">
                        <span class="author-name">{{ comment.authorName }}</span>
                        <a-rate :value="comment.rating" disabled allow-half class="rating"></a-rate>
                    </div>
                    <div slot="content" class="comment-content">
                        <p>{{ comment.content }}</p>
                    </div>
                    <div slot="datetime" class="author-rating">
                        {{ comment.date }}
                    </div>
                </a-comment>
                <a-divider class="custom-divider" v-if="index < userComments.length - 1" />
            </div>
        </a-card>
    </page-layout>
</template>

<script>
import PageLayout from '@/layouts/PageLayout'
import { getTeacherInfo } from '@/services/user'
import HeadInfo from '@/components/tool/HeadInfo'

export default {
    name: 'teacherHomePage',
    components: { PageLayout, HeadInfo},
    data() {
        return {
            userId: this.$route.params.id, // 获取路由参数中的id
            userName: '',
            userEmail: '',
            userTelephone: '',
            userAddress: '',
            userFullAddress: '',
            userPersonalSignature: '',
            userIntro: '',
            userAge: 0,
            userGender: '',
            userDegree: '',
            userRate: 0,
            userRateNum: 0,
            userComments: []
        }
    },
    created() {
        this.fetchUserInfo();
    },
    methods: {
        fetchUserInfo() {
            getTeacherInfo(this.userId)
                .then(response => {
                    const res = response.data;
                    if (res.code >= 0) {
                        this.userName = res.data.name;
                        this.userEmail = res.data.email || '这个人很懒，还什么都没有写';
                        this.userTelephone = res.data.telephone || '这个人很懒，还什么都没有写';
                        this.userAddress = res.data.address || '这个人很懒，还什么都没有写';
                        this.userPersonalSignature = res.data.personalSignature|| '这个人很懒，还什么都没有写';
                        this.userIntro = res.data.intro || '这个人很懒，还什么都没有写';
                        this.userAge = res.data.age || 0;
                        this.userGender = res.data.gender;
                        this.userDegree = res.data.degree;
                        this.userRate = res.data.rate;
                        this.userRateNum = res.data.rateNum;
                        this.userComments = res.data.comments;
                        console.log('获取用户信息成功:', res.data);
                    } else {
                        console.error('获取用户信息失败:', res.msg);
                    }
                })
                .catch(error => {
                    console.error('获取用户信息失败:', error);
                });
        }
    }
}
</script>

<style lang="less" scoped>
.page-layout {
    padding: 20px;
}


.user-info-card, .user-bio-card {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    margin-bottom: 30px;
}

.user-info-label {
    font-weight: bold;
    color: #555;
    margin-bottom: 4px;
}

.user-info-content {
    color: #333;
    font-size: 16px;
    white-space: pre-line;
}

.custom-divider {
    border-top: 2px solid #e8e8e8; /* 改变分割线的粗细和颜色 */
    margin: 16px 0; /* 调整上下间距 */
}

.author-rating {
    display: flex;
    align-items: center;
    margin-bottom: 8px; /* 底部间距 */
}

.author-name {
    font-weight: bold;
    font-size: 16px; /* 字体大小 */
    color: #333; /* 字体颜色 */
    margin-right: 8px; /* 名字与评分之间的间距 */
}

.rating {
    color: #fadb14; /* 评分的颜色 */
}

.comment-content p {
    font-size: 14px; /* 字体大小 */
    line-height: 1.5; /* 行高 */
    color: #555; /* 字体颜色 */
}
</style>