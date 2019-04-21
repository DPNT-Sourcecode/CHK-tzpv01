

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	pr=dict.fromkeys(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),0)
	for sku in list(skus):
		if sku.isupper():
			pr[sku]=pr[sku]+1;
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
	
	
	sum+=pr['G']*20
	
	
	
	sum=sum+int(pr['H']/10)*80
	pr['H']=int(pr['H']%10)
	sum=sum+int(pr['H']/5)*45
	sum=sum+int(pr['H']%5)*10
	
	sum+=pr['I']*35
	sum+=pr['J']*60
	
	sum=sum+int(pr['K']/2)*120
	sum=sum+int(pr['K']%2)*70
	
	
	sum+=pr['L']*90
	
	
	
	
	
	sum+=pr['N']*40
	if (pr['M']-int(pr['N']/3))>=0:
		pr['M']=pr['M']-int(pr['N']/3)
		sum+=pr['M']*15
	
	
	sum+=pr['O']*10
	
	sum=sum+int(pr['P']/5)*200
	sum=sum+int(pr['P']%5)*50
	
	
	
	sum+=pr['R']*50
	if (pr['Q']-int(pr['R']/3))>=0:
		pr['Q']=pr['Q']-int(pr['R']/3)
		sum=sum+int(pr['Q']/3)*80
		sum=sum+int(pr['Q']%3)*30
	

	
	
	
	sum=sum+(pr['U']-int(pr['U']/4))*40
	
	
	
	
	sum=sum+int(pr['V']/3)*130
	pr['V']=int(pr['V']%3)
	sum=sum+int(pr['V']/2)*90
	sum=sum+int(pr['V']%2)*50
	
	
	sum+=pr['W']*20
	
	
	
	group_d=pr['X']+pr['S']+pr['T']+pr['Y']+pr['Z']
	sum+=int(group_d/3)*45
	group_d=int(group_d/3)*3
	if group_d>=3:
		if (group_d-pr['Z'])>=0:
			group_d-=pr['Z']
			pr['Z']=0
		elif group_d>0:
			pr['Z']-=group_d
			group_d=0
			
		if (group_d-pr['Y'])>=0:
			group_d-=pr['Y']
			pr['Y']=0
		elif group_d>0:
			pr['Y']-=group_d
			group_d=0
			
		if (group_d-pr['T'])>=0:
			group_d-=pr['T']
			pr['T']=0
		elif group_d>0:
			pr['T']-=group_d
			group_d=0
			
		if (group_d-pr['S'])>=0:
			group_d-=pr['S']
			pr['S']=0
		else:
			pr['S']-=group_d
			group_d=0
			
		if (group_d-pr['X'])>=0:
			group_d-=pr['X']
			pr['X']=0	
		elif group_d>0:
			pr['X']-=group_d
			group_d=0
	

	sum+=pr['X']*17
	sum+=pr['S']*20
	sum+=pr['T']*20
	sum+=pr['Y']*20
	sum+=pr['Z']*21

	
	
	return sum


