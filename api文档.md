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
    "token": "Authorization:0.123456789",   // 用户唯一标识id，用于后续与后端进行数据交流
  },
  "message": "登录失败"    // 返回信息，例如登录失败则返回“登录失败”，用户名不存在则返回“用户名不存在”
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
    "token": "Authorization:0.123456789",   // 用户唯一标识id，用于后续与后端进行数据交流
  },
  "message": "注册失败"    // 返回信息
}
```

