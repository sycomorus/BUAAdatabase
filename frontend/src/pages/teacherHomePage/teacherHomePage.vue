<template>
    <page-layout :title='userName' :desc='userPersonalSignature'>
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
    </page-layout>
</template>

<script>
import PageLayout from '@/layouts/PageLayout'
import { getTeacherInfo } from '@/services/user'

export default {
    name: 'teacherHomePage',
    components: { PageLayout},
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
            userDegree: ''
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
                        this.userDegree = res.data.Degree;
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
}

.user-info-card {
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
</style>