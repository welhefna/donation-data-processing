'''
iterator pattern
'''
class Writer:
	def __init__(self,file_handler,output_keys,token):
		self.__file_handler=file_handler
		self.__output_keys=output_keys
		self.__token=str(token)
	
	
	def write(self,records):
		tmp_out=''
		for record in records:
			tmp_record=[]
			for key in self.__output_keys:
				tmp_record.append(str(record[key]))
			tmp_out+=(self.__token).join(tmp_record)+'\n'
		
		tmp_out+="\n"
		
		self.__file_handler.write(tmp_out)
		
	