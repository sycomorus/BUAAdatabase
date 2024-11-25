import Mock from 'mockjs';

// 模拟公告数据
const announcements = Mock.mock({
    'announcements|5': [
        {
            title: '这是一个公告', // 随机生成 3-5 个单词的标题
            content: '这是一段内容', // 随机生成 2-4 段内容
            date: '2024-11-25', // 随机生成日期
        }
    ],
});

// 使用 Mock.js 拦截请求
Mock.mock(/\/getAnnouncements\//, 'get', () => {
    console.log('获取公告列表');

    return {
        code: 0, // 模拟成功返回
        data: {
            announcements: announcements.announcements, // 返回模拟的公告数据
        }
    };
});
