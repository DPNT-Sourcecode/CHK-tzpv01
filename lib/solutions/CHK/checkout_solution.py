

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	try:
		sum=0
		sku=list(skus)
		
		sum=sum+(sku[0]/3)*130
		sum=sum+(sku[0]%3)*50
		
		sum=sum+(sku[1]/2)*45
		sum=sum+(sku[1]%2)*30
			 
		sum=sum+sku[2]*20
		sum=sum+sku[3]*15
		return sum

	except:
		return -1;

