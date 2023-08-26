#After watching through codebasics' video on the Shell Sort Algorithm, I tried to implement his visualised
#explanation algorithmically of Shell Sort Algorithm (with reference to the original code of Shell Sort Algorithm).

#It works, but this implementation of the Shell Sort Algorithm carries out the Shell Sort Algorithm slightly 
#differently from how the original code Shell Sort Algorithm does. You can do debugging to see the difference.

#I am not going to type out his visualised explanation since I believe its not the clearest explanation of the
#Shell Sort Algorithm. But if you're curious to see how this implementation of Shell Sort Algorithm works, you
#can go and take a look at codebasics' video on his visualised explanation of Shell Sort Algorithm which I based
#this implementation of Shell Sort Algorithm off of
#-> Link: https://www.youtube.com/watch?v=VxNr9Vudp4Y&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=18


#What this function does is that it is my own implementation of the Shell Sort Algorithm, based on the visualised 
#explanation from codebasics' video on the Shell Sort Algorithm
def my_implementation_of_shell_sort(number_list):
    
    gap = len(number_list) // 2

    while gap > 0:
            
        for z in range(gap, gap*2):

            for i in range(z, len(number_list), gap):
        
                anchor = number_list[i]

                j = i - gap
        
                while j >= 0 and anchor < number_list[j]:
                    number_list[j + gap] = number_list[j]
                    j -= gap

                number_list[j + gap] = anchor

        gap = gap // 2


if __name__ == '__main__':
    nums_list = [70, 3, 1, 56, 34, 12, 9, 13, 80]

    my_implementation_of_shell_sort(nums_list)
    
    print(nums_list)
