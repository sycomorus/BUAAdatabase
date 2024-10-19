import Mock from 'mockjs';

const teachers = Mock.mock({
    'teachers|10': [
        {
            id: 1,
            name: 'this is a name',
        }
    ],
});

Mock.mock(/\/getTeachers\//, 'get', (options) => {
    // 解析 URL 获取查询参数
    const url = new URL(options.url, window.location.origin);
    const id = url.searchParams.get('id');
    console.log(`获取用户ID为${id}的家教`);

    return {
        code: 0, // 模拟成功返回
        teachers: teachers.teachers
    };
});