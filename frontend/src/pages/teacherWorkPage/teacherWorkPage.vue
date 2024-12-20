<template>
    <page-layout>
        <a-card :bordered="false">
            <div>
                <a-tabs size="large" :tabBarStyle="{ textAlign: 'center' }" @change="onTabChange"
                    style="padding: 0 10px;">
                    <a-tab-pane :key="1" tab="我的帖子">
                        <a-list item-layout="horizontal">
                            <a-list-item v-for="(post, index) in posts" :key="index">
                                <a-list-item-meta :title="post.title">
                                    <div slot="description">
                                        <div class="content">
                                            <div class="detail" :class="{ 'expanded': showFullContent === post.id }">
                                                {{ showFullContent === post.id || !shouldShowReadMore(post.content) ?
                                                    post.content :
                                                    post.content.slice(0, 60) + '...' }}
                                            </div>
                                            <div class="read-more"
                                                v-if="shouldShowReadMore(post.content) && showFullContent !== post.id">
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
                    <a-tab-pane key="2" tab="我的学生">
                        <a-list item-layout="horizontal">
                            <a-list-item v-for="(student, index) in students" :key="index">
                                <a-list-item-meta :title="student.name"></a-list-item-meta>
                                <div slot="actions">
                                    <router-link :to="{ name: '学生主页', params: { id: student.id } }">
                                        <a-button type="link">学生主页</a-button>
                                    </router-link>
                                    <a-button type="link" @click="publishLearningMaterial(student.id)">发布学习资料</a-button>
                                    <a-button type="link"
                                        @click="showUnlinkStudentMessage(student.id)">解除师生关系</a-button>
                                </div>
                            </a-list-item>
                        </a-list>
                    </a-tab-pane>
                    <a-tab-pane key="3" tab="我的待办">
                        <a-list item-layout="horizontal">
                            <a-list-item v-for="(todo, index) in todos" :key="index">
                                <div>
                                    您发布的求聘帖
                                    <router-link
                                        :to="{ name: '帖子详情', params: { id: todo.postId, showAccept: false } }">“{{
                                            todo.postTitle }}”</router-link>
                                    被用户<router-link :to="{ name: '学生主页', params: { id: todo.accepterId } }">“{{
                                        todo.accepterName }}”</router-link>
                                    所接受
                                </div>
                                <div slot="actions">
                                    <a-button type="link" @click="showAcceptMessgae(todo.accepterId)">接受</a-button>
                                    <a-button type="link" @click="showRefuseMessage(todo.accepterId)">拒绝</a-button>
                                </div>
                            </a-list-item>
                        </a-list>
                    </a-tab-pane>
                    <a-tab-pane key="4" tab="已上传学习文件">
                        <a-list item-layout="horizontal">
                            <a-list-item v-for="(learningMaterial, index) in uploadedLearningMaterials" :key="index">
                                <a-list-item-meta :title="learningMaterial.fileName">
                                    <div slot="description">
                                        <div>于<strong>{{ learningMaterial.date }}</strong>上传给<strong>{{
                                                learningMaterial.target }}</strong></div>
                                    </div>
                                </a-list-item-meta>
                                <div slot="actions">
                                    <a :href=learningMaterial.downloadLink tatget="_blank">
                                        <a-button type="link">下载</a-button>
                                    </a>
                                </div>
                            </a-list-item>
                        </a-list>
                    </a-tab-pane>
                </a-tabs>
            </div>
        </a-card>

        <!-- 删除帖子模态框 -->
        <a-modal :visible="deleteOpen" title="警告" @ok="handleDeleteOk" @cancel="handleDeleteCancel">
            <p>您确认要删除该帖子吗？</p>
        </a-modal>

        <!-- 解除师生关系模态框 -->
        <a-modal :visible="unlinkOpen" title="警告" @ok="handleUnlinkOk" @cancel="handleUnlinkCancel">
            <p>您确认要解除与该学生的关系吗？</p>
        </a-modal>
        <!-- 接受学生求职请求模态框 -->
        <a-modal :visible="acceptOpen" title="提示" @ok="handleAcceptOk" @cancel="handleAcceptCancel">
            <p>您确认要接受该用户的请求吗？</p>
        </a-modal>
        <!-- 拒绝学生求职请求模态框 -->
        <a-modal :visible="refuseOpen" title="提示" @ok="handleRefuseOk" @cancel="handleRefuseCancel">
            <p>您确认要拒绝该用户的请求吗？</p>
        </a-modal>
        <!-- 发布学习资料抽屉 -->
        <a-drawer :visible="drawerOpen" class="custom-class" root-class-name="root-class-name"
            :root-style="{ color: 'blue' }" style="color: red" title="发布学习资料" placement="right" @close="closeDrawer">
            <a-upload class="avatar-uploader" :file-list="fileList" :before-upload="beforeUpload"
                :remove="handleRemove">
                <a-button>
                    <upload-outlined></upload-outlined>
                    选择文件
                </a-button>
            </a-upload>
            <a-button type="primary" :disabled="fileList.length === 0" style="margin-top: 16px"
                @click="submitLearningMaterial">
                {{ uploading ? 'Uploading' : '开始上传' }}
            </a-button>
        </a-drawer>
    </page-layout>
</template>

<script>
import { mapState } from 'vuex'
import PageLayout from '@/layouts/PageLayout'
import { getUserPosts, deletePost, getStudents, unlink, submitLearningMaterial, getTodos, link, refuseLink, getUploadedLearningMaterials } from '@/services/user'

export default {
    name: 'teacherWorkPage',
    computed: {
        ...mapState('account', { currUser: 'user' })
    },
    components: { PageLayout },
    created() {
        this.fetchUserPosts();
        this.fetchStudents();
        this.fetchTodos();
        this.fetchUploadedLearningMaterial();
    },
    data() {
        return {
            activeKey: 1,
            posts: [],
            showFullContent: null, // 控制显示完整内容的帖子ID
            deleteOpen: false,
            unlinkOpen: false, // 控制解除师生关系模态框
            curPostId: null,
            curStudentId: null,
            students: [],
            drawerOpen: false,
            fileName: '',
            downloadLink: '',
            todos: [],
            curAccepterId: null,
            curRefuseId: null,
            acceptOpen: false,
            refuseOpen: false,
            fileList: [],
            uploadedLearningMaterials: []
        }
    },
    methods: {
        onTabChange(key) {
            this.activeKey = key;
        },
        fetchTodos() {
            getTodos(this.currUser.id).then(res => {
                if (res.data.code >= 0) {
                    this.todos = res.data.todos;
                    console.log('获取待办事项成功:', this.todos);
                } else {
                    console.error('获取待办事项失败');
                }
            }).catch(error => {
                console.error('获取待办事项失败:', error);
            });
        },
        fetchStudents() {
            getStudents(this.currUser.id).then(res => {
                if (res.data.code >= 0) {
                    this.students = res.data.students;
                    console.log('获取学生信息成功:', this.students);
                } else {
                    console.error('获取学生信息失败');
                }
            }).catch(error => {
                console.error('获取学生信息失败:', error);
            });
        },
        fetchUserPosts() {
            getUserPosts(this.currUser.id).then(res => {
                if (res.data.code >= 0) {
                    this.posts = res.data.posts;
                    console.log('获取帖子信息成功:', this.posts);
                } else {
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
                } else {
                    console.error('删除帖子失败');
                }
            }).catch(error => {
                console.error('删除帖子失败:', error);
            });
        },
        handleDeleteCancel() {
            this.deleteOpen = false;
        },
        showUnlinkStudentMessage(id) {
            this.unlinkOpen = true;
            this.curStudentId = id;
        },
        handleUnlinkOk() {
            this.unlinkOpen = false;
            unlink(this.currUser.id, this.curStudentId).then(res => {
                if (res.data.code >= 0) {
                    this.fetchStudents(); // 刷新学生列表
                    console.log('解除师生关系成功');
                } else {
                    console.error('解除师生关系失败');
                }
            }).catch(error => {
                console.error('解除师生关系失败:', error);
            });
        },
        handleUnlinkCancel() {
            this.unlinkOpen = false;
        },
        closeDrawer() {
            this.drawerOpen = false;
            this.fileName = '';
            this.downloadLink = '';
        },
        publishLearningMaterial(id) {
            this.drawerOpen = true;
            this.curStudentId = id;
        },
        submitLearningMaterial() {
            const formData = new FormData();
            formData.append('file', this.fileList[0]);
            const jsonData = {
                id: this.currUser.id,
                teacher: this.currUser.name,
                studentId: this.curStudentId,
            };
            formData.append('data', JSON.stringify(jsonData));

            // 这里可以添加实际的提交逻辑
            submitLearningMaterial(formData).then(res => {
                if (res.data.code >= 0) {
                    this.$message.success('发布学习资料成功');
                    this.fileList = [];
                    this.closeDrawer(); // 提交后关闭抽屉
                    this.fetchUploadedLearningMaterial(); // 刷新已上传学习文件
                } else {
                    console.error('发布学习资料失败', res.data.message);
                }
            }).catch(error => {
                console.error('发布学习资料失败:', error);
            });
        },
        showAcceptMessgae(id) {
            this.curAccepterId = id;
            this.acceptOpen = true;
        },
        handleAcceptOk() {
            this.acceptOpen = false;
            link(this.currUser.id, this.curAccepterId).then(res => {
                if (res.data.code >= 0) {
                    this.fetchTodos(); // 刷新待办事项
                    this.fetchStudents(); // 刷新学生列表
                    console.log('接受学生求职请求成功:', this.curAccepterId);
                } else {
                    console.error('接受学生求职请求失败');
                }
            }).catch(error => {
                console.error('接受学生求职请求失败:', error);
            });
        },
        handleAcceptCancel() {
            this.acceptOpen = false;
        },
        showRefuseMessage(id) {
            this.curRefuseId = id;
            this.refuseOpen = true;
        },
        handleRefuseOk() {
            this.refuseOpen = false;
            // 这里可以添加实际的拒绝逻辑
            refuseLink(this.currUser.id, this.curRefuseId).then(res => {
                if (res.data.code >= 0) {
                    this.fetchTodos(); // 刷新待办事项
                    console.log('拒绝学生求职请求成功:', this.curRefuseId);
                } else {
                    console.error('拒绝学生求职请求失败');
                }
            }).catch(error => {
                console.error('拒绝学生求职请求失败:', error);
            });
            console.log('拒绝学生求职请求:', this.curRefuseId);
        },
        handleRefuseCancel() {
            this.refuseOpen = false;
        },
        beforeUpload(file) {
            if (file.size / 1024 / 1024 > 5) {
                this.$message.error('文件必须小于 5MB!');
            } else {
                this.fileList = [file];
            }
            return false;
        },
        handleRemove() {
            this.fileList = [];
            return false;
        },
        fetchUploadedLearningMaterial() {
            getUploadedLearningMaterials(this.currUser.id).then(res => {
                if (res.data.code >= 0) {
                    this.uploadedLearningMaterials = res.data.data;
                    console.log('获取已上传学习文件成功:', this.uploadedLearningMaterials);
                } else {
                    console.error('获取已上传学习文件失败');
                }
            }).catch(error => {
                console.error('获取已上传学习文件失败:', error);
            });
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
