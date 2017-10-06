Words = ["a","a","a","a","a",'a',"a","a","A","b"]
newWord = raw_input("what letter do you want to add to the array")
if newWord in Words:
	print "your letter is in my array"
else:
	Words[0] = newWord
print Words