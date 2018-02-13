import unittest
import math
class Percentile:
	def __init__(self,precentile=50):
		"""
		create and initialize a new Percentile
		percentile -- percentil value integer (defualt 50)
		"""
		self.__precentile=precentile
	
	def set(self,precentile):
		self.__precentile=precentile
		
	def file(self,file_handler):
		pct=file_handler.readline()
		try:
		       precentile=int(pct)
		       if precentile>=0 and precentile<=100:
		       		self.__precentile
		       else:
				raise Exception("precentile is not in range 0 to 100") 
		       
		except ValueError:
			raise Exception("precentile is not a numeric value")
			
		
	def merger(self,left,right):
		"""
		2-merge form a sorted array arr from two arrays  
		left -- sorted array
		right -- sorted array 
		"""
		
		i=0
		j=0
		k=0
		arr=[0]*(len(left)+len(right))
		
		while i<len(left) and j<len(right):
			if left[i]<right[j]:
				arr[k]=left[i]
				i=i+1
			else:
				arr[k]=right[j]
				j=j+1
			k=k+1
		
		while i<len(left):
			arr[k]=left[i]
			i=i+1
			k=k+1
			
		if j <len(right):
			arr[k]=right[j]
			j=j+1
			k=k+1
			
		return arr
			
		
	def quantile(self,arr):
		"""
		calculate running quantailes for given sorted array and percentile
		Keyword arguments:
		arr -- sorted array of integers
		"""
		arr_length=len(arr)
		if arr_length<1:
			return []
		index=arr_length*self.__precentile/100.0
		if not (index).is_integer():
			result=arr[int(math.ceil(index))-1]
		else:
			result=arr[int(index)-1]
		
		return result
			
		'''
		if arr_length>0:
			return arr[int(0.5+( arr_length - 1 ) * (self.__precentile/100.0))]
		else:
			return []
		'''
		
	def running(self,left,right):
		arr=self.merger(left,right)
		pct=self.quantile(arr)
		return arr,pct
		
		
class Test(unittest.TestCase):		
	def test_Percentile(self):
		"""
		unittest for percentile class test coverage 
		"""
		percentile=Percentile()
		
		#check if 
		self.assertEqual(percentile.merger([],[]), [])
		
		#test quantail calculations
		
		#test run behavoir if the input list empty
		percentile.set(25)
		self.assertEqual(percentile.quantile([]),[]) 
		
		#test Q1
		percentile.set(25)
		self.assertEqual(percentile.quantile([2,4,4,5,6,7,8]), 4) #odd
		self.assertEqual(percentile.quantile([1, 3, 3, 4, 5, 6, 6, 7, 8, 8]), 3) #even
		
		#test Q2
		percentile.set(50)
		self.assertEqual(percentile.quantile([2,4,4,5,6,7,8]), 5)
		self.assertEqual(percentile.quantile([1, 3, 3, 4, 5, 6, 6, 7, 8, 8]), 5)
		
		#test Q3
		percentile.set(75)
		self.assertEqual(percentile.quantile([2,4,4,5,6,7,8]), 7)	
		self.assertEqual(percentile.quantile([1, 3, 3, 4, 5, 6, 6, 7, 8, 8]), 7) 
	
if __name__=="__main__":
	unittest.main()
	