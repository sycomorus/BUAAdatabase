import Mock from 'mockjs';

// 模拟通知信息接口
Mock.mock(/\/getAvatar\//, 'get', (options) => {
    const url = options.url;
    const id = url.split('id=')[1]; // 获取传递的用户ID
    console.log(`获取用户ID为${id}的头像`);
    // 模拟头像数据
    const avatar = "http://120.46.1.4:9000/zxb/png/Akkarin.png";

    return {
        code: 0,
        avatar: avatar,
    }
});
