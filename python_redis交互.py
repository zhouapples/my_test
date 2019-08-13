from redis import *


# 1.创建对象

if __name__ == '__main__':


# 设置string
    def setting():
        try:
            sr = StrictRedis()
            result = sr.set('name','itheima')
            # 输出响应结果,成功返回true,否则false
            print(result)
        except Exception as e:
            print(e)



# 获取string
    def get_str():
        try:
            sr = StrictRedis()
            result = sr.get('name')
            # 输出响应结果,成功返回true,否则false
            # 输出的是二进制数据
            print(result)
        except Exception as e:
            print(e)


        # 修改string
    def modify():
        try:
            sr = StrictRedis()
            result = sr.set('name','zhouapples')
            # 输出响应结果,成功返回true,否则false
            print(result)
        except Exception as e:
                print(e)



    def delete():
        try:
            sr = StrictRedis()
            result = sr.delete('name')
            # 输出响应结果,成功返回true,否则false
            print(result)
        except Exception as e:
                print(e)



    def show():
        try:
            sr = StrictRedis()
            result = sr.keys()
            # 输出响应结果,成功返回true,否则false
            print(result)
        except Exception as e:
                print(e)



