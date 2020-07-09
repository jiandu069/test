# 引用数据
from lemon_69.R_W_excel import read_data
from lemon_69.http_request import http_request
# 执行文件
# 获取到所有的测试数据
all_case=read_data('test_data.xlsx','recharge')
# print('获取所有的测试数据是：',all_case)
# 执行测试
test_data=all_case[0]#先执行第一条用例
print('第一条用例的数据：',all_case[0])
login_case_data=all_case[0]
ip='http://120.78.128.25:8766'
login_response=http_request(ip+login_case_data[4],eval(login_case_data[5]),token=None,method=login_case_data[3])
for i in range(1,len(all_case)):
    test_data=all_case[i]
    token =login_response['data']['token_info']['token']
    response=http_request(ip+test_data[4],eval(test_data[5]),token='Bearer '+token,method=test_data[3])
    excepted = eval(test_data[6])#期望值
    print('最后的结果值是：',response)