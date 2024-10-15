// mock.js
import Mock from 'mockjs'

// 模拟发送表单数据的接口
Mock.mock(`${process.env.VUE_APP_API_BASE_URL}/savePost`, 'post', (options) => {
  const {id, data} = JSON.parse(options.body);
  const {title, startDate, endDate, subjects, location, fullLocation, teltphoneNumber, emailAddress, content} = data;

  // 打印收到的参数，便于调试
  console.log('收到的请求数据:', {
    id, title, startDate, endDate, subjects, location, fullLocation, teltphoneNumber, emailAddress, content
  });

  // 模拟响应
  return Mock.mock({
    code: 0, // 成功状态码
    message: '发布成功',
    data: {
      id: id, // 模拟生成唯一 ID
      title: title,
      startDate: startDate,
      endDate: endDate,
      subjects: subjects,
      location: location,
      fullLocation: fullLocation,
      teltphoneNumber: teltphoneNumber,
      emailAddress: emailAddress,
      content: content
    }
  });
});
