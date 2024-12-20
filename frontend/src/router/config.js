import TabsView from '@/layouts/tabs/TabsView'
//import BlankView from '@/layouts/BlankView'
// import PageView from '@/layouts/PageView'

// 路由配置
const options = {
  routes: [
    {
      path: '/login',
      name: '登录页',
      component: () => import('@/pages/login')
    },
    {
      path: '*',
      name: '404',
      component: () => import('@/pages/exception/404'),
    },
    {
      path: '/403',
      name: '403',
      component: () => import('@/pages/exception/403'),
    },
    {
      path: '/',
      name: '首页',
      component: TabsView,
      redirect: '/login',
      children: [
        // {
        //   path: 'dashboard',
        //   name: 'Dashboard',
        //   meta: {
        //     icon: 'dashboard',
        //     authority: {
        //       role: 'admin',
        //     }
        //   },
        //   component: BlankView,
        //   children: [
        //     {
        //       path: 'workplace',
        //       name: '工作台',
        //       component: () => import('@/pages/dashboard/workplace'),
        //     },
        //     {
        //       path: 'analysis',
        //       name: '分析页',
        //       component: () => import('@/pages/dashboard/analysis'),
        //     }
        //   ]
        // },
        {
          path: 'announcementPage',
          name: '公告',
          meta: {
            icon: 'dashboard',
            page: {
              closable: false
            },
          },
          component: () => import('@/pages/announcementPage'),
        },
        {
          path: 'jobSeekPage', // 这是针对教师的求职页面
          name: "广场",
          meta: {
            icon: "team",
            authority: {
              role: 'teacher', 
            }
          },
          component: () => import('@/pages/jobSeekPage')
        },
        {
          path: 'teacherPostPage', // 这是教师发布家教信息的页面
          name: "我要求聘",
          meta: {
            icon: "form",
            authority: {
              role: 'teacher'
            }
          },
          component: () => import('@/pages/teacherPostPage')
        },
        {
          path: 'teacherWorkPage', // 这是教师工作页面
          name: "我的工作",
          meta: {
            icon: "switcher",
            authority: {
              role: 'teacher'
            }
          },
          component: () => import('@/pages/teacherWorkPage')
        },
        {
          path : "hirePage", // 这是针对学生的招聘页面
          name: "广场",
          meta: {
            icon: "team",
            authority: {
              role: 'student'
            }
          },
          component: () => import('@/pages/hirePage')
        },
        {
          path: 'studentPostPage', // 这是学生发布招聘信息的页面
          name: "我要招聘",
          meta: {
            icon: "form",
            authority: {
              role: 'student'
            }
          },
          component: () => import('@/pages/studentPostPage')
        },
        {
          path: 'studentWorkPage',  // 这是学习资料页面
          name: "我的学习",
          meta: {
            icon: "book",
            authority: {
              role: 'student'
            }
          },
          component: () => import('@/pages/studentWorkPage')
        },
        {
          path: 'makeAnnouncementPage',
          name: "发布公告",
          meta: {
            icon: "dashboard",
            authority: {
              role: 'admin'
            }
          },
          component: () => import('@/pages/makeAnnouncementPage')
        },
        // {
        //   path: 'managePostsPage',
        //   name: "帖子管理",
        //   meta: {
        //     icon: "book",
        //     authority: {
        //       role: 'admin'
        //     }
        //   },
        //   component: () => import('@/pages/managePostsPage')
        // },
        {
          path: 'moderatePostsPage',
          name: "帖子审核",
          meta: {
            icon: "book",
            authority: {
              role: 'admin'
            }
          },
          component: () => import('@/pages/moderatePostsPage')
        },
        {
          path: 'manageUserPage',
          name: "用户管理",
          meta: {
            icon: "team",
            authority: {
              role: 'admin'
            }
          },
          component: () => import('@/pages/manageUserPage')
        },
        {
          path: 'user/studentHomePage/:id',
          name: '学生主页',
          meta: {
            invisible: true
          },
          component: () => import('@/pages/studentHomePage')
        },
        {
          path : 'user/editStudentHomePage/:id',
          name: '编辑学生主页',
          meta: {
            invisible: true
          },
          component: () => import('@/pages/editStudentHomePage')
        },
        {
          path: 'user/teacherHomePage/:id',
          name: '家教主页',
          meta: {
            invisible: true
          },
          component: () => import('@/pages/teacherHomePage')
        },
        {
          path : 'user/editTeacherHomePage/:id',
          name: '编辑家教主页',
          meta: {
            invisible: true
          },
          component: () => import('@/pages/editTeacherHomePage')
        },
        {
          path : 'postDetail/:id',
          name: '帖子详情',
          meta: {
            invisible: true
          },
          component: () => import('@/pages/postDetail')
        },
        {
          path: 'managePostDetail/:id',
          name: '管理详情',
          meta: {
            invisible: true
          },
          component: () => import('@/pages/managePostDetail')
        },
        {
          path: 'moderatePostDetail/:id',
          name: '审核详情',
          meta: {
            invisible: true
          },
          component: () => import('@/pages/moderatePostDetail')
        },
        // {
        //   path: 'form',
        //   name: '表单页',
        //   meta: {
        //     authority: {
        //       role: 'admin'
        //     },
        //     icon: 'form',
        //     page: {
        //       cacheAble: false
        //     }
        //   },
        //   component: PageView,
        //   children: [
        //     {
        //       path: 'basic',
        //       name: '基础表单',
        //       component: () => import('@/pages/form/basic'),
        //     },
        //     {
        //       path: 'step',
        //       name: '分步表单',
        //       component: () => import('@/pages/form/step'),
        //     },
        //     {
        //       path: 'advance',
        //       name: '高级表单',
        //       component: () => import('@/pages/form/advance'),
        //     }
        //   ]
        // },
        // {
        //   path: 'list',
        //   name: '列表页',
        //   meta: {
        //     authority: {
        //       role: 'admin'
        //     },
        //     icon: 'table'
        //   },
        //   component: PageView,
        //   children: [
        //     {
        //       path: 'query',
        //       name: '查询表格',
        //       meta: {
        //         authority: 'queryForm',
        //       },
        //       component: () => import('@/pages/list/QueryList'),
        //     },
        //     {
        //       path: 'query/detail/:id',
        //       name: '查询详情',
        //       meta: {
        //         highlight: '/list/query',
        //         invisible: true
        //       },
        //       component: () => import('@/pages/Demo')
        //     },
        //     {
        //       path: 'primary',
        //       name: '标准列表',
        //       component: () => import('@/pages/list/StandardList'),
        //     },
        //     {
        //       path: 'card',
        //       name: '卡片列表',
        //       component: () => import('@/pages/list/CardList'),
        //     },
        //     {
        //       path: 'search',
        //       name: '搜索列表',
        //       component: () => import('@/pages/list/search/SearchLayout'),
        //       children: [
        //         {
        //           path: 'article',
        //           name: '文章',
        //           component: () => import('@/pages/list/search/ArticleList'),
        //         },
        //         {
        //           path: 'application',
        //           name: '应用',
        //           component: () => import('@/pages/list/search/ApplicationList'),
        //         },
        //         {
        //           path: 'project',
        //           name: '项目',
        //           component: () => import('@/pages/list/search/ProjectList'),
        //         }
        //       ]
        //     }
        //   ]
        // },
        // {
        //   path: 'details',
        //   name: '详情页',
        //   meta: {
        //     authority: {
        //       role: 'admin'
        //     },
        //     icon: 'profile'
        //   },
        //   component: BlankView,
        //   children: [
        //     {
        //       path: 'basic',
        //       name: '基础详情页',
        //       component: () => import('@/pages/detail/BasicDetail')
        //     },
        //     {
        //       path: 'advance',
        //       name: '高级详情页',
        //       component: () => import('@/pages/detail/AdvancedDetail')
        //     }
        //   ]
        // },
        // {
        //   path: 'result',
        //   name: '结果页',
        //   meta: {
        //     authority: {
        //       role: 'admin'
        //     },
        //     icon: 'check-circle-o',
        //   },
        //   component: PageView,
        //   children: [
        //     {
        //       path: 'success',
        //       name: '成功',
        //       component: () => import('@/pages/result/Success')
        //     },
        //     {
        //       path: 'error',
        //       name: '失败',
        //       component: () => import('@/pages/result/Error')
        //     }
        //   ]
        // },
        // {
        //   path: 'exception',
        //   name: '异常页',
        //   meta: {
        //     icon: 'warning',
        //     authority: {
        //       role: 'admin'
        //     }
        //   },
        //   component: BlankView,
        //   children: [
        //     {
        //       path: '404',
        //       name: 'Exp404',
        //       component: () => import('@/pages/exception/404')
        //     },
        //     {
        //       path: '403',
        //       name: 'Exp403',
        //       component: () => import('@/pages/exception/403')
        //     },
        //     {
        //       path: '500',
        //       name: 'Exp500',
        //       component: () => import('@/pages/exception/500')
        //     }
        //   ]
        // },
        // {
        //   path: 'components',
        //   name: '内置组件',
        //   meta: {
        //     authority: {
        //       role: 'admin'
        //     },
        //     icon: 'appstore-o'
        //   },
        //   component: PageView,
        //   children: [
        //     {
        //       path: 'taskCard',
        //       name: '任务卡片',
        //       component: () => import('@/pages/components/TaskCard')
        //     },
        //     {
        //       path: 'palette',
        //       name: '颜色复选框',
        //       component: () => import('@/pages/components/Palette')
        //     },
        //     {
        //       path: 'table',
        //       name: '高级表格',
        //       component: () => import('@/pages/components/table')
        //     }
        //   ]
        // },
        // {
        //   name: '验权表单',
        //   path: 'auth/form',
        //   meta: {
        //     icon: 'file-excel',
        //     authority: {
        //       role: 'admin'
        //     }
        //   },
        //   component: () => import('@/pages/form/basic')
        // },
        // {
        //   name: '带参菜单',
        //   path: 'router/query',
        //   meta: {
        //     icon: 'project',
        //     authority: {
        //       role: 'admin'
        //     },
        //     query: {
        //       name: '菜单默认参数'
        //     }
        //   },
        //   component: () => import('@/pages/Demo')
        // },
        // {
        //   name: '动态路由菜单',
        //   path: 'router/dynamic/:id',
        //   meta: {
        //     icon: 'project',
        //     authority: {
        //       role: 'admin'
        //     }, 
        //     params: {
        //       id: 123
        //     }
        //   },
        //   component: () => import('@/pages/Demo')
        // },
        // {
        //   name: 'Ant Design Vue',
        //   path: 'antdv',
        //   meta: {
        //     authority: {
        //       role: 'admin'
        //     }, 
        //     icon: 'ant-design',
        //     link: 'https://www.antdv.com/docs/vue/introduce-cn/'
        //   }
        // },
        // {
        //   name: '使用文档',
        //   path: 'document',
        //   meta: {
        //     authority: {
        //       role: 'admin'
        //     }, 
        //     icon: 'file-word',
        //     link: 'https://iczer.gitee.io/vue-antd-admin-docs/'
        //   }
        // }
      ]
    },
  ]
}

export default options
