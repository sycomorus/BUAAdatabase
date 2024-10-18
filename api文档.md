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
    	"fullLocation": "" // 详细地址
		"telephoneNumber": "" // 联系电话
		"emailAddress": "" // 电子邮箱
		"subjects": [""] // 科目，格式如["语文", "数学", "英语"]
		"content": "" // 文章的内容
    }
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
后续可能要增加家教评分，家教评论等系统，暂时不确定返回值
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

