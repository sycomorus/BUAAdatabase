<template>
    <page-layout :title="'编辑学生主页'" :desc="'在这里你可以修改你的个人信息'">
        <a-card :bordered="false" class="edit-user-info-card">
            <a-form @submit.prevent="submitForm">
                <a-row gutter="32">
                    <a-col span="8">
                        <div class="user-info-label">姓名</div>
                        <a-input v-model="editUserName" placeholder="请输入姓名" />
                    </a-col>
                    <a-col span="8">
                        <div class="user-info-label">性别</div>
                        <a-select v-model="editUserGender" placeholder="请选择性别">
                            <a-select-option value="男">男</a-select-option>
                            <a-select-option value="女">女</a-select-option>
                        </a-select>
                    </a-col>
                    <a-col span="8">
                        <div class="user-info-label">年龄</div>
                        <a-input-number v-model="editUserAge" min="0" placeholder="请输入年龄" />
                    </a-col>
                </a-row>
                <a-divider class="custom-divider" />
                <a-row gutter="32">
                    <a-col span="8">
                        <div class="user-info-label">邮箱</div>
                        <a-input v-model="editUserEmail" placeholder="请输入邮箱" />
                    </a-col>
                    <a-col span="8">
                        <div class="user-info-label">电话</div>
                        <a-input v-model="editUserTelephone" placeholder="请输入电话" />
                    </a-col>
                    <a-col span="8">
                        <div class="user-info-label">地址</div>
                        <a-input v-model="editUserAddress" placeholder="请输入地址" />
                    </a-col>
                </a-row>
                <a-divider class="custom-divider" />
                <a-row gutter="16">
                    <a-col span="24">
                        <div class="user-info-label">个人简介</div>
                        <a-textarea v-model="editUserIntro" rows="4" placeholder="请输入个人简介"></a-textarea>
                    </a-col>
                </a-row>
                <a-row>
                    <a-col span="24" style="text-align: center; margin-top: 20px;">
                        <a-button type="primary" html-type="submit">保存</a-button>
                    </a-col>
                </a-row>
            </a-form>
        </a-card>
    </page-layout>
</template>

<script>
import PageLayout from '@/layouts/PageLayout'
import { getStudentInfo, updateStudentInfo } from '@/services/user' // 假设有 `updateStudentInfo` 接口

export default {
    name: 'editStudentHomePage',
    components: { PageLayout },
    data() {
        return {
            userId: this.$route.params.id, // 获取用户ID
            editUserName: '',
            editUserGender: '',
            editUserAge: 0,
            editUserEmail: '',
            editUserTelephone: '',
            editUserAddress: '',
            editUserIntro: '',
        };
    },
    created() {
        this.fetchUserInfo(); // 页面加载时获取用户信息
    },
    methods: {
        fetchUserInfo() {
            getStudentInfo(this.userId).then(response => {
                const res = response.data;
                if (res.code >= 0) {
                    const userData = res.data;
                    this.editUserName = userData.name || '';
                    this.editUserGender = userData.gender || '';
                    this.editUserAge = userData.age || 0;
                    this.editUserEmail = userData.email || '';
                    this.editUserTelephone = userData.telephone || '';
                    this.editUserAddress = userData.address || '';
                    this.editUserIntro = userData.intro || '';
                } else {
                    console.error('获取用户信息失败:', res.msg);
                }
            }).catch(error => {
                console.error('获取用户信息失败:', error);
            });
        },
        submitForm() {
            // 提交编辑后的用户信息
            const updatedUserInfo = {
                name: this.editUserName,
                gender: this.editUserGender,
                age: this.editUserAge,
                email: this.editUserEmail,
                telephone: this.editUserTelephone,
                address: this.editUserAddress,
                intro: this.editUserIntro,
            };
            updateStudentInfo(this.userId, updatedUserInfo).then(response => {
                if (response.data.code >= 0) {
                    this.$message.success('修改个人资料成功！');
                } else {
                    this.$message.error('修改个人资料失败！');
                }
            }).catch(error => {
                this.$message.error('提交失败，请稍后重试');
                console.error('提交用户信息失败:', error);
            });
        }
    }
}
</script>
