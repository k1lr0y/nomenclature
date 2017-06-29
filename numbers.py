import math
stop = 0


def vowels(num):
    if num == 0:
        return "Ō"
    elif num == 1:
    		return "i"
	  elif num == 2:
		    return "ŏ"
	  elif num == 3:
		    return "ŏi"
    elif num == 4:
		    return "w"
  	elif num == 5:
	    	return "wi"
  	elif num == 6:
	    	return "wŏ"
	  elif num == 7:
	    	return "wŏi"
	  elif num == 8:
	    	return "ĕ"
	  elif num == 9:
	    	return "ei"

def hex0(n):
  	if n < 0:
    		return "k"+vowels(abs(n))
	  else:
	    	return "d"+vowels(abs(n))

def translate(decnum,basenum):
	  print ('')
	  print (str(decnum)+":")
	  for a in range(-9,10):
		    for b in range(-9,10):
			      for c in range(-9,10):
				        for d in range(-9,10):
				        	  if str(decnum) == str(((int(basenum)**3)*a) + ((int(basenum)**2)*b) + (int(basenum)*c) + (d)):
						            if a == 0:	
							              if b == 0:
								                if c == 0:
						                  			print (hex0(d)+"n")
								                else:
						        			          print (hex0(c)+hex0(d)+"n")
	          				    		else:
						     	             	print (hex0(b)+hex0(c)+hex0(d)+"n")
					            	else:
						                print (hex0(a)+hex0(b)+hex0(c)+hex0(d)+"n")
		

def trans(decnum,basenum):
  	wordlist=[]
	  for a in range(-9,10):
		    for b in range(-9,10):
		        for c in range(-9,10):
		            for d in range(-9,10):
					          if str(decnum) == str(((int(basenum)**3)*a) + ((int(basenum)**2)*b) + (int(basenum)*c) + (d)):
			                	if a == 0:	
			                			if b == 0:
		                  					if c == 0:
		                    						wordlist.append(hex0(d)+"n")
			                  				else:
			                    					wordlist.append(hex0(c)+hex0(d)+"n")
			                 			else:
			                   				wordlist.append(hex0(b)+hex0(c)+hex0(d)+"n")
		               			else:
			                  			wordlist.append(hex0(a)+hex0(b)+hex0(c)+hex0(d)+"n")
    return wordlist
		
while stop == 0:
  	print ()
	  base = input("Enter base number: ")
	  numb = input("Enter decimal number for translation (q to quit): ")
	  if numb == "q":
		    stop = 1
  	else:
	    	print ()
		    print (str(numb)+" in base "+ str(base)+": ")
	    	print (trans(numb,base))
