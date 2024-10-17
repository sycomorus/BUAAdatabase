import Mock from 'mockjs';

// 模拟返回的帖子数据
const postsData = Mock.mock({
    'posts|100': [
        {
            'id|+1': 1,  // 帖子ID，自增
            title: '123',  // 随机生成的帖子标题
            content: '撒大大',  // 随机生成的帖子内容
            tags: ['数学', "语文"],  // 随机生成的标签数组，1-3 个标签
            author: 'mysterious_name',  // 随机生成的作者名
            authorId: 1,
            date: "2024-08-19",  // 随机生成的日期
            location: '北京海淀'  // 随机生成的城市地址
        }
    ],
    total: 100  // 假设总共有50条帖子
});

const postsData2 = Mock.mock({
    'posts|100': [
        {
            'id|+1': 1,  // 帖子ID，自增
            title: '456',  // 随机生成的帖子标题
            content: '撒大大',  // 随机生成的帖子内容
            tags: ['数学', "语文"],  // 随机生成的标签数组，1-3 个标签
            author: 'mysterious_name',  // 随机生成的作者名
            authorId: 1,
            date: "2024-08-19",  // 随机生成的日期
            location: '北京海淀'  // 随机生成的城市地址
        }
    ],
    total: 100  // 假设总共有50条帖子
});

// 模拟 getPosts 的接口返回
Mock.mock(/\/getPosts\//, 'get', (options) => {
    const urlParams = new URLSearchParams(options.url.split('?')[1]);
    const page = urlParams.get('page') || 1;
    const id = urlParams.get('id') || 'unknown';
    const query = urlParams.get('query') || '';

    console.log(`模拟获取用户ID为${id}的帖子, 页码: ${page}, 查询内容: ${query}`);

    // 简单模拟分页，每页显示10条帖子
    const pageSize = 10;
    const start = (page - 1) * pageSize;
    const end = start + pageSize;
    const paginatedPosts = postsData.posts.slice(start, end);
    const paginatedPosts2 = postsData2.posts.slice(start, end);
    console.log("帖子内容", paginatedPosts);
    console.log("帖子数目", postsData.total);

    return {
        posts: query == ''? paginatedPosts : paginatedPosts2,
        total: postsData.total
    };
});
