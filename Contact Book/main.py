contacts = []
print('Welcome To contact book .\nFor see contacts please enter \"C\" and for add new Contact press \"N\".')
k = input()
b = 1
while(b==1):
    if k == 'C':
        for i in range(len(contacts)):
            print(contacts[i])
    if k == 'N':
        print('Please Enter Information of Contact.')
        n = input('contact name:')
        p = input('contact number:')
        contacts.append(f"Name: {n}\nNumber: {p}\n======================\n")
    print('For see contacts please enter \"C\" and for add new Contact press \"N\".')
    k = input()