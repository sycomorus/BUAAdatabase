import {LOGIN, REGISTER, ROUTES, ACTIVITIES} from '@/services/api'
import {request, METHOD, removeAuthorization} from '@/utils/request'

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
export async function getActivities(token) {
  return request(ACTIVITIES, METHOD.GET, token)
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
