import unittest

class Validator:
	def __init__(self,validation_dictionary):
		"""
		constructor set validation specifications
		"""
		self.__validation_dictionary=validation_dictionary
		
	def validate(self,record):
		"""
		check if content of record is in the specification format
		record -- input data to validate
		"""
		
		if type(record) != type(self.__validation_dictionary):
			return False
			
		for key in self.__validation_dictionary.keys():
			if self.__validation_dictionary[key]!=None:
				if len(record[key])!= self.__validation_dictionary[key]:
					return False			
			else:	
				if record[key]=='':
					return False
		return True
	

class Test(unittest.TestCase):		
	def test_Validator(self):
		"""
		unittest for validator class test coverage 
		"""
		selected_fields_validation={'CMTE_ID': None,'NAME': None,'ZIP_CODE':5,'TRANSACTION_DT':4,'TRANSACTION_AMT':None,'OTHER_ID': 0}
		validator=Validator(selected_fields_validation)
		
		#record has different data type of specifications 
		record=0
		self.assertFalse(validator.validate(record))

		record=''
		self.assertFalse(validator.validate(record))
		
		#empty dictionary
		record={}
		self.assertFalse(validator.validate(record))

		#different format
		record={'x':0,'y':1}
		self.assertFalse(validator.validate(record))
		
		#dictionary with missing keys 
		record={'CMTE_ID': 'C00384818','ZIP_CODE':'23529','TRANSACTION_DT':'2018','TRANSACTION_AMT':'333','OTHER_ID': ''}
		self.assertFalse(validator.validate(record))
		
		#record has ZIP_CODE of size less than cofiguration specifications 
		record={'CMTE_ID': 'C00384818','NAME': 'Wessam','ZIP_CODE':'3529','TRANSACTION_DT':'2018','TRANSACTION_AMT':'333','OTHER_ID': ''}
		self.assertFalse(validator.validate(record))
		
		#record has ZIP_CODE of size less than cofiguration specifications 
		record={'CMTE_ID': 'C00384818','NAME': 'Wessam','ZIP_CODE':'3529','TRANSACTION_DT':'2018','TRANSACTION_AMT':'333','OTHER_ID': ''}
		self.assertFalse(validator.validate(record))

		#record in format 
		record={'CMTE_ID': 'C00384818','NAME': 'Wessam','ZIP_CODE':'23529','TRANSACTION_DT':'2018','TRANSACTION_AMT':'333','OTHER_ID': ''}
		self.assertTrue(validator.validate(record))
	
if __name__=="__main__":
	unittest.main()
				