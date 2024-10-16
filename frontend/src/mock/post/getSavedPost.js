// mock.js
import Mock from 'mockjs'

// 模拟获取保存表单数据的接口
Mock.mock(/\/getSavedPost\//, 'get', (options) => {
    // 解析 URL 获取查询参数
    const url = new URL(options.url, window.location.origin);
    const id = url.searchParams.get('id');

    if (id === '1') {
        return {
            code: 0,  // 返回0表示成功
            data: {
                title: '教师职位招聘',
                startDate: '2024-10-01',
                endDate: '2024-12-31',
                subjects: ['语文', '数学'],
                location: ['北京', '海淀区'],
                fullLocation: '中关村大街',
                telephoneNumber: '1234567890',
                emailAddress: 'example@test.com',
                content: '具备5年教学经验，擅长语文与数学教学。',
            },
        };
    } else if (id == '2') {
        return {
            code: 0,  // 返回0表示成功
            data: {
                title: '学生家教',
                startDate: '2024-10-01',
                endDate: '2024-12-31',
                subjects: ['英语', '数学'],
                location: ['上海', '浦东新区'],
                fullLocation: '陆家嘴',
                telephoneNumber: '1234567890',
                emailAddress: '',
            }
        }
    } else {
        return {
            code: -1,  // 返回-1表示没有保存的草稿
            message: '没有找到草稿信息',
        };
    }
});
