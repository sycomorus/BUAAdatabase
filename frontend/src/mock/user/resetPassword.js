import Mock from "mockjs";

Mock.mock(`${process.env.VUE_APP_API_BASE_URL}/resetPassword/`, 'post', (options) => {
    // 打印收到的参数，便于调试

    const { id, oldpassword, password } = JSON.parse(options.body);
    console.log(id, oldpassword, password)
    let message = ""
    let code = 0
    if (oldpassword === "123" && id && password) {
        code = 0
        message = ""
    } else if (oldpassword === '456') {
        code = 1
        message = "旧密码错误"
    }
    return Mock.mock({
        code,
        message
    });
});