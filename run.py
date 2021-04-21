# @Time ： 2021/4/19 21:01
# @Auth ： tudou
# @File ：run.py
# @QQ ：121313927
# @Company：湖南省零檬信息技术有限公司

from Python_0414.lesson07 import read_data,api_fun,wirte_result

# 接口测试实战，封装成函数
def execute_fun(filename,sheetname):
    cases = read_data(filename,sheetname)
    # print(cases)
    for case in cases:   # 依次去访问cases中的元素，保存到定义的变量case中
        # print(case)
        case_id = case['case_id']
        url = case['url']   #
        data = eval(case['data'])
        # print(case_id,url,data)


        # 获取期望结果code、msg
        expect = eval(case['expect'])
        expect_code = expect['code']
        expect_msg = expect['msg']
        print('预期结果code为：{}，msg为：{}'.format(expect_code,expect_msg))

        # 执行接口测试
        real_result = api_fun(url=url,data=data)
        # print(real_result)
        # 获取实际结果code、msg
        real_code = real_result['code']
        real_msg = real_result['msg']
        print('实际结果code为：{}，msg为：{}'.format(real_code,real_msg))

        #断言：预期vs实际结果
        if real_code == expect_code and real_msg == expect_msg:
            print('这{}条测试用例执行通过！'.format(case_id))
            final_re = 'Passed'
        else:
            print('这{}条测试用例执行不通过！'.format(case_id))
            final_re = 'Failed'
        print('*'*50)

        # 写入最终的测试结果到excel中
        wirte_result(filename,sheetname,case_id+1,8,final_re)


# 调用函数
execute_fun('D:\\Program Files\\.jenkins\\workspace\\scb20\\test_data\\test_case_api.xlsx','register')
# execute_fun('D:\\Pycharm_workspace\\SCB20\\test_data\\test_case_api.xlsx','login')

