import Mock from 'mockjs';

// 模拟教师信息接口
Mock.mock(/\/getTeacherInfo\//, 'get', (options) => {
    const url = options.url;
    const id = url.split('id=')[1]; // 获取传递的用户ID

    // 模拟教师数据
    const teachers = {
        1: {
            name: '张老师',
            email: 'zhanglaoshi@example.com',
            telephone: '12345678901',
            address: '北京市朝阳区',
            personalSignature: '热爱教学',
            intro: '一位资深的数学老师，教授代数和几何。',
            gender: '男',
            age: 35,
            degree: '硕士',
            rate: 4.5,
            rateNum: 120,
            comments: [
                {
                    id: 1,
                    authorName: '学生A',
                    rating: 5,
                    content: '老师讲得非常好，受益匪浅！',
                    date: '2021-01-01'
                },
                {
                    id: 2,
                    authorName: '学生B',
                    rating: 4,
                    content: '课程内容丰富，期待下次上课。',
                    date: '2021-01-02'
                }
            ]
        },
        2: {
            name: '李老师',
            email: 'lilaoshi@example.com',
            telephone: '09876543210',
            address: '上海市浦东新区',
            personalSignature: '教学是我最大的热爱',
            intro: '一位英语老师，专注于口语和写作。',
            gender: '女',
            age: 30,
            Degree: '硕士',
            rate: 4.8,
            rateNum: 80,
            comments: []
        },
        // 可以添加更多教师信息
    };

    // 如果教师存在，返回对应数据，否则返回错误
    if (teachers[id]) {
        return {
            code: 0,
            data: teachers[id],
        };
    } else {
        return {
            code: -1,
            message: '用户不存在',
        };
    }
});
