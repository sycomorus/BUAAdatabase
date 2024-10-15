# api设计文档

## 登录注册相关

### login

**类型**：POST

**参数**：

```json
{
    "username": str
	"passage": str
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
	"username": str
	"passage": str
	"role": student // 可选student或者teacher
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
    'id': '',    // 用户独有的标识符id
    'data': {
      'title': '',  // 文章标题
      'startDate': '',  // 开始日期，注意格式为YYYY-MM-DD 
      'endDate': '',    // 结束日期，注意格式为YYYY-MM-DD
      'subjects':[],    // 已选科目
      'location': [],   // 地址，格式如['湖南省','衡阳市','雁峰区']，总之是包含三级行政规划的列表
      'fullLocation': ''  // 详细地址
      'teltphoneNumber': '',  // 电话号码
      'emailAddress': '',   // 电子邮箱地址
      'content': ''      // 帖子内容
    }
}
```

**返回**

```json
{
	'code': 0   // 0成功，-1表示失败
}
```

### savePost

**类型**：POST

**参数**

```json
{
    'id': '',    // 用户独有的标识符id
    'data': {
      'title': '',  // 文章标题
      'startDate': '',  // 开始日期，注意格式为YYYY-MM-DD 
      'endDate': '',    // 结束日期，注意格式为YYYY-MM-DD
      'subjects':[],    // 已选科目
      'location': [],   // 地址，格式如['湖南省','衡阳市','雁峰区']，总之是包含三级行政规划的列表
      'fullLocation': ''  // 详细地址
      'teltphoneNumber': '',  // 电话号码
      'emailAddress': '',   // 电子邮箱地址
      'content': ''      // 帖子内容
    }
}
```

**返回**

```json
{
	'code': 0   // 0成功，-1表示失败
}
```

### getSavedPost

**类型**：GET

**参数**：

```json
{
	'id': 1  // 用户独有的标识符id
}
```

**返回**：

```json
{
    'code': 0     // 0成功，-1表示失败
    'data': {
        'title': '',  // 文章标题
        'startDate': '',  // 开始日期，注意格式为YYYY-MM-DD 
        'endDate': '',    // 结束日期，注意格式为YYYY-MM-DD
        'subjects':[],    // 已选科目
        'location': [],   // 地址，格式如['湖南省','衡阳市','雁峰区']，总之是包含三级行政规划的列表
        'fullLocation': ''  // 详细地址
        'teltphoneNumber': '',  // 电话号码
        'emailAddress': '',   // 电子邮箱地址
        'content': ''      // 帖子内容
	}
}
```



