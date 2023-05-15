# Existing Data
# Columns are Brand, Model name, Quantity, Price, and Status
# Primary key is the model name
existStock = [
    ['Senny','HD560S',3,160,'New'],
    ['Senny','HD600',4,375,'New'],
    ['ATH','M40x',5,120,'New'],
    ['Grado','SR60x',1,75,'Open box']
]

# Function Declarations

# Menu
def printMenu():
    print('Welcome to JR\'s Audio Warehouse')
    print('Please select the menu selections below:\nMenu List:\n1. Show the available item(s)\n2. Add a new item into Stock\n3. Delete an item from Stock\n4. Update an item from Stock\n5. Exit Program')

def printlist():
    print('------------------------- Stock List --------------------------')
    print("Index\t|Brand\t|Model\t|Quantity (pcs) |Price (USD) |Status\t\n---------------------------------------------------------------")
    for i in range(len(existStock)):
        print('{}\t|{}\t|{}\t| {}\t\t| {}\t\t\b\b\b| {}\t'.format(i,existStock[i][0],existStock[i][1],existStock[i][2],existStock[i][3],existStock[i][4]))
    print('---------------------- End of Stock List ----------------------')

# Create function declaration
def addItem():
    newBrand = input("Enter the new brand of item : ")
    newQuan = int(input("Enter the new item quantity : "))
    newPrice = int(input('Enter the new item price : '))
    newStatus = input('Enter the new item status : ')
    newItem = [newBrand,newModel,newQuan,newPrice,newStatus]
    userPrompt = input('Do you want to save the item addition into Stock list?(Y/N)')
    if userPrompt ==  'Y' or userPrompt == 'y':
        existStock.append(newItem)
        print('Item successfully saved into Stock list')
        newItem.clear()
    elif userPrompt == 'N' or userPrompt == 'n':
        print('No change saved into system')
        newItem.clear()


# Delete function declaration
def delItem():
    delName = int(input('Enter the index of item to be deleted:'))
    userPrompt = input('Please confirm the action of deleting item with index no. {} (Y/N)'.format(delName))
    if userPrompt ==  'Y' or userPrompt == 'y':
        existStock.pop(delName)
        print('Item successfully deleted from Stock list')
    elif userPrompt == 'N' or userPrompt == 'n':
        print('No change saved into system')


# Search function declaration
result = []
def dataLook():
    userSearch = input('Please enter the desired search data : ')
    try:
        checker = any (int(userSearch) in x for x in existStock)
    except:
        checker = any (userSearch in x for x in existStock)
    if checker == True:
        result.append(True)
        result.append(userSearch)
    else:
        result.append(False)
        result.append(userSearch)

# Index Search and Item Updater Function
def searcher():
    for x in range(0,len(existStock)):
        try:
            pos1 = existStock[x].index(modele)
            if pos1 == True:
                print("Index\t|Brand\t|Model\t| Quantity  | Price\t| Status")
                print('{}\t|{}\t|{}\t| {}\t    | {}\t| {}'.format(x,existStock[x][0],existStock[x][1],existStock[x][2],existStock[x][3],existStock[x][4]))
                if userPutMain == 4:
                    userPrompt = input('Do you want to continue item update process?(Y/N)')
                    if userPrompt ==  'Y' or userPrompt == 'y':
                        selector = int(input('Select the column to update : \n1. Brand\n2. Model\n3. Quantity\n4. Price\n5. Status\n'))
                        if selector == 1:
                            newBrand = input('Enter the new Brand to update, formerly {} : '.format(existStock[x][0]))
                            userPrompt = input('Do you want to save update into Stock List?(Y/N)')
                            if userPrompt == 'Y' or userPrompt == 'y':
                                existStock[x][0] = newBrand
                                print('Update of data have been saved into Stock List')
                                printlist()
                            elif userPrompt == 'N' or userPrompt == 'n':
                                print('No change saved into Stock List')
                        elif selector == 2:
                            newModelName = input('Enter the new Model name to update, formerly {} : '.format(existStock[x][1]))
                            userPrompt = input('Do you want to save update into Stock List?(Y/N)')
                            if userPrompt == 'Y' or userPrompt == 'y':
                                existStock[x][1] = newModelName
                                print('Update of data have been saved into Stock List')
                                printlist()
                            elif userPrompt == 'N' or userPrompt == 'n':
                                print('No change saved into Stock List')
                        elif selector == 3:
                            newQuant = int(input('Enter the new Quantity, formerly {} unit(s) : '.format(existStock[x][2])))
                            userPrompt = input('Do you want to save update into Stock List?(Y/N)')
                            if userPrompt == 'Y' or userPrompt == 'y':
                                existStock[x][2] = newQuant
                                print('Update of data have been saved into Stock List')
                                printlist()
                            elif userPrompt == 'N' or userPrompt == 'n':
                                print('No change saved into Stock List')
                        elif selector == 4:
                            newPrice = int(input('Enter the new Price, formerly {} USD : '.format(existStock[x][3])))
                            userPrompt = input('Do you want to save update into Stock List?(Y/N)')
                            if userPrompt == 'Y' or userPrompt == 'y':
                                existStock[x][3] = newPrice
                                print('Update of data have been saved into Stock List')
                                printlist()
                            elif userPrompt == 'N' or userPrompt == 'n':
                                print('No change saved into Stock List')
                        elif selector == 5:
                            newStat = input('Enter the new Status, formerly {} : '.format(existStock[x][4]))
                            userPrompt = input('Do you want to save update into Stock List?(Y/N)')
                            if userPrompt == 'Y' or userPrompt == 'y':
                                existStock[x][4] = newStat
                                print('Update of data have been saved into Stock List')
                                printlist()
                            elif userPrompt == 'N' or userPrompt == 'n':
                                print('No change saved into Stock List')
                    elif userPrompt == 'N' or userPrompt == 'n':
                        pass
                else:
                    break
            break
        except:
            pass


# Main Loop
i = 0
while i < 1:
        try:
            printMenu()
            userPutMain = int(input('Please enter your menu selection number :'))
            if userPutMain == 1:
                # Read submenu
                printlist()
                subA = 0
                while subA < 1:
                    print('Additional submenu:\n1. Search for existing data\n2. Search for existing models\n3. Back to Main Menu')
                    userPutSub1 = int(input('Please enter your submenu selection number :'))
                    if userPutSub1 == 1:
                        dataLook()
                        if result[0] == True:
                            print('Yes, this following data does exist in Stock list :',result[1])
                            result.clear()
                            printlist()
                        else:
                            print('No, this following data does not exist in Stock list :',result[1])
                            result.clear()
                    elif userPutSub1 == 2:
                        dataLook()
                        if result[0] == True:
                            modele = result[1]
                            print('Yes, this following model does exist in Stock list :',result[1])
                            result.clear()
                            searcher()
                        else:
                            print('No, this following model does not exist in Stock list :',result[1])
                            result.clear()
                    elif userPutSub1 == 3:
                        break
                    else:
                        print('!-- Wrong input, no submenu selection with typed number please try again --!')
            elif userPutMain == 2:
                # Create submenu
                subB = 0
                while subB < 1:
                    print('Additional submenu:\n1. Add new item into Stocklist\n2. Back to Main Menu')
                    userPutSub2 = int(input('Please enter your submenu selection number :'))
                    if userPutSub2 == 1:
                        newModel = input("Enter the new item model : ")
                        print('Caution, please reenter the model name below to check for model name duplicates')
                        dataLook()
                        if result[0] == True:
                            print('Yes, this following model already exist in Stock list :',result[1])
                            result.clear()
                        else:
                            result.clear()
                            print('Model name does not exist in Stock list, please continue to enter the remaining data below:')
                            addItem()
                            print('Current Stock List below :')
                            printlist()
                    elif userPutSub2 == 2:
                        break
                    else:
                        print('!-- Wrong input, no submenu selection with typed number please try again --!')
            elif userPutMain == 3:
                # Delete submenu
                subC = 0
                while subC < 1:
                    print('Item deletion additional submenu:\n1. Item check\n2. Back to Main Menu')
                    userPutSub3 = int(input('Please enter your submenu selection number :'))
                    if userPutSub3 == 1:
                        dataLook()
                        if result[0] == True:
                            print('Yes, this following data does exist in Stock list :',result[1])
                            result.clear()
                            delItem()
                            printlist()
                        else:
                            print('No, this following data does not exist in Stock list :',result[1])
                            result.clear()
                    elif userPutSub3 == 2:
                        break
                    else:
                        print('!-- Wrong input, no submenu selection with typed number please try again --!')

            elif userPutMain == 4:
                # Update submenu
                subD = 0
                while subD < 1:
                    print('Stock List update submenu:\n1. Update existing item in Stock List\n2. Back to Main Menu')
                    userPutSub4 = int(input('Please enter your submenu selection number :'))
                    if userPutSub4 == 1:
                        modele = input('Please enter the model name intended to update :')
                        print('**Please retype the model name to confirm**')
                        dataLook()
                        if result[0] == True:
                            result.clear()
                            searcher()
                        else:
                            print('No, this following data does not exist in Stock list :',result[1])
                            result.clear()
                    elif userPutSub4 == 2:
                        break
                    else:
                        print('!-- Wrong input, no submenu selection with typed number please try again --!')
            elif userPutMain == 5:
                break
            else:
                print('!-- Wrong input, no menu selection with typed number please try again --!')
        except ValueError:
            print("--------------------------!!--------------------------\n Please do not type letters into menu selection field \n--------------------------!!--------------------------")
