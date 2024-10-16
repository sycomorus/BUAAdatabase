//跨域代理前缀
// const API_PROXY_PREFIX='/api'
// const BASE_URL = process.env.NODE_ENV === 'production' ? process.env.VUE_APP_API_BASE_URL : API_PROXY_PREFIX
const BASE_URL = process.env.VUE_APP_API_BASE_URL;
module.exports = {
  LOGIN: `${BASE_URL}/login/`,
  ROUTES: `${BASE_URL}/routes/`,
  REGISTER: `${BASE_URL}/register/`,
  ACTIVITIES: `${BASE_URL}/activities/`,
  SEND_POST: `${BASE_URL}/sendPost/`,
  SAVE_POST: `${BASE_URL}/savePost/`,
  GET_SAVED_POST: `${BASE_URL}/getSavedPost/`,
  GET_POSTS: `${BASE_URL}/getPosts/`,
  GET_STUDENT_INFO: `${BASE_URL}/getStudentInfo/`,
  UPDATE_STUDENT_INFO: `${BASE_URL}/updateStudentInfo/`,
  GET_TEACHER_INFO: `${BASE_URL}/getTeacherInfo/`,
  UPDATE_TEACHER_INFO: `${BASE_URL}/updateTeacherInfo/`,
  GET_POST: `${BASE_URL}/getPost/`,
  AGREE_POST_REQUEST: `${BASE_URL}/agreePostRequest/`,
};
