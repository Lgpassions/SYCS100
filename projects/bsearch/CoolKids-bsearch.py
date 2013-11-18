Group Members


Dontrell Knighten
Glenisha Smith
Travon Speller
Jabari Olatunji
Oluwatoorese Lasebikan
Christian Quist


Solutions:


# def bSearch(searchList, target):
#    low = 0
#    high = len(searchList)
#    while low <= high:
#       if len(searchList)==0:
#          return "EMPTY LIST"
#       testpos = low + (high-low)/2
#       ITEM = searchList[testpos]
#       if ITEM == target:
#          return testpos            
#       elif ITEM < target: 
#          low = testpos+1
#       else:
#          high = testpos-1


#Glenisha Smith @02679391
# November 17, 2013
# SYCS 100
# Binary Search


# myList = sorted([67,78,9,67,53,24,23,87])
# myItem = 9
def bsearch(myItem, myList):
	low = 0
	high = (len(myList)-1)
	while low <= high:
		mid = (low + high)//2
		if myList[mid]== myItem:
			return mid
		elif myList[mid] < myItem:
			low = mid + 1
		else :
			high = mid - 1
	return -1

#print bsearch(18, [2,5,18])
