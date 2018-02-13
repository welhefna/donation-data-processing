import unittest

class Tokenizer:
	def __init__(self,raw_list,selected_dictionary,token):
		"""
		constructor set specifications of Tokenizer
		"""
		self.__raw_list=raw_list
		self.__selected_dictionary=selected_dictionary
		self.__token=token
		
	def tokenize(self,record):
		"""
		construct tokens of input string 
		record -- input string
		"""
		
		if type(record) != type(str()) or len(record)<1:
			return False
			
		record=record.strip()
		record=record.split(self.__token)

		rDict={}
		for key in self.__selected_dictionary.keys():
			if self.__selected_dictionary[key]:
				if self.__selected_dictionary[key]>=0:
					rDict[key]=record[self.__raw_list.index(key)][:self.__selected_dictionary[key]]
				else:
					rDict[key]=record[self.__raw_list.index(key)][self.__selected_dictionary[key]:]
			else:
				rDict[key]=record[self.__raw_list.index(key)]
				
		return rDict
		
		
class Test(unittest.TestCase):		
	def test_Tokenizer(self):
		"""
		unittest for Tokenizer class test coverage 
		"""
		raw_input_fields=['CMTE_ID','AMNDT_IND','RPT_TP','TRANSACTION_PGI','IMAGE_NUM','TRANSACTION_TP','ENTITY_TP','NAME','CITY','STATE','ZIP_CODE',
				  'EMPLOYER','OCCUPATION','TRANSACTION_DT','TRANSACTION_AMT','OTHER_ID','TRAN_ID','FILE_NUM','MEMO_CD','MEMO_TEXT','SUB_ID']
		selected_fields_options={'CMTE_ID': None,'NAME': None,'ZIP_CODE':5,'TRANSACTION_DT':-4,'TRANSACTION_AMT':None,'OTHER_ID': 0}
		tokenizer=Tokenizer(raw_input_fields,selected_fields_options,'|')
		
		record="C00384516|N|M2|P|201702039042410894|15|IND|SABOURIN, JAMES|LOOKOUT MOUNTAIN|GA|028956146|UNUM|SVP, CORPORATE COMMUNICATIONS|01312018|384||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339"

		#record has different data type of specifications 
		record=0
		self.assertFalse(tokenizer.tokenize(record))

		record=''
		self.assertFalse(tokenizer.tokenize(record))
		
		#empty dictionary
		record={}
		self.assertFalse(tokenizer.tokenize(record))

		#different format
		record={'x':0,'y':1}
		self.assertFalse(tokenizer.tokenize(record))


		#record in format 
		record="C00384516|N|M2|P|201702039042410894|15|IND|SABOURIN, JAMES|LOOKOUT MOUNTAIN|GA|028956146|UNUM|SVP, CORPORATE COMMUNICATIONS|01312018|384||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339"
		self.assertEqual(len(tokenizer.tokenize(record)),len(selected_fields_options.keys()))
	
if __name__=="__main__":
	unittest.main()
			
	

			