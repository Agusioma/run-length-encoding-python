def encode(message):
    encoded_message = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1): 
            if (message[j] == message[j+1]): 
                count = count+1
                j = j+1
            else: 
                break
        encoded_message=encoded_message+str(count)+ch
        i = j+1
    return encoded_message 

def decode(our_message):
	decoded_message = ""
	i=0
	j=0
	while (i <= len(our_message)-1):
		run_count = int(our_message[i])
		run_word = our_message[i + 1]
		for j in range(run_count):
			decoded_message = decoded_message+run_word
			j = j + 1
		i = i + 2
	return decoded_message

def display():
	our_message = "AuuBBBCCCCCCcccccCCCCCCCCCA"
	encoded_message=encode(our_message)
	decoded_message=decode(encoded_message)
	print(encoded_message)
	print(decoded_message)
    
display()