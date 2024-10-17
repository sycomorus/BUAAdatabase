<template>
    <page-layout :title="'编辑家教主页'" :desc="'在这里你可以修改你的个人信息'">
        <a-card :bordered="false" class="edit-user-info-card">
            <a-form @submit.prevent="submitForm">
                <a-row gutter="32">
                    <a-col span="8">
                        <div class="user-info-label">年级</div>
                        <a-select v-model="editUserGrade" placeholder="请选择年级">
                            <a-select-option value="学龄前">学龄前</a-select-option>
                            <a-select-option value="小学一年级">小学一年级</a-select-option>
                            <a-select-option value="小学二年级">小学二年级</a-select-option>
                            <a-select-option value="小学三年级">小学三年级</a-select-option>
                            <a-select-option value="小学四年级">小学四年级</a-select-option>
                            <a-select-option value="小学五年级">小学五年级</a-select-option>
                            <a-select-option value="小学六年级">小学六年级</a-select-option>
                            <a-select-option value="初中一年级">初中一年级</a-select-option>
                            <a-select-option value="初中二年级">初中二年级</a-select-option>
                            <a-select-option value="初中三年级">初中三年级</a-select-option>
                            <a-select-option value="高中一年级">高中一年级</a-select-option>
                            <a-select-option value="高中二年级">高中二年级</a-select-option>
                            <a-select-option value="高中三年级">高中三年级</a-select-option>
                            <a-select-option value="本科生">本科生</a-select-option>
                        </a-select>
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
                        <div class="user-info-label">个性签名</div>
                        <a-input v-model="editUserSignature" placeholder="请输入个性签名" />
                    </a-col>
                </a-row>
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
import { getTeacherInfo, updateTeacherInfo } from '@/services/user'

export default {
    name: 'editTeacherHomePage',
    components: { PageLayout },
    data() {
        return {
            userId: this.$route.params.id, // 获取用户ID
            editUserGrade: '',
            editUserGender: '',
            editUserAge: 0,
            editUserEmail: '',
            editUserTelephone: '',
            editUserAddress: '',
            editUserIntro: '',
            editUserSignature: '', // 新增个性签名字段
        };
    },
    created() {
        this.fetchUserInfo(); // 页面加载时获取用户信息
    },
    methods: {
        fetchUserInfo() {
            getTeacherInfo(this.userId).then(response => {
                const res = response.data;
                if (res.code >= 0) {
                    const userData = res.data;
                    this.editUserGrade = userData.grade || '';
                    this.editUserGender = userData.gender || '';
                    this.editUserAge = userData.age || 0;
                    this.editUserEmail = userData.email || '';
                    this.editUserTelephone = userData.telephone || '';
                    this.editUserAddress = userData.address || '';
                    this.editUserIntro = userData.intro || '';
                    this.editUserSignature = userData.personalSignature || ''; // 获取个性签名信息
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
                grade: this.editUserGrade,
                gender: this.editUserGender,
                age: this.editUserAge,
                email: this.editUserEmail,
                telephone: this.editUserTelephone,
                address: this.editUserAddress,
                intro: this.editUserIntro,
                signature: this.editUserSignature,
            };
            updateTeacherInfo(this.userId, updatedUserInfo).then(response => {
                console.log(this.userId, updatedUserInfo);
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

<style lang="less" scoped>
.page-layout {
    padding: 20px;
}

.edit-user-info-card {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
}

.custom-divider {
    border-top: 2px solid #e8e8e8;
    margin: 16px 0;
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
</style>
