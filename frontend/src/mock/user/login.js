import Mock from "mockjs";
import "@/mock/extend";

Mock.mock(`${process.env.VUE_APP_API_BASE_URL}/login/`, "post", ({ body }) => {
  let result = { data: {} };
  const { name, password } = JSON.parse(body);

  let success = false;

  if (name === "admin" && password === "888888") {
    success = true;
    result.data.roles = [{ id: "admin" }];
    result.data.id = "0";
  } else if (name === "teacher" && password === "888888") {
    success = true;
    result.data.roles = [{ id: "teacher" }];
    result.data.id = "1";
  } else if (name == "student" && password == "888888") {
    success = true;
    result.data.roles = [{ id: "student" }];
    result.data.id = "2";
  } else {
    success = false;
  }

  if (success) {
    result.code = 0;
    result.data.token = "Authorization:" + Math.random();
    result.message = "登录成功";
  } else {
    result.code = -1;
    result.message = "账户名或密码错误（admin/888888 or test/888888）";
  }
  return result;
});
