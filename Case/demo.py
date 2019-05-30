from Base.get_data import GetFileData


def get_login_data():
    """定义一个读取数据的方法"""

    success_data_list = []  # 预期成功的数据列表
    fail_data_list = []  # 预期失败的数据列表
    login_data = GetFileData().get_file_data("login_data.yml")
    for i in login_data:
        if login_data.get(i).get("toast"):
            fail_data_list.append((i, login_data.get(i).get("account"),
                                   login_data.get(i).get("passwd"),
                                   login_data.get(i).get("toast"),
                                   login_data.get(i).get("expect_data")))
        else:
            success_data_list.append((i, login_data.get(i).get("account"), login_data.get(i).get("passwd")
                                     , login_data.get(i).get("expect_data")))
    return {"success": success_data_list, "fail": fail_data_list}


class Test01(object):
    def test01(self):
        print("test01")
        print(get_login_data())

