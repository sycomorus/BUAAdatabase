import Mock from "mockjs";
import "@/mock/extend";

Mock.mock(`${process.env.VUE_APP_API_BASE_URL}/updateStudentInfo/`, "post", ({ body }) => {
  let result = { data: {} };
  const { id, data } = JSON.parse(body);
  let success = false;

  // 假设根据 userId 校验更新
  if (id && data) {
    // 可以在这里添加更多逻辑来校验具体的字段
    success = true;
  }

  if (success) {
    result.code = 0; // 成功
  } else {
    result.code = -1; // 失败
  }

  return result;
});