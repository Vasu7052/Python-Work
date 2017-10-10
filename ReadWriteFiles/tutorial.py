fw = open("sample.txt" , "w" )
fw.write("I am writing some text in my files\n")
fw.write("Yes its working")
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()