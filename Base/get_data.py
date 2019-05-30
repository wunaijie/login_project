import os
import yaml


class GetFileData:
    def __init__(self):
        pass

    def get_file_data(self, name):
        """

        :param name:文件名
        :return: 文件数据
        """
        file_path = os.getcwd() + os.sep + "Data" + os.sep + name
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
