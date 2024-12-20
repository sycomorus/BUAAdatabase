from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import login, register, get_routes_config, sendPost, savePost, getSavedPost,getPosts,getPost,agreePostRequest,updateStudentInfo,getStudentInfo,updateTeacherInfo,getTeacherInfo,getUserPosts,deletePost,link,unlink,refuseLink,getStudents,getTeachers,sendNotice,getNotices,submitComment,submitLearningMaterial,getLearningMaterials,sendTodo,getTodos,getUserRole,approvePost,rejectPost,getAllStudents,getAllTeachers,makeAnnouncement,deleteUser,getAnnouncements,resetPassword,uploadAvatar,getAvatar,getUploadedLearningMaterials

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('sendPost/', sendPost, name='sendPost'),
    path('savePost/', savePost, name='savePost'),
    path('getSavedPost/',getSavedPost,name='getSavedPost'),
    path('getPosts/',getPosts,name="getPosts"),
    path('getPost/',getPost,name="getPost"),
    path('agreePostRequest/',agreePostRequest,name="agreePostRequest"),
    path('routes/', get_routes_config, name='get_routes_config'),
    path('updateStudentInfo/',updateStudentInfo,name="updateStudentInfo"),
    path('getStudentInfo/',getStudentInfo,name="getStudentInfo"),
    path('updateTeacherInfo/',updateTeacherInfo,name="updateTeacherInfo"),
    path('getTeacherInfo/',getTeacherInfo,name="getTeacherInfo"),
    path('getUserPosts/',getUserPosts,name="getUserPosts"),
    path('deletePost/',deletePost,name="deletePost"),
    path('link/',link,name="link"),
    path('unlink/',unlink,name="unlink"),
    path('refuseLink/',refuseLink,name="refuseLink"),
    path('getStudents/',getStudents,name="getStudents"),
    path('getTeachers/',getTeachers,name="getTeachers"),
    path('sendNotice/',sendNotice,name="sendNotice"),
    path('getNotices/',getNotices,name="getNotices"),
    path('submitComment/',submitComment,name="submitComment"),
    path('submitLearningMaterial/',submitLearningMaterial,name="submitLearningMaterial"),
    path('getLearningMaterials/',getLearningMaterials,name="getLearningMaterials"),
    path('sendTodo/',sendTodo,name="sendTodo"),
    path('getTodos/',getTodos,name="getTodos"),
    path('getUserRole/',getUserRole,name="getUserRole"),
    path('approvePost/',approvePost,name="approvePost"),
    path('rejectPost/',rejectPost,name="rejectPost"),
    path('getAllStudents/',getAllStudents,name="getAllStudents"),
    path('getAllTeachers/',getAllTeachers,name="getAllTeachers"),
    path('makeAnnouncement/', makeAnnouncement, name='makeAnnouncement'),
    path('deleteUser/',deleteUser,name="deleteUser"),
    path('getAnnouncements/',getAnnouncements,name="getAnnouncements"),
    path('resetPassword/',resetPassword,name="resetPassword"),
    path('uploadAvatar/',uploadAvatar,name="uploadAvatar"),
    path('getAvatar/',getAvatar,name="getAvatar"),
    path('getUploadedLearningMaterials/',getUploadedLearningMaterials,name="getUploadedLearningMaterials"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)