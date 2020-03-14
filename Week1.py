class Teams:
    def __init__(self,members):
            self.__myTeam=members
    def __len__(self):
        return len(self.__myTeam)
    def __contains__(self, member):
        #print("in is from here only")
        return member in self.__myTeam
    def __iter__(self):
        #print("Iterator")
        return iter(self.__myTeam)
def main():
    classmates=Teams(['John','Steve','Tim'])
    print('Tim' in classmates)
    print('Sam' in classmates)
    iterator=iter(classmates)#we get iterable object reference
    for member in iterator:
        print(member,end=" ")
main()

# 3. classmates is not a class it it object that holds reference of Teams.Teams class implements __len__ method but not classmates.
# 
# 4. Interface specifies set of methods must be available to implement. It is more like when we are implementing encapsulation we define certain methods but we are not going implement there.
# 
# 5. We can implement each storage device as method in class. and we add necessary conditions for each storage device in method of class.
# We provide interface that allows to select a storage device and files that contain information and based on selection of storage device we call method that implements it.