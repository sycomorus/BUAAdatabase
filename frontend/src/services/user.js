import {
  LOGIN,
  REGISTER,
  ROUTES,
  ACTIVITIES,
  SEND_POST,
  SAVE_POST,
  GET_SAVED_POST,
  GET_POSTS,
  GET_STUDENT_INFO,
  UPDATE_STUDENT_INFO,
  GET_TEACHER_INFO,
  UPDATE_TEACHER_INFO,
  GET_POST,
  AGREE_POST_REQUEST,
  GET_USER_POSTS,
  DELETE_POST,
} from "@/services/api";
import { request, METHOD, removeAuthorization } from "@/utils/request";

/**
 * 登录服务
 * @param name 账户名
 * @param password 账户密码
 * @returns {Promise<AxiosResponse<T>>}
 */
export async function login(name, password) {
  return request(LOGIN, METHOD.POST, {
    name: name,
    password: password,
  });
}

/**
 * 注册服务
 * @param name 账户名
 * @param password 账户密码
 * @param role 账户角色
 * @returns {Promise<AxiosResponse<T>>}
 */
export async function register(name, password, role) {
  return request(REGISTER, METHOD.POST, {
    name: name,
    password: password,
    role: role,
  });
}

/*
 * 获取用户动态
 * @param userToken 用户token
 * @returns {Promise<AxiosResponse<T>>}
 */
export async function getActivities() {
  return request(ACTIVITIES, METHOD.GET);
}

/**
 * 发布帖子
 * @param id 用户id
 * @param title 标题
 * @param startDate 开始日期
 * @param endDate 结束日期
 * @param subjects 科目
 * @param location 地点
 * @param fullLocation 详细地址
 * @param telephoneNumber 联系电话
 * @param emailAddress 邮箱
 * @param content 内容
 * @returns {Promise<AxiosResponse<T>>}
 */
export async function sendPost(
  id,
  title,
  startDate,
  endDate,
  subjects,
  location,
  fullLocation,
  telephoneNumber,
  emailAddress,
  content
) {
  return request(SEND_POST, METHOD.POST, {
    id: id,
    data: {
      title: title,
      startDate: startDate,
      endDate: endDate,
      subjects: subjects,
      location: location,
      fullLocation: fullLocation,
      telephoneNumber: telephoneNumber,
      emailAddress: emailAddress,
      content: content,
    },
  });
}

/**
 * 保存帖子
 * @param id 用户id
 * @param title 标题
 * @param startDate 开始日期
 * @param endDate 结束日期
 * @param subjects 科目
 * @param location 地点
 * @param fullLocation 详细地址
 * @param telephoneNumber 联系电话
 * @param emailAddress 邮箱
 * @param content 内容
 * @returns {Promise<AxiosResponse<T>>}
 */
export async function savePost(
  id,
  title,
  startDate,
  endDate,
  subjects,
  location,
  fullLocation,
  telephoneNumber,
  emailAddress,
  content
) {
  return request(SAVE_POST, METHOD.POST, {
    id: id,
    data: {
      title: title,
      startDate: startDate,
      endDate: endDate,
      subjects: subjects,
      location: location,
      fullLocation: fullLocation,
      telephoneNumber: telephoneNumber,
      emailAddress: emailAddress,
      content: content,
    },
  });
}

/**
 * 获取保存的帖子
 * @param id 用户id
 * @returns {Promise<AxiosResponse<T>>}
 */
export async function getSavedPost(id) {
  return request(`${GET_SAVED_POST}?id=${id}`, METHOD.GET);
}


/*
  * 获取帖子
  * @param id 用户id
  * @param page 页码
  * @param query 查询
  * @returns {Promise<AxiosResponse<T>>}
*/
export async function getPosts(id, page, query) {
  return request(`${GET_POSTS}?id=${id}&page=${page}&query=${query}`, METHOD.GET);
}


/*
  * 获取帖子
  * @param id 帖子id
  * @returns {Promise<AxiosResponse<T>>} 
*/
export async function getPost(id) {
  return request(`${GET_POST}?id=${id}`, METHOD.GET);
}


/**
 * 获取学生信息
 * @param id 学生id
 * @returns {Promise<AxiosResponse<T>>}
 */
export async function getStudentInfo(id) {
  return request(`${GET_STUDENT_INFO}?id=${id}`, METHOD.GET);
}


/*
  * 获取老师信息
  * @param id 老师id
  * @returns {Promise<AxiosResponse<T>>}
*/
export async function getTeacherInfo(id) {
  return request(`${GET_TEACHER_INFO}?id=${id}`, METHOD.GET);
}

/**
 * 更新学生信息
 * @param id 学生id
 * @param data 学生信息
 * @returns {Promise<AxiosResponse<T>>}
 */
export async function updateStudentInfo(id, data) {
  return request(UPDATE_STUDENT_INFO, METHOD.POST, {
    id: id,
    data: data,
  })
}

/*
  * 更新老师信息
  * @param id 老师id
  * @param data 老师信息
  * @returns {Promise<AxiosResponse<T>>}
  */
export async function updateTeacherInfo(id, data) {
  return request(UPDATE_TEACHER_INFO, METHOD.POST, {
    id: id,
    data: data,
  })
}


/*
  * 同意帖子请求
  * @param id 用户id
  * @param postId 帖子id
  * @returns {Promise<AxiosResponse<T>>}
*/
export async function agreePostRequest(id, postId) {
  return request(AGREE_POST_REQUEST, METHOD.POST, {
    id: id,
    postId: postId,
  });
}


/*
  * 获取用户发的所有帖子
  * @param id 用户id
  * @returns {Promise<AxiosResponse<T>>}
*/
export async function getUserPosts(id) {
  return request(`${GET_USER_POSTS}?id=${id}`, METHOD.GET);
}

/*
  * 删除帖子
  * @param postId 帖子id
  * @returns {Promise<AxiosResponse<T>>}
*/
export async function deletePost(postId) {
  return request(DELETE_POST, METHOD.POST, {
    postId: postId,
  });
}

export async function getRoutesConfig() {
  return request(ROUTES, METHOD.GET);
}

/**
 * 退出登录
 */
export function logout() {
  localStorage.removeItem(process.env.VUE_APP_ROUTES_KEY);
  localStorage.removeItem(process.env.VUE_APP_PERMISSIONS_KEY);
  localStorage.removeItem(process.env.VUE_APP_ROLES_KEY);
  removeAuthorization();
}
export default {
  login,
  logout,
  getRoutesConfig,
};
