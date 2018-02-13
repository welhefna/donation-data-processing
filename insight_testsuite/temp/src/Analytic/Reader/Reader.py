'''
iterator pattern
'''
class Reader:
	def __init__(self,file_handler,tokenizer):
		'''
		itype: file_name:str input file path
		'''
		self.__file_iterator=iter(file_handler)
		self.__file_handler=file_handler
		self.__data_iterator=None
		self.__tokenizer=tokenizer #straty pattern
		
	def read(self):
		   while True:
		        record = self.__file_handler.readline()
		        if not record:
		            break
        		yield self.__tokenizer(record)
	'''
	def next(self):
		
		#next item in the itreator list
		
        	
        	if self.__data_iterator is None:
            		self.__data_iterator = iter(self.__tokenize(next(self.__file_iterator)))
        	try:
            		return self.__tokenize(next(self.__file_iterator))
        	except StopIteration:
        		pass
            		#self.__data_iterator = None
            		#return next(self)
			
		
	def __iter__(self):
		return self
	'''		
		