import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='Productmatch.log',
                    filemode='w')


class ProductMatch(object):
	"""docstring for Product"""
	def __init__(self):
		self.Product_prdID={}
		self.get_all_product()
		self.get_all_prod_name_url()

	def get_all_product(self,Product_file='data\Mobiles-Master-Data.txt'):
		"""
		reading all the Product and Indix_Product_ID in a dictionary

		"""
		with open(Product_file,'r') as f:
			for line in f:
				parts=line.strip().split('\t')
				logging.info(parts)
				Indix_Product_Name=parts[0].lower()
				Indix_Product_ID=parts[1]
				self.Product_prdID[Indix_Product_Name]=Indix_Product_ID
		logging.info(self.Product_prdID)


	def getmatch(self,key):
		if self.Product_prdID.has_key(key):
			#print i
			print 'MATCH'
			logging.info('MATCH Result:')
			logging.info(key+'\t'+self.Product_prdID[key]+'\n')
			return self.Product_prdID[key]
		else :
			return False

	def get_all_prod_name_url(self,infibeamfile='data\Mobiles-Infibeam.txt'):
		with open(infibeamfile,'r') as f:
			i=0
			cnt=0
			for line in f:
				if i==0:
					i=1
					continue
				parts=line.strip().split('\t')
				Infi_Product_Name=parts[0]
				Infi_url=parts[1].lower()
				url_part=Infi_url.split('/')
				logging.info(url_part)
				pdx_candidate1=' '.join(url_part[4].split('-')[1:])
				pdx_candidate2=url_part[5].split('.')[0]
				logging.info(pdx_candidate1)
				logging.info(pdx_candidate2)
				#pdx_candidate.split()
				fullkey=pdx_candidate1.split()
				for i in range(1,len(fullkey)):
					logging.debug(fullkey[0:i])
					if self.getmatch(' '.join(fullkey[0:i])):
						key=' '.join(fullkey[0:i])
						print Infi_Product_Name+'\t'+Infi_url+'\t'+str(key)+'\t'+self.Product_prdID[key]+'\n'
				
				#print cnt
				#self.Product_prdID[Indix_Product_Name]=Indix_Product_ID

if __name__ == '__main__':
	p=ProductMatch()