import Mock from 'mockjs'
import '@/mock/user/current'
import '@/mock/project'
import '@/mock/user/login'
import '@/mock/user/getStudentInfo'
import '@/mock/workplace'
import '@/mock/goods'
import '@/mock/list'
import '@/mock/post/sendPost'
import '@/mock/post/savePost'
import '@/mock/post/getSavedPost'
import '@/mock/post/getPosts'
import '@/mock/user/updateStudentInfo'
import '@/mock/post/getPost'
import '@/mock/post/getUserPosts'
import '@/mock/user/getStudents'
import "@/mock/user/getTodos"
import "@/mock/user/getTeachers"
import "@/mock/user/getLearningMaterials"
import "@/mock/user/getTeacherInfo"
import "@/mock/user/getNotices"
import "@/mock/user/getAnnouncements"
import "@/mock/user/resetPassword"
import "@/mock/user/getAvatar"
import "@/mock/user/uploadAvatar"

// 设置全局延时
Mock.setup({
  timeout: '200-400'
})
