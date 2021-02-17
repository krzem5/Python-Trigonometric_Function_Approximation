def sin(v):
	return (4*v*(180-v))/(40500-v*(180-v))



def cos(v):
	return sin(v+90)



print(sin(47))
print(cos(47))
