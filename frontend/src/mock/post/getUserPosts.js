// mock/user.js
import Mock from 'mockjs';

const posts = Mock.mock({
    'posts|10': [
        {
            id: 1,
            title: 'this is a title',
            content: 'this is a content asdnoadnowqndoqdnqodnqodnwqdinqwidnqwdwqndonwqiodnwqodwqidnwqodniqconiondsovndsovnsiovnsvsdvd',
        }
    ],
});

// 模拟 getUserPosts 的接口返回
Mock.mock(/\/getUserPosts\//, 'get', (options) => {
    // 解析 URL 获取查询参数
    const url = new URL(options.url, window.location.origin);
    const id = url.searchParams.get('id');
    console.log(`模拟获取用户ID为${id}的帖子`);

    return {
        code: 0, // 模拟成功返回
        posts: posts.posts
    };
});