#Write a number in full from 0 to 999 
#a value will be requested and with that value an answer will be given
#Example: "Say number: 4" the answer that should be given: "four"



#Comments
# Write one, two, three, four... It would be a very boring thing to do 
# Looking at it in a more practical way, the best thing would be to write only the units, tens and hundreds 
# Afeter that it would be more a matter of joining the numbers, but the question is... How??
# #


#dictionary of numbers
dicionario = dict()
dicionario ['0 to 9'] = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dicionario ['10 to 19']= ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
dicionario ['20 to 99']= ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
dicionario ['100 to 999']= ['One hundred', 'Two hundred', 'Three hundred', 'Four hundred', 'Five hundred', 'Six hundred', 'Seven hundred', 'Eight hundred', 'Nine hundred']

while True:
    #Main repeat
    while True:
        #Asking the value
        try:
            num = input('Enter a value berween 0 and 999: ')
            num_int = int(num)
            if 0 <= int(num) <= 999:
                num = num.lstrip('0')
                break
            print('Invalid value! Try again. ', end='')
        except:
            print('Only numbers!')


    if 9 >= int(num) >= 0:#0 to 9
            print(dicionario['0 to 9'][num_int])
            break


    elif 10 <= int(num) <= 19:#10 to 19
        num_1 = int(num[1])
        print(dicionario['10 to 19'][num_1])
        break    

    if 99 >= int(num) >= 20:#20 to 99
        num_1 = int(num[0])
        num_2 = int(num[1])
        print(dicionario['20 to 99'][num_1-2],end ='')
        if num_2 != 0:
            print('-' + dicionario['0 to 9'][num_2])
        break


    if 999 >= int(num) >= 100:#100 to 999
        num_1 = int(num[0])
        num_2 = int(num[1])
        num_3 = int(num[2])
        if num == '100':
            print('One hundred')
            break

        print(dicionario['100 to 999'][num_1-1], end = '')
        if num_2 != 0 or num_3 != 0 :
            if num_2 == 1:
                print(' and', dicionario['10 to 19'][num_3])
                break        

            if num_2 == 0:
                print(' and', dicionario['0 to 9'][num_3])
                break  
            
            else:
                print(' and', dicionario['20 to 99'][num_2-2], end = '')
                print('-' + dicionario['0 to 9'][num_3])
                break  



