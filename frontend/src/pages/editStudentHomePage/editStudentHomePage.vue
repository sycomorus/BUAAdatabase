<template>
    <page-layout :title="'编辑学生主页'" :desc="'在这里你可以修改你的个人信息'">
        <a-card :bordered="false" class="edit-user-info-card">
            <a-form @submit.prevent="submitForm">
                <a-row gutter="0">
                    <a-col span="4">
                        <div class="container">
                            <a-avatar :src="userAvatar" shape="square" :size="120" />
                            <a-upload class="avatar-uploader" :file-list="fileList" :before-upload="beforeUpload"
                                :remove="handleRemove">
                                <a-button>
                                    <upload-outlined></upload-outlined>
                                    Select File
                                </a-button>
                            </a-upload>
                            <a-button type="primary" :disabled="fileList.length === 0" style="margin-top: 16px"
                                @click="handleUpload">
                                {{ uploading ? 'Uploading' : 'Start Upload' }}
                            </a-button>
                        </div>
                    </a-col>
                    <a-col span="20">
                        <a-row gutter="10">
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
                        <a-divider class="custom-divider1" />
                        <a-row gutter="10">
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
import { getStudentInfo, updateStudentInfo, uploadAvatar, getAvatar } from '@/services/user'
import { mapState } from 'vuex'

export default {
    name: 'editStudentHomePage',
    components: { PageLayout },
    computed: {
        ...mapState('account', { currUser: 'user' }),
    },
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
            userAvatar: '',
            fileList: [],
        };
    },
    created() {
        if (this.currUser.id !== this.userId) {
            this.$router.push('/404');
        }
        this.fetchUserInfo(); // 页面加载时获取用户信息
        this.fetchUserAvatar();
    },
    methods: {
        fetchUserInfo() {
            getStudentInfo(this.userId).then(response => {
                const res = response.data;
                if (res.code >= 0) {
                    const userData = res.data;
                    this.editUserGrade = userData.grade || '';
                    this.editUserGender = userData.gender || '';
                    this.editUserAge = userData.age || '';
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
                personalSignature: this.editUserSignature,
            };
            updateStudentInfo(this.userId, updatedUserInfo).then(response => {
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
        },
        beforeUpload(file) {
            const isJpgOrPng = file.type === 'image/jpeg' || file.type === 'image/png';
            if (!isJpgOrPng) {
                this.$message.error('你只能上传 JPG/PNG 文件!');
            }
            const isLt2M = file.size / 1024 / 1024 < 2;
            if (!isLt2M) {
                this.$message.error('图片必须小于 2MB!');
            }
            if (isJpgOrPng && isLt2M) {
                this.fileList = [file];
            }
            return false;
        },
        handleRemove() {
            this.fileList = [];
            return false;
        },
        handleUpload() {
            if (this.fileList.length === 0) {
                this.$message.error('请选择一个文件');
                return;
            }
            const formData = new FormData();
            formData.append('file', this.fileList[0]);
            const jsonData = {
                id: this.userId,
            };
            formData.append('data', JSON.stringify(jsonData));
            uploadAvatar(formData).then(response => {
                if (response.data.code >= 0) {
                    this.$message.success('上传头像成功');
                } else {
                    this.$message.error(response.data.message);
                }
            }).catch(error => {
                this.$message.error('上传头像失败');
                console.error('上传头像失败:', error);
            });
        },
        fetchUserAvatar() {
            getAvatar(this.userId).then(response => {
                const res = response.data;
                if (res.code >= 0) {
                    this.userAvatar = res.avatar;
                    console.log('获取用户头像成功');
                }
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

.custom-divider1 {
    border-top: 2px solid #e8e8e8;
    margin-top: 40px;
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

.avatar-uploader {
    display: flex;
    align-items: center;
    flex-direction: column;
    margin-top: 8px;
}

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>