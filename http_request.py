import requests
#题1 注册+登录
# 访问前程贷接口
def http_request(url,data,token=None,method='post'):
    header = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Authorization': token}
    if method=='get':
        result=requests.get(url,json=data,headers=header)#返回的结果
    else:
        result = requests.post(url, json=data, headers=header)  # 返回的结果
    # print(result.json())
    return result.json()#return返回指定的结果
if __name__ == '__main__':
    # 注册数据
    reg_url = 'http://120.78.128.25:8766/futureloan/member/register'
    reg_data = {'mobile_phone': 13488889999, 'pwd': 'lemon666', 'type': 0, 'reg_name': '监督'}  # 请求体
    http_request(reg_url,reg_data)
    # 登录数据
    log_url = 'http://120.78.128.25:8766/futureloan/member/login'
    log_data = {'mobile_phone': 13488889999, 'pwd': 'lemon666'}  # 请求体
    response=http_request(log_url,log_data)

    # 充值数据
    token=response['data']['token_info']['token']
    rec_url='http://120.78.128.25:8766/futureloan/member/recharge'
    rec_data={'member_id':205805,'amount':30000}
    http_request(rec_url,rec_data,'Bearer '+token)
    # 提现数据
    wit_url='http://120.78.128.25:8766/futureloan/member/withdraw'
    wit_data={'member_id':205805,'amount':1}
    http_request(wit_url,wit_data,'Bearer '+token)