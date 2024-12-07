import Mock from "mockjs";

Mock.mock(`${process.env.VUE_APP_API_BASE_URL}/uploadAvatar/`, "post", ({ body }) => {
    let result = { data: {} };
    const { id, avatar } = JSON.parse(body);
    console.log(id, avatar);
    
    result.code = 0;
    result.message = "上传成功";
    return result;
})