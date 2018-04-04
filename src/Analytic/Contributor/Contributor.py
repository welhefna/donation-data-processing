class Contributor:

	def __init__(self,contributor_dictionary,validator):
		self.__contributor_dictionary=contributor_dictionary
		self.__contributor_dictionary.update({'min_year':contributor_dictionary['TRANSACTION_DT'],'max_year':contributor_dictionary['TRANSACTION_DT']})
		self.__validator=validator
	
	def isValid(self):
		return self.__validator(self.__contributor_dictionary)
	
	def __str__(self):
		output=[ str(self.__contributor_dictionary[token]) for token in self.__contributor_dictionary.keys()]
		return  "|".join(output)
	
	def __getitem__(self, key): 
		return self.__contributor_dictionary[key]
	
	def __setitem__(self, key,item): 
		try:
		 	return self.__contributor_dictionary.update({key:item})
		except KeyError:
		 	print "setter wrong key"
		 	raise
	
		
	def append(self,contributor,key_list=['CMTE_ID','TRANSACTION_DT','TRANSACTION_AMT']):
		for key in key_list:
			self.__contributor_dictionary[key]+=','+contributor.__contributor_dictionary[key]
			
		if self.__contributor_dictionary['min_year']>contributor['min_year']:
			self.__contributor_dictionary.update({'min_year':contributor['min_year']})
			
		elif self.__contributor_dictionary['max_year']<contributor['max_year']:
			self.__contributor_dictionary.update({'max_year':contributor['max_year']})
	
		
	def isRepeated(self,key_id='CMTE_ID',key_data='TRANSACTION_DT',key_amount='TRANSACTION_AMT'):
		repeated=False
		amt=[]
		cmt=[]
		
		ID=self.__contributor_dictionary[key_id].split(',')
		amount=self.__contributor_dictionary[key_amount].split(',')
		years=self.__contributor_dictionary[key_data].split(',')
		
		max_year=self.__contributor_dictionary['max_year']
		min_year=self.__contributor_dictionary['min_year']

		if min_year<max_year:
			total_amount=0
			for yInd in range(len(years)):
				if years[yInd] ==  max_year:
					amt.append(int(amount[yInd]))
					cmt.append(ID[yInd])
					
			self.__contributor_dictionary[key_id]=cmt[-1]
			self.__contributor_dictionary[key_amount]=amt
			self.__contributor_dictionary[key_data]=str(max_year)
			
			repeated=True
		
		return repeated
		

		
		
		
		
if __name__=="__main__":
	pass
