

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	pr=[0 for i in range(skus.len())]
	for sku in list(skus):
		if sku.isupper():
			pr[sku]+=1;
		else:
			return -1;

	
	sum=0
		
	sum=sum+int(pr['A']/5)*200
	pr['A']=int(pr['A']%5)
	sum=sum+int(pr['A']/3)*130
	sum=sum+int(pr['A']%3)*50
	
	
			 
	sum=sum+pr['C']*20
	sum=sum+pr['D']*15
	sum=sum+pr['E']*40
	
	if (pr['B']-int(pr['E']/2))>=0:
		pr['B']=pr['B']-int(pr['E']/2)
		sum=sum+int(pr['B']/2)*45
		sum=sum+int(pr['B']%2)*30
		
	sum=sum+(pr['F']-int(pr['F']/3))*10
	return sum




