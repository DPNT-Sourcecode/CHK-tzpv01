

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	
	a=0
	b=0
	c=0
	d=0
	for sku in list(skus):
		if sku=='A':
			a+=1
		elif sku=='B':
			b+=1
		elif sku=='C':
			c+=1
		elif sku=='D':
			d+=1
		else:
			return -1
	
	sum=0
		
	sum=sum+int(a/3)*130
	sum=sum+int(a%3)*50
		
	sum=sum+int(b/2)*45
	sum=sum+int(b%2)*30
			 
	sum=sum+c*20
	sum=sum+d*15
	return sum



