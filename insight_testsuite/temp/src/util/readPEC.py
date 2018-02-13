class ReadPEC:
	def __init__(self,file_name):
		'''
		itype: file_name:str input file path
		'''
		self.file_name=file_name
		pass
	
	def read(self):
		'''
		itype: None
		rtype: data:str	       data stream 
		help: uses a gererator to read large file line by line (simulate data stream)
		'''
		try:
			with open(self.file_name) as file_handler:
				while True:
					data=file_handler.readline()
					if not data:
						break
					yield data
		except (IOError, OSError):
			print "Error opening file | processing file"
		except StopItreation:
			return
			