import sys
from Analytic.Reader import Reader
from Analytic.Tokenizer import Tokenizer
from Analytic.Validator import Validator
from Analytic.Contributor import Contributor
from Analytic.Percentile import Percentile
from Analytic.Writer import Writer

import time

class Solution():
	def __init__(self,helper_objects_dictionary):
		self.tokenizer=helper_objects_dictionary['tokenizer']
		self.validator=helper_objects_dictionary['validator']
		self.percentile=helper_objects_dictionary['percentile']
		self.reader=helper_objects_dictionary['reader']
		self.writer=helper_objects_dictionary['writer']

	
	def FEC_solution(self):
		
		contributors=list()
		contributorsIndex=dict()
		
		for cdata in self.reader.read():
			donor=Contributor.Contributor(cdata,self.validator.validate)
			if donor.isValid():
				identification=donor['NAME']+donor['ZIP_CODE']
				try:
					contributors[contributorsIndex[identification]].append(donor)
				except KeyError:
					contributors.append(donor)
					contributorsIndex[identification]=len(contributors)-1
	

		total_contribution=0
		repeated_donor_count=0
		running_amount_list=[]
		
		print len(contributors)
		
		repeatedDonors=list()
		for donor in contributors:
			if donor.isRepeated():
				
				repeated_donor_count+=1
				running_amount_list=self.percentile.merger(running_amount_list,donor['TRANSACTION_AMT'])
				percentile_value=self.percentile.runnningQuantiles(running_amount_list,30)
				repeatedDonors.append({'CMTE_ID':donor['CMTE_ID'],'ZIP_CODE':donor['ZIP_CODE'],'TRANSACTION_DT':donor['TRANSACTION_DT'],
							'PERCENTILE':percentile_value,'TOTAL':sum(running_amount_list),'REPEATED_DONOR':repeated_donor_count})

		self.writer.write(repeatedDonors)



def getFileHandler(file_path,mode):
	try:
		file=open(file_path,mode)
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		exit()
	except :
		print "Unexpected error:", sys.exc_info()[0]
		exit()

	return file

def main():
	if (len(sys.argv) != 4):
		print 'usage : python ', len(sys.argv)
		print 'usage : python ./src/donation-analytics.py ./input/itcont.txt ./input/percentile.txt ./output/repeat_donors.txt'
		print 'Example : python ./src/donation-analytics.py ./input/itcont.txt ./input/percentile.txt ./output/repeat_donors.txt'
		quit()	
		
	raw_input_fields=['CMTE_ID','AMNDT_IND','RPT_TP','TRANSACTION_PGI','IMAGE_NUM','TRANSACTION_TP','ENTITY_TP','NAME','CITY','STATE','ZIP_CODE',
			  'EMPLOYER','OCCUPATION','TRANSACTION_DT','TRANSACTION_AMT','OTHER_ID','TRAN_ID','FILE_NUM','MEMO_CD','MEMO_TEXT','SUB_ID']
	selected_fields_options={'CMTE_ID': None,'NAME': None,'ZIP_CODE':5,'TRANSACTION_DT':-4,'TRANSACTION_AMT':None,'OTHER_ID': 0}
	selected_fields_validation={'CMTE_ID': None,'NAME': None,'ZIP_CODE':5,'TRANSACTION_DT':4,'TRANSACTION_AMT':None,'OTHER_ID': 0}
	output_list=['CMTE_ID','ZIP_CODE','TRANSACTION_DT','PERCENTILE','TOTAL','REPEATED_DONOR']
	
	itcont_file=getFileHandler(sys.argv[1],'r')
	percentile_file=getFileHandler(sys.argv[1],'r')
	repeat_donors_file=getFileHandler('../output/itcont.txt','w')
	
	percentile_value=percentile_file.readline()
	
	
	tokenizer=Tokenizer.Tokenizer(raw_input_fields,selected_fields_options,'|')	
	validator=Validator.Validator(selected_fields_validation)
	percentile=Percentile.Percentile(percentile_value)
	reader=Reader.Reader(input_file,tokenizer.tokenize)
	writer=Writer.Writer(output_file,output_list,'|')
	
	
	
	
	helper_objects_dictionary={'tokenizer':tokenizer,'validator':validator,'percentile':percentile,'reader':reader,'writer':writer}
	
	solution=Solution(helper_objects_dictionary).FEC_solution()
	
	itcont_file.close()
	percentile_file.close()
	percentile_file.close()
	


if __name__=="__main__":
	t=time.time()
	main()
	print time.time()-t
