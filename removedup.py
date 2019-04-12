from collections import OrderedDict
def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str))  
if __name__ == "__main__": 
    str =input()
print(removeDupWithOrder(str))
