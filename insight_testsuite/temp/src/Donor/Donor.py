class Contributor:
	def __init__(self,name,zip_code,amount_contributed,transaction_data,recipient_ID):
		self.name=name
		self.zip_code=zip_code
		self.amount_contributed=amount_contributed
		self.transaction_data=transaction_data
		self.recipient_ID=recipient_ID
		
	def identification(self):
		'''
		itype:None
		rtype: tuple name, ans zip_code
		help: this method return contributor identification as tuple conatin his name and zip code
		'''
		return (self.name,self.zip_code)
	
		
		
		
		
		
		
		
if __name__=="__main__":
	print "hello"