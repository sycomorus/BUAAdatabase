import Mock from 'mockjs';

// 模拟通知信息接口
Mock.mock(/\/getNotices\//, 'get', (options) => {
    const url = options.url;
    const id = url.split('id=')[1]; // 获取传递的用户ID
    console.log(`获取用户ID为${id}的通知`);
    // 模拟通知数据
    const notices = [
        {
            title: '你收到了 14 份新周报',
            description: '一年前'
        },
        {
            title: '你推荐的 曲妮妮 已通过第三轮面试',
            description: '一年前'
        },
        {
            title: '这种模板可以区分多种通知类型',
            description: '一年前'
        }
    ];

    // 随机生成新通知数量
    const newNum = Mock.Random.integer(0, 10);

    return {
        code: 0,
        data: {
        notices: notices,
        newNum: newNum,
        }
    };
});
