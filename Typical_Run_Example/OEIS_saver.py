import requests
import sys

dl_start_idx = int(sys.argv[1]) #sequence index to start download from
dl_stop_idx = int(sys.argv[2])+1 # sequence index to terminate download at
errs = [] # store the sequence indexes which were problematic saving to the file

def OEIS_formatter(text):
	lines = text.split("\n")
	sequence = "SEQUENCE: "
	name_seq = "NAME: "
	props = "PROPERTIES: \n"

	#The info we need is just the name, few terms and some properties of the sequence

	#As per their page format, a few terms of the sequence are contained in lines index 
	#	6 to 8. The first 10 characters in each of these lines are "%S","%T", "%U" respectively
	#Line index 9 contains the name of the sequence with the first two characters being "%N"
	#From line index 10 to somewhere, the first two characters of each line are "%C" and remaining contains
	#	a few properties of the sequence. This may or may not be present.

	#All the lines that follow from index 6 to end,contain sequence_id from character indices 3 to 9
	#We don't need that as in our case, the for_loop_index is just that thing

	sequence += lines[6][11:] + lines[7][11:] + lines[8][11:]
	name_seq += lines[9][11:]

	props_start_idx = 10
	props_end_idx = 10

	for i in range(10,len(lines)):
		if lines[i][0:2] != "%C":
			props_end_idx = i
			break

	props += "\n".join(a[11:] for a in lines[props_start_idx:props_end_idx])

	finalText = name_seq + "\n" + sequence + "\n" + props + "\n" + "\n" + "\n"

	return finalText

with open("OEIS_text.txt",'a+') as fd: #We just append to the file as previous data may be present
	for i in range(dl_start_idx,dl_stop_idx):
		article_url = "https://oeis.org/search?q=id:A" + str(1000000+i)[1:] + "&fmt=text"
		req = requests.get(article_url)

		print("Writing "+str(i))

		try:
			fd.write(OEIS_formatter(req.text))
		except:
			print("Could not write " + str(i) + ", skipping it and continuing")
			errs.append(str(i)) 

#In case of any error, save the sequence index in err_log.txt file for help in manual scraping
with open("err_log.txt",'a+') as err_log:
	err_log.write('\n'.join(errs)+"\n")

