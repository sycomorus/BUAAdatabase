import Mock from 'mockjs';

// Mock 数据
const todosData = Mock.mock({
    'todos|5-10': [
        {
            'id': 1,
            'postId': 1,
            'postTitle': "诚信求聘",
            'accepterName': "乌啦啦",
            "accepterId": 1
        }
    ]
});

// 设置 mock 接口
Mock.mock(/\/getTodos\//, 'get', (options) => {
    // 解析 URL 获取查询参数
    const url = new URL(options.url, window.location.origin);
    const id = url.searchParams.get('id');
    console.log(`获取用户ID为${id}的用户的待办`);

    return {
        code: 0, // 模拟成功返回
        todos: todosData.todos
    };
});
