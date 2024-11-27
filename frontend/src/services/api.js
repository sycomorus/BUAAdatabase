//跨域代理前缀
// const API_PROXY_PREFIX='/api'
// const BASE_URL = process.env.NODE_ENV === 'production' ? process.env.VUE_APP_API_BASE_URL : API_PROXY_PREFIX
const BASE_URL = process.env.VUE_APP_API_BASE_URL;
module.exports = {
  LOGIN: `${BASE_URL}/login/`,
  ROUTES: `${BASE_URL}/routes/`,
  REGISTER: `${BASE_URL}/register/`,
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
  GET_USER_POSTS: `${BASE_URL}/getUserPosts/`,
  DELETE_POST: `${BASE_URL}/deletePost/`,
  GET_STUDENTS: `${BASE_URL}/getStudents/`,
  UNLINK: `${BASE_URL}/unlink/`,
  SUBMIT_LEARNING_MATERIAL: `${BASE_URL}/submitLearningMaterial/`,
  GET_TODOS: `${BASE_URL}/getTodos/`,
  LINK: `${BASE_URL}/link/`,
  REFUSE_LINK: `${BASE_URL}/refuseLink/`,
  GET_TEACHERS: `${BASE_URL}/getTeachers/`,
  SUBMIT_COMMENT: `${BASE_URL}/submitComment/`,
  GET_LEARNING_MATERIALS: `${BASE_URL}/getLearningMaterials/`,
  GET_NOTICES: `${BASE_URL}/getNotices/`,
  GET_USER_ROLE: `${BASE_URL}/getUserRole/`,
  APPROVE_POST: `${BASE_URL}/approvePost/`,
  REJECT_POST: `${BASE_URL}/rejectPost/`,
  GET_ALL_TEACHERS: `${BASE_URL}/getAllTeachers/`,
  GET_ALL_STUDENTS: `${BASE_URL}/getAllStudents/`,
  MAKE_ANNOUNCEMENT: `${BASE_URL}/makeAnnouncement/`,
  DELETE_USER: `${BASE_URL}/deleteUser/`,
  GET_ANNOUNCEMENTS: `${BASE_URL}/getAnnouncements/`
};
