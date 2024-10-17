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
            FullAddress: 'Wonderland, 123, 456',
            bio: 'I am Alice'
        },
        2: {
            name: 'Bob',
            email: 'bob@example.com',
            telephone: '0987654321',
            address: 'Nowhere',
            FullAddress: 'Nowhere, 098, 765',
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
