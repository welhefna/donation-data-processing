import sys
import traceback
from Analytic.Reader import Reader
from Analytic.Tokenizer import Tokenizer
from Analytic.Validator import Validator
from Analytic.Contributor import Contributor
from Analytic.Percentile import Percentile
from Analytic.Writer import Writer

import time

class FEC:
	def __init__(self,helper_objects_dictionary):
		self.tokenizer=helper_objects_dictionary['tokenizer']
		self.validator=helper_objects_dictionary['validator']
		self.percentile=helper_objects_dictionary['percentile']
		self.reader=helper_objects_dictionary['reader']
		self.writer=helper_objects_dictionary['writer']

	
	def FEC_Analytic(self):
		
		contributors=list()
		contributorsIndex=dict()
		
		#process all contributions stream
		for cdata in self.reader.read():
			
			#form contributor data record
			donor=Contributor.Contributor(cdata,self.validator.validate)
			
			#validated and update Contributor data
			if donor.isValid():
				identification=donor['NAME']+donor['ZIP_CODE']
				try:
					contributors[contributorsIndex[identification]].append(donor)
				except KeyError:
					contributors.append(donor)
					contributorsIndex[identification]=len(contributors)-1
	
		#store amounts of Contributor
		amounts=list()
		
		#store amounts of Contributor
		repeated_donors=list()
		
		#calculate total repeated donor and total amounts
		repeated_donor_count=0
		total_amount=0
		
		#process contributors data
		for donor in contributors:
			if donor.isRepeated():
				
				repeated_donor_count+=1
				amounts,percentile_value=self.percentile.running(amounts,donor['TRANSACTION_AMT'])

				for amt in donor['TRANSACTION_AMT']:
					total_amount+=amt
					
				repeated_donors.append({'CMTE_ID':donor['CMTE_ID'],'ZIP_CODE':donor['ZIP_CODE'],'TRANSACTION_DT':donor['TRANSACTION_DT'],
							'PERCENTILE':percentile_value,'TOTAL':total_amount,'REPEATED_DONOR':repeated_donor_count})
		
		#save all repeated donor information in output file
		self.writer.write(repeated_donors)



def getFileHandler(file_path,mode):
	try:
		file_handler=open(file_path,mode)
	except IOError as e:
		print "I/O error({0}) {2} : {1}".format(e.errno, e.strerror, file_path)
		exit()
	except :
		print "Unexpected error({0}) : {1}".format(sys.exc_info()[2], file_path) 
		exit()

	return file_handler

def main():
	#read command line arguments as input file , precentile file path, then output file path respectively.
	if (len(sys.argv) != 4):
		print 'usage : python ', len(sys.argv)
		print 'usage : python ./src/donation-analytics.py ./input/itcont.txt ./input/percentile.txt ./output/repeat_donors.txt'
		print 'Example : python ./src/donation-analytics.py ./input/itcont.txt ./input/percentile.txt ./output/repeat_donors.txt'
		quit()	
		
		
	#FEC file data considerations 
	#raw file input data dictionary keys 
	raw_input_fields=['CMTE_ID','AMNDT_IND','RPT_TP','TRANSACTION_PGI','IMAGE_NUM','TRANSACTION_TP','ENTITY_TP','NAME','CITY','STATE','ZIP_CODE',
			  'EMPLOYER','OCCUPATION','TRANSACTION_DT','TRANSACTION_AMT','OTHER_ID','TRAN_ID','FILE_NUM','MEMO_CD','MEMO_TEXT','SUB_ID']
	
	#input file data dictionary options
	selected_fields_options={'CMTE_ID': None,'NAME': None,'ZIP_CODE':5,'TRANSACTION_DT':-4,'TRANSACTION_AMT':None,'OTHER_ID': None}
	
	#input file data dictionary values size
	selected_fields_validation={'CMTE_ID': None,'NAME': None,'ZIP_CODE':5,'TRANSACTION_DT':4,'TRANSACTION_AMT':None,'OTHER_ID': 0}
	
	#output data dictionary keys and order
	output_list=['CMTE_ID','ZIP_CODE','TRANSACTION_DT','PERCENTILE','TOTAL','REPEATED_DONOR']
	
	
	#create files handlers
	#input file handler
	itcont_file=getFileHandler(sys.argv[1],'r')
	
	#precentil file handler
	percentile_file=getFileHandler(sys.argv[2],'r')
	
	#output file handler
	repeat_donors_file=getFileHandler(sys.argv[3],'w')
	
	
	
	#create FEC records tokenizer
	tokenizer=Tokenizer.Tokenizer(raw_input_fields,selected_fields_options,'|')	
	
	#create FEC records validator
	validator=Validator.Validator(selected_fields_validation)
	
	#create FEC percentile
	percentile=Percentile.Percentile()
	
	try:
		percentile.file(percentile_file)
	except:
		print traceback.format_exc()
		exit()
	
	
	#create FEC reader
	reader=Reader.Reader(itcont_file,tokenizer.tokenize)
	
	#create FEC writer 
	writer=Writer.Writer(repeat_donors_file,output_list,'|')
	
	
	
	#FEC configuration dictionary
	helper_objects_dictionary={'tokenizer':tokenizer,'validator':validator,'percentile':percentile,'reader':reader,'writer':writer}
	fec=FEC(helper_objects_dictionary)
	fec.FEC_Analytic()
	
	#close input and output files handlers
	itcont_file.close()
	percentile_file.close()
	repeat_donors_file.close()
	


if __name__=="__main__":
	t=time.time()
	main()
	print "Execution Time : ",time.time()-t
