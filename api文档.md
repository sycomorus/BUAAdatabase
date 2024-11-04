# api设计文档

## 登录注册相关

### login

**类型**：POST

**参数**：

```json
{
  "username": "",
	"passage": ""
}
```

**返回**：

```json
{
  "code": 0,   // 0表示登录成功，-1表示登录失败
  "data": {
    "roles": [{"id": "admin"}],  // id表示用户的身份，可选admin,student,teacher
    "token": "Authorization:0.123456789",   // 用于后续与后端进行数据交流，随机数即可
    "id" : "123456789" // 用户id
  },
}
```



### register

**类型**：POST

**参数**：

```json
{
	"username": "",
	"passage": "",
	"role": "" // 可选student或者teacher
}
```

**返回**：

```json
{
  "code": 0,   // 0表示注册成功，-1表示注册失败
  "data": {
    "roles": [{"id": "admin"}],  // id表示用户的身份，可选admin,student,teacher
    "token": "Authorization:0.123456789",   // 用于后续与后端进行数据交流，随机数即可
    "id" : "123456789" // 用户id
  },
}
```

## 发帖相关

### sendPost

**类型**：POST

**参数**

```json
{
    "id": "",    // 用户独有的标识符id
    "data": {
      "title": "",  // 文章标题
      "startDate": "",  // 开始日期，注意格式为YYYY-MM-DD 
      "endDate": "",    // 结束日期，注意格式为YYYY-MM-DD
      "subjects":[],    // 已选科目，格式为['数学','英语'，'语文']
      "location": [],   // 地址，格式如['湖南省','衡阳市','雁峰区']，总之是包含三级行政规划的列表
      "fullLocation": "",  // 详细地址
      "telephoneNumber": "",  // 电话号码
      "emailAddress": "",   // 电子邮箱地址
      "content": ""      // 帖子内容
    }
}
```

**返回**

```json
{
	"code": 0   // 0成功，-1表示失败
}
```

### savePost

**类型**：POST

**参数**

```json
{
    "id": "",    // 用户独有的标识符id
    "data": {
      "title": "",  // 文章标题
      "startDate": "",  // 开始日期，注意格式为YYYY-MM-DD 
      "endDate": "",    // 结束日期，注意格式为YYYY-MM-DD
      "subjects":[],    // 已选科目，格式为['数学','英语'，'语文']
      "location": [],   // 地址，格式如['湖南省','衡阳市','雁峰区']，总之是包含三级行政规划的列表
      "fullLocation": "",  // 详细地址
      "telephoneNumber": "",  // 电话号码
      "emailAddress": "",   // 电子邮箱地址
      "content": ""      // 帖子内容
    }
}
```

**返回**

```json
{
	"code": 0   // 0成功，-1表示失败
}
```

### getSavedPost

**类型**：GET

**参数**：

```json
"id": 1  // 用户独有的标识符id
```

注意，GET类型的参数直接从url获取，比如这个为``${GET_SAVED_POST}?id=${id}``

**返回**：

```json
{
    "code": 0,     // 0成功，-1表示失败
    "data": {
      "title": "",  // 文章标题
      "startDate": "",  // 开始日期，注意格式为YYYY-MM-DD 
      "endDate": "",    // 结束日期，注意格式为YYYY-MM-DD
      "subjects":[],    // 已选科目，格式为['数学','英语'，'语文']
      "location": [],   // 地址，格式如['湖南省','衡阳市','雁峰区']，总之是包含三级行政规划的列表
      "fullLocation": "",  // 详细地址
      "telephoneNumber": "",  // 电话号码
      "emailAddress": "",   // 电子邮箱地址
      "content": ""      // 帖子内容
    }
}
```



## 广场相关

### getPosts

**类型**：GET

**参数**：

```json
"id": "" //用户id
"page": "" // 页面编号，这里我规定，每页只展示十个帖子
"query": "" //查询内容，若为空则代表查询全部
```

注意，GET类型的参数直接从url获取，比如这个为``${GET_POSTS}?id=${id}&page=${page}&query=${query}``

**返回**：

```json
{
    "posts": [{         // 一个帖子的列表
        "id": "",       // 帖子id
        "title": ""     // 帖子标题
        "tags": [""],     // 帖子的tags
        "content": "",  // 帖子内容
        "author": "",   // 帖子作者
        "authorId": int, // 帖子作者id
        "date": "",     // 帖子发布日期（如果在二十四内则显示“几小时前”， 此外如果在三天内则显示“几天前， 此外显示日期”）
        "location": ""   // 简略地址即可
    }]
    "total": int        // 总共的帖子数，不是单次返回的帖子数，注意是int
}
```

### getPost

**类型**：GET

**参数**：

```json
"id": ""   // 帖子的独有标识符
```

**返回**

```json
{
	"code": 0   // 0表示成功，-1表示失败
    "data": {
		"title": "" // 帖子的标题
    	"author": "" // 帖子的作者
    	"location": [""] // 简略地址，格式如["湖南省", "衡阳市", "雁峰区"]
		"startDate": "" // yyyy-mm-dd
		"endDate": "" // yyyy-mm-dd
    	"fullLocation": "" // 详细地址
		"telephoneNumber": "" // 联系电话
		"emailAddress": "" // 电子邮箱
		"subjects": [""] // 科目，格式如["语文", "数学", "英语"]
		"content": "" // 文章的内容
    }
}
```

### agreePostRequest

**描述**：用户接受帖子

**类型**：POST

**参数**：

```json
{
	"id": ""   // 接受的用户的id
	"postId":""   // 用户接受的帖子id
}
```

**返回**

```json
{
	"code": 0 // 0表示成功，-1表示失败
}
```



## 用户主页相关

### getStudentInfo

**类型**：GET

**参数**：

```json
"id": ""   // 目标用户的id
```

**返回**

```json
{
    "code": 0  // 0表示成功，-1表示失败
    "data": {
    	"name": "" // 用户名
    	"email": "" // 电子邮箱地址
    	"telephone": "" //电话号码
    	"address": "" // 地址
    	"personalSignature": "" // 个性签名
    	"intro": "" // 简介
    	"age": int // 年龄
    	"gender": "" // 性别，可选男或女（没有武装直升机！！！）
    	"grade": "" //年级
    }
}
```

### updateStudentInfo

**类型**：POST

**参数**：

```json
{
    "id": "" // 目标学生id
    "data": {
    	"grade": ""   // 年级
        "gender": ""  // 性别
        "age": int    // 年龄
        "email": ""   // 电子邮箱地址
        "telephone": "",  // 电话
        "address": "",  // 地址
        "intro": "",  // 简介
        "personalSignature": "",  // 个性签名
	}
}
```

**返回**：

```json
{
	"code": 0  // 0表示成功，-1表示失败
}
```

### getTeacherInfo

**类型**：GET

**参数**：

```json
"id": ""  // 目标家教的id
```

**返回**：

```json
{
    "code": 0  // 0表示成功，-1表示失败
    "data": {
		"name": "" // 教师姓名
    	"email": "" // 电子邮箱地址
    	"telephone": "" // 电话
    	"address": "" // 地址，简略地址即可
    	"personalSignature": "" // 个性签名
		"intro": "" // 自我介绍
    	"gender": "" // 性别，可选男女
    	"age": int // 年龄
    	"degree": "" // 学历
    	"rate": float // 评分
    	"rateNum": int // 评分人数
    	"comments":[{ // 一个包含评论信息的列表
				"id": "" // 评论id
    			"authorName": "" // 评论作者
    			"rating": "" // 评分
    			"content": "" // 评论内容
    			"date": "" // 日期
            }]
    }
}
```

### updateTeacherInfo

**类型**：POST

**参数**：

```json
{
	"id": "" // 目标家教id
    "data": {
		"dagree": ""  // 学历
    	"gender": ""  // 性别
    	"age": int // 年龄
    	"email": "", // 电子邮箱地址
        "telephone": "",  // 电话
        "address": "",  // 地址
        "intro": "", // 简介
        "signature": "",  // 个性签名
    }
}
```

**返回**：

```json
{
	"code": 0 // 0表示成功，-1表示失败
}
```

## 个人工作相关

### getUserPosts

**描述**：获取一个用户发过的所有帖子

**类型**：GET

**参数**：

```json
"id": ""  // 用户id
```

**返回**

```json
{
	"code": 0 // 0表示成功，-1表示失败
	"posts": [{ // 一个包含字典的列表
		"id": "" // 帖子id
    	"title": "" // 帖子标题
    	"content": "" //帖子内容
	}]
}
```

### deletePost

**描述**：在数据库中删除帖子

**类型**：POST

**参数**：

```json
{
	"postId": ""
}
```

**返回**：

```json
{
	"code": 0  // 0表示成功，-1表示失败
}
```

### getStudents

**描述**：获取一个家教的所有学生信息

**类型**：GET

**参数**：

```json
"id": "" //家教的id
```

**返回**：

```json
{
	"code": 0  // 0表示成功，-1表示失败
    "students": [{  // 一个包含学生信息的列表
        "id": ""  // 学生id
        "name": "" // 学生姓名
    }]
}
```

### getTeachers

**描述**：获取一个学生的所有家教信息

**类型**：GET

**参数**：

```json
"id": ""  // 学生的id
```

**返回**：

```json
{
	"code": 0 // 0表示成功， -1表示失败
	"teachers": [{
		"id": "" // 家教的id
		"name": '' // 家教的昵称
	}]
}
```

### submitComment

**描述**：学生对家教发表评论

**类型**：POST

**参数**

```json
{
	"studentId": "" // 学生id
	"studentName": "" // 学生名字
	"teacherId": "" // 家教id
	"rate": float // 评分
	"comment": "" // 评论内容
}
```

**返回**

```json
{
	"code": 0
}
```

### submitLearningMaterial

**描述**：家教上传学习资料

**类型**：POST

**参数**：

```json
{
	"teacherId": "" // 家教id
    "teacherName": "" // 家教名
	"studentId": "" // 学生id
	"filename": "" // 文件名
	"downloadLink": "" // 下载链接
}
```

**返回**：

```json
{
	"code": 0
}
```

### getLearningMaterials

**描述**：学生获取学习资料

**类型**：GET

**参数**：

```json
"id": "" // 学生id
```

**返回**：

```json
{
	"code": 0
	"materials": [{
        "id": "",   // 学习资料id
        "filename": "", // 学习资料名称
        "publisher": "", // 发布者名称
        "downloadLink": "", // 链接
        "date": "", // 发布日期
	}]
}
```



### getTodos

**描述**：获取待办事项

**类型**：GET

**参数**：

```json
{
	"id": ""   // 用户id
}
```

**返回**：

```json
{
	"code": 0
	"todos": [{   // 一个包含todo信息的列表
        "id": ""  // todo的唯一标识符
        "postId": "" // todo的来源帖子的id
        'accepterName': "" // 来源帖的接受者姓名
        "accepterId": "" //  来源贴的接收者id
    }]	
}
```



## 师生关系相关

### link

**描述**：正式建立师生关系

**类型**：POST

**参数**：

```json
{
	"teacherId": "" // 家教id
	"studentId": "" // 学生id
}
```

**返回**：

```json
{
	"code": 0  // 0表示成功，-1表示失败
}
```

### unlink

**描述**：解除师生关系

**类型**：POST

**参数**：

```json
{
	"teacherId": "" // 家教id
	"studentId": "" // 学生id
}
```

**返回**：

```json
{
	"code": 0
}
```

### refuseLink

**描述**：拒绝某个用户尝试建立师生关系的请求

**类型**：POST

**参数**：

```json
{
	"teacherId": "" // 家教id
	"studentId": "" // 学生id
}
```

**返回**：

```json
{
	"code": 0 
}
```

## 通知相关

### getNotices

**描述**：用于管理页面右上角的通知图标

**类型**：GET

**参数**：

```json
"id": "" // 收到通知的用户id
```

**返回**

```json
{
	"code": 0
	"data": {
		"notices": [{  // 包含通知信息的列表
			"title": "",   // 通知的主要内容
			"description": ""  // 通知的时间
		}]
		"newNum": int   // 新通知的个数
	}
}
```

## 管理员相关

### getUserRole

**描述**：用于获取发帖人的身份

**类型**：GET

**参数**：

```json
"postId": ""//帖子的id
```

**返回**

```json
{
	"code": 0 // 0表示成功，-1表示失败
	"data": { 
		"userRole": "" //“家教”或“学生”
	}
}
```

## approvePost

**描述**：用于通过待审核的帖子

**类型**：POST

**参数**：

```json
{
	"postId": ""
}
```

**返回**

```json
{
	"code": 0  // 0表示成功，-1表示失败
}
```

## rejectPost

**描述**：用于驳回待审核的帖子

**类型**：POST

**参数**：

```json
{
	"postId": ""
}
```

**返回**：

```json
{
	"code": 0  // 0表示成功，-1表示失败
}
```

