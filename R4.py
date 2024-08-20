import re
# import difflib
from googletrans import Translator, constants

from pprint import pprint
# from PyDictionary import PyDictionary
translator = Translator()

# dictionary=PyDictionary()
with open(r"C:\Users\Reza\Desktop\sub\friends1.txt", "+r" , encoding="utf8") as x:
    list1 = []
    for line in x:
        line = re.sub("\d+", "", line)
        line = line.replace('\n' , '').replace('...','').replace(".", "").replace("[", "").replace("]", "").replace("monica", "").replace("chandler","").replace("Joey", "").replace("ross","").replace("!", "").replace(",","").replace("?", "").replace("PHOEBE", "").lower().replace("\"" , "").replace('\'' , "").replace("&" , "").replace(":" , "").replace("i>","").replace("</i>","").replace("$", "").replace(">", "").replace("<","").replace("(", "").replace(")" , "").replace("\"" , "").replace("©", "").replace("ã","").replace("_", "").replace("-","").replace("+", "").replace("*","").replace("#", "").replace("=","").replace("@", "")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
     #    if re.search('^\d', line):
     #        continue
        
        list1.append(line)
new_list=[]
for i in list1:
        list2 = i.split()
        for j in list2:
            new_list.append(j)
new_list = set(new_list)
new_list= list(new_list)
# balad_list = []
# for i in new_list:
#      if len(i)==1 or len(i)== 2   :
#           balad_list.append(i)

# with open(r"C:\Users\Reza\Desktop\sub\balad.txt", "r" ) as b:
#      for i in b :
#           i = i.replace('\n' , '').replace(' ', "")
#           balad_list.append(i)

# for i in balad_list:
#      if i in new_list:
#           new_list.remove(i)
# empty_list = []
# for i in new_list:
#      r= set(new_list) - {i}
#      r= list(r)
#      empty_list += difflib.get_close_matches(i,r)
#      new_list = set(new_list) - set(difflib.get_close_matches(i,r, n=0)) 

# empty_list = set(empty_list)
# empty_list = list(empty_list)
new_list.sort()

# new_list.sort()
with open(r"C:\Users\Reza\Desktop\sub\diff.txt", "+r") as y:
     for i in new_list:
          translation = translator.translate(i, dest='fa')
          y.write(F"{i} : {translation.text}  \n")

