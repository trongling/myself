# Encoding: utf-8# Date: 2019/5/30# Name: 仲玲from selenium import webdriverfrom commen.read_config import Read_Configclass Broswer_setup():	def __init__(self,logger):		self.logger = logger		self.con = Read_Config(logger)		self.broswer = self.con.read_config("server","broswer")		self.br = self.broswer.lower()	def get_broswer(self):		if self.br == "chrome":			return webdriver.Chrome		if self.br == "firefox":			return webdriver.Firefox		if self.br == "ie":			return webdriver.Ieif __name__ == '__main__':	from commen.log_method import Log_Method	logger = Log_Method().get_logger()	bro = Broswer_setup(logger).get_broswer()