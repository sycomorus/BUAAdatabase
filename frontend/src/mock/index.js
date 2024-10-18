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

// 设置全局延时
Mock.setup({
  timeout: '200-400'
})
