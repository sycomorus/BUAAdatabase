import Mock from 'mockjs';

const learningMaterials = Mock.mock({
    'materials|10': [
        {
            id: '1',
            filename: '123.pdf', // 文件名
            publisher: 'asd', // 发布者名称
            downloadLink: 'http://www.bilibili.com', // 下载链接
            date: '2021-06-01', // 发布日期
        }
    ],
});

Mock.mock(/\/getLearningMaterials\//, 'get', (options) => {
    // 解析 URL 获取查询参数
    const url = new URL(options.url, window.location.origin);
    const userId = url.searchParams.get('userId'); // 获取用户ID
    console.log(`获取用户ID为${userId}的学习资料`);

    return {
        code: 0, // 模拟成功返回
        materials: learningMaterials.materials
    };
});
