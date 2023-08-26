#Question 1:

#Modify 'bubble_sort' function such that it can sort following list of transactions happening in an electronic store,

    # elements = [
    #         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    #         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    #         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    #         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    #     ]

#The 'bubble_sort' function should take key from a transaction record and sort the list as per that key. For example,

    # bubble_sort(elements, key='transaction_amount')
    # This will sort elements by transaction_amount and your sorted list will look like,

    # elements = [
    #         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    #         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    #         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    #         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    #     ]

#But if you call it like this,

    # bubble_sort(elements, key='name')

#The output will be,

    # elements = [
    #         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    #         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    #         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    #         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    #     ]


#My answer:
def modified_bubble_sort(list, sorting_dictionary_key):

    if sorting_dictionary_key != 'name' and sorting_dictionary_key != 'transaction_amount' and sorting_dictionary_key != 'device':
        print('Please enter an existing sorting category!')
        return
    
    size = len(list)

    for i in range(size - 1):
        swapped = False

        for j in range(size - 1 - i):
            index_plus_one = j+1
            if list[j][sorting_dictionary_key] > list[index_plus_one][sorting_dictionary_key]:
                temp = list[j]

                list[j] = list[index_plus_one]
                list[index_plus_one] = temp
                swapped = True

        if not swapped:                     #'if swapped == False' works as well
            break
        

if __name__ == '__main__':
    electronic_store_transactions = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    modified_bubble_sort(electronic_store_transactions, 'name')
    print(electronic_store_transactions)

    modified_bubble_sort(electronic_store_transactions, 'transaction_amount')
    print(electronic_store_transactions)

    modified_bubble_sort(electronic_store_transactions, 'device')
    print(electronic_store_transactions)


    #All works well, my answer looks correct, Solution is almost the same so won't be uploading Solution