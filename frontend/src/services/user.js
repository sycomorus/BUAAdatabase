import { LOGIN, REGISTER, ROUTES, ACTIVITIES, SEND_POST, SAVE_POST, GET_SAVED_POST} from '@/services/api'
import { request, METHOD, removeAuthorization } from '@/utils/request'

/**
 * 登录服务
 * @param name 账户名
 * @param password 账户密码
 * @returns {Promise<AxiosResponse<T>>}
 */
export async function login(name, password) {
  return request(LOGIN, METHOD.POST, {
    name: name,
    password: password
  })
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
    role: role
  })
}

/*
  * 获取用户动态
  * @param userToken 用户token
  * @returns {Promise<AxiosResponse<T>>}
  */
export async function getActivities() {
  return request(ACTIVITIES, METHOD.GET)
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
export async function sendPost(id, title, startDate, endDate, subjects, location, fullLocation, telephoneNumber, emailAddress, content) {
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
      content: content
    }
  })
}

export async function savePost(id, title, startDate, endDate, subjects, location, fullLocation, telephoneNumber, emailAddress, content) {
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
      content: content
    }
  })
}

export async function getSavedPost(id) {
  return request(`${GET_SAVED_POST}?id=${id}`, METHOD.GET);
}



export async function getRoutesConfig() {
  return request(ROUTES, METHOD.GET)
}

/**
 * 退出登录
 */
export function logout() {
  localStorage.removeItem(process.env.VUE_APP_ROUTES_KEY)
  localStorage.removeItem(process.env.VUE_APP_PERMISSIONS_KEY)
  localStorage.removeItem(process.env.VUE_APP_ROLES_KEY)
  removeAuthorization()
}
export default {
  login,
  logout,
  getRoutesConfig
}
