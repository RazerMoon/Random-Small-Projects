
class FriendLists:
    def createLists(self): #Creates the lists and asks for input
        global lists
        list_no = 0
        
        while True:
            try:
                number_of_lists = int(input('How many lists do you want to make? (integer): '))
                break
            except ValueError:
                print('Not a valid integer! Please try again')
    
        lists = [[] for i in range(number_of_lists)]
    
        for list_number in lists:
            list_no = list_no + 1
            list_number.extend([name for name in input(f'Enter friends for list {list_no} (Space between each name): ').split()])
            print(f"Friends in list {list_no}: ", list_number)
    
    def listProperties(self): #Checks for commonality between lists by converting them into sets
        global res1, res2, res3
    
        if len(lists) > 2: #If there are more than two lists
            res1 = list(set.intersection(*map(set, lists))) #Common across all
            res2 = list((set.union(*map(set, lists))-set.intersection(*map(set, lists)))) #Not common between all
        else: #If there are two or less lists
            res1 = list(set.intersection(*map(set, lists))) #Common across all
            res2 = list(set.symmetric_difference(*map(set, lists))) #Not common at all

    def displayProperties(self):
        message = (f"""
        ------------------------------------------
        Friends common across all lists - {res1}
        Friends not common across all lists - {res2}
        ------------------------------------------
        """)
        return message

    def createFile(self):
        f = open("uncommon_friends.txt","w+")
        f.write(self.displayProperties())
        f.close()

    def __init__(self):
        self.createLists()
        self.listProperties()
        print(self.displayProperties())
        self.createFile()

if __name__ == '__main__':
    s = FriendLists()