import Mock from 'mockjs';

// 模拟用户信息接口
Mock.mock(/\/getStudentInfo\//, 'get', (options) => {
    const url = options.url;
    const id = url.split('id=')[1]; // 获取传递的用户ID

    // 模拟用户数据
    const users = {
        1: {
            name: 'Alice',
            email: 'alice@example.com',
            telephone: '1234567890',
            address: 'Wonderland',
            intro: '我是一名初三学生，目前主要需要补习的科目是数学和英语。数学方面主要是代数与几何部分，尤其是函数和几何证明这两块掌握得不够扎实。英语需要加强的是语法和阅读理解能力，尤其是提升阅读速度和扩大词汇量。\n我的学习态度积极，平时也有较强的学习主动性，但在一些难题和综合性较强的知识点上容易遇到瓶颈。希望通过家教的辅导，能够系统地梳理知识，提高解题技巧，并在即将到来的中考中取得更好的成绩。\n希望家教老师有耐心，能够根据我的实际情况制定教学计划，帮助我在短期内快速提升学习成绩。',
            personalSignature: 'I am Alice',
            gender: '女',
            age: 15,
            grade: "高三"
        },
        2: {
            name: 'Bob',
            email: 'bob@example.com',
            telephone: '0987654321',
            address: 'Nowhere',
            bio: 'I am Bob'
        },
        // 其他用户可以按需添加
    };

    // 如果用户存在，返回对应数据，否则返回错误
    if (users[id]) {
        return {
            code: 0,
            data: users[id],
        };
    } else {
        return {
            code: -1,
            date: ""
        };
    }
});
