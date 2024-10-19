import Mock from 'mockjs';

const students = Mock.mock({
    'students|10': [
        {
            id: 1,
            name: 'this is a name',
        }
    ],
});

// 模拟 getStudents 的接口返回
Mock.mock(/\/getStudents\//, 'get', (options) => {
    // 解析 URL 获取查询参数
    const url = new URL(options.url, window.location.origin);
    const id = url.searchParams.get('id');
    console.log(`获取用户ID为${id}的学生`);

    return {
        code: 0, // 模拟成功返回
        students: students.students
    };
});