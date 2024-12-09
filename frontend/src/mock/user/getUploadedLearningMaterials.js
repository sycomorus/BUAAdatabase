import Mock from 'mockjs';
Mock.mock(/\/getUploadedLearningMaterials\//, 'get', (options) => {
    // 解析 URL 获取查询参数
    const url = new URL(options.url, window.location.origin);
    const id = url.searchParams.get('id');
    console.log(`获取用户ID为${id}的用户的已上传学习资料`);
    const data = [{
        "fileName": "文件1",
        "downloadLink": "http://www.baidu.com",
        "target": "张三",
        "date": "2021-06-01",
    },
    {
        "fileName": "文件2",
        "downloadLink": "http://www.baidu.com",
        "target": "李四",
        "date": "2021-06-02",
    }]
    const uploadedLearningMaterials = Mock.mock({
        code: 0,
        data: data,
    });

    return uploadedLearningMaterials;
});
