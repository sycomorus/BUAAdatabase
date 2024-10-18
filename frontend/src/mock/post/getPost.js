import Mock from "mockjs";
import "@/mock/extend"; // 根据实际项目路径调整这个引入

// 模拟帖子数据
Mock.mock(/\/getPost\//, "get", (options) => {
    const url = new URL(options.url, window.location.origin);
    const postId = url.searchParams.get('id');

    const posts = {
        "1": {
            author: "张三",
            title: "数学辅导",
            startDate: "2024-01-10",
            endDate: "2024-01-20",
            subjects: ["数学", "物理"],
            location: ["湖南省", "长沙市", "岳麓区"],
            fullLocation: "湖南省长沙市岳麓区大学城",
            telephoneNumber: "12345678901",
            emailAddress: "zhangsan@example.com",
            content: "提供数学和物理辅导，欢迎咨询！"
        },
        "2": {
            author: "李四",
            title: "英语学习班",
            startDate: "2024-02-01",
            endDate: "2024-02-10",
            subjects: ["英语"],
            location: ["广东省", "广州市", "天河区"],
            fullLocation: "广东省广州市天河区天汇大厦",
            telephoneNumber: "98765432100",
            emailAddress: "lisi@example.com",
            content: "开设英语口语和写作课程，期待您的加入！"
        }
    };

    const result = { code: 0, data: null };

    if (posts[postId]) {
        result.data = posts[postId];
        result.message = "获取帖子详情成功";
    } else {
        result.code = -1;
        result.message = "帖子不存在";
    }

    return result;
});
