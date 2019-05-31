# Encoding: utf-8# Date: 2019/5/30# Name: 仲玲from commen.log_method import Log_Methodfrom commen.http_request import HTTP_Requestfrom commen.read_config import Read_Configfrom commen.excel_util import Excerl_Methodimport unittestclass Register_Method(unittest.TestCase):	@classmethod	def setUpClass(cls):		cls.logger = Log_Method().get_logger()		cls.http = HTTP_Request(cls.logger)		cls.config = Read_Config(cls.logger)		cls.ip = cls.config.read_config("server","ip")		cls.url = cls.config.read_config("login","url2")		cls.data = int(cls.config.read_config("login", "data"))		cls.expected = int(cls.config.read_config("login", "expected"))		cls.result = int(cls.config.read_config("login", "result"))		cls.excel = Excerl_Method(cls.logger,"register")		cls.data_list = cls.excel.read_excel()	def test_register(self):		for i in range(len(self.data_list)):			self.response = self.http.post_request(self.url,eval(self.data_list[i][self.data]))			if self.data_list[i][self.expected] in self.response.decode():				self.excel.write_excel(i+2,"pass")			else:				self.excel.write_excel(i+2,"fail")if __name__ == '__main__':	unittest.main()