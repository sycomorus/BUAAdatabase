<template>
    <page-layout :title='userName' :desc = 'userBio'>
        <div>
        </div>
    </page-layout>
</template>

<script>
import PageLayout from '@/layouts/PageLayout'
import { getStudentInfo } from '@/services/user'

export default {
    name: 'studentHomePage',
    components: { PageLayout },
    data() {
        return {
            userId: this.$route.params.id, // 获取路由参数中的id
            userName: '',
            userEmail: '',
            userTelephone: '',
            userAddress: '',
            userFullAddress: '',
            userBio: '',
        }
    },
    created() {
        this.fetchUserInfo();
    },
    methods: {
        fetchUserInfo() {
            // 调用 getUserInfo 方法，获取用户信息
            getStudentInfo(this.userId)
                .then(response => {
                    const res = response.data;
                    if (res.code >= 0) {
                        this.userName = res.data.name;
                        this.userEmail = res.data.email || '这个人很懒，还什么都没有写';
                        this.userTelephone = res.data.telephone || '这个人很懒，还什么都没有写';
                        this.userAddress = res.data.address || '这个人很懒，还什么都没有写';
                        this.userFullAddress = res.data.fullAddress || '这个人很懒，还什么都没有写';
                        this.userBio = res.data.bio || '这个人很懒，还什么都没有写';
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

</style>