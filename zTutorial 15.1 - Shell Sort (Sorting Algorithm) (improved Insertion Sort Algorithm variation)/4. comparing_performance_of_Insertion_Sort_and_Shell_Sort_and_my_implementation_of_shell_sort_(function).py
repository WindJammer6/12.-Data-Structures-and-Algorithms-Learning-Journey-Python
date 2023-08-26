#To understand about Decorators and 'wrapped functions' that we will be using in this file,  please refer to the files
#'4.1. What_are_Decorators.txt' to '4.5. Excercise1_Decorators.py' in the 
#'Tutorial 12 - Binary Search (Searching Algorithm) and Linear Search (Searching Algorithm)' tutorial

#Importing the 'wrapped function' 'time_it' from 'time_it.py' (you can find this file in this tutorial's directory),
#so that we can add a Decorator (with the 'wrapped function''s name as the Decorator/'tag' ('@time_it')) to the 
#'insertion_sort', 'shell_sort' and 'my_own_implementation_of_shell_sort' functions to add/modify the functionalities 
#of these functions to be able to measure/track their own respective runtimes 


#////////////////////////////////////////////


#Comparing Insertion Sort Algorithm's code and Shell Sort Algorithm's code:
#Notice that the code implementing the Shell Sort and Insertion Sort Algorithm are almost looks identical. Shell Sort 
#effectively have a 'gap-ed' version of Insertion Sort within itself, where the '1's are replaced by the 'gap' variable
#(the code of this 'inner Insertion Sort' within the code implementing Shell Sort is marked out in the 'shell_sort' 
#function)


from time_it import time_it

#What this function does is that it implements Insertion Sort Algorithm.
#(from '2. insertion_sort_(function).py' in the 'Tutorial 15 - Insertion Sort (Sorting Algorithm)' tutorial)
@time_it
def insertion_sort(number_list):

    for i in range(1, len(number_list)):

        anchor = number_list[i]

        j = i - 1
 
        while j >= 0 and anchor < number_list[j]:
            number_list[j + 1] = number_list[j]
            j -= 1

        number_list[j + 1] = anchor


#What this function does is that it implements Shell Sort Algorithm.
#(from '2. shell_sort_(function).py')
@time_it
def shell_sort(number_list):

    gap = len(number_list)//2

    while gap > 0:


        #~~~(Start of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~
        
        for i in range(gap, len(number_list)):

            anchor = number_list[i]

            j = i - gap

            while j >= 0 and anchor < number_list[j]:
                number_list[j + gap] = number_list[j]
                j -= gap

            number_list[j + gap] = anchor

        #~~~(End of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~


        gap = gap // 2


#What this function does is that it is my own implementation of the Shell Sort Algorithm, based on the visualised 
#explanation from codebasics' video on the Shell Sort Algorithm
#(from '3. my_implementation_of_shell_sort_(function).py')

#I included this 'my_implementation_of_shell_sort' function just to prove that this code implementation indeed 
#works as a Shell Sort Algorithm based on its sorting time complexity, which should be identical to the 'shell_sort' 
#function's sorting time complexity
@time_it
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
    #Testing the 3 functions on a large (using a large list so can see a noticable time performance difference from
    #the 'time_it' decorator) unsorted List:
    large_unsorted_list = [6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769, 6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769]
    insertion_sort(large_unsorted_list)

    large_unsorted_list2 = [6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769, 6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769]
    shell_sort(large_unsorted_list2)

    large_unsorted_list3 = [6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769, 6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769]
    my_implementation_of_shell_sort(large_unsorted_list3)

    #Output:
        # insertion_sort took 10.04648208618164 milliseconds
        # shell_sort took 0.0 milliseconds
        # my_implementation_of_shell_sort took 0.0 milliseconds

    #(Notice that the 'shell_sort' function and 'my_implementation_of_shell_sort' function both takes roughly the 
    #same amount of time to execute the sorting process. Since 'shell_sort' function is guranteed to be implementing
    #the Shell Sort Algorithm, this is also proof that the ''my_implementation_of_shell_sort' function is an 
    #implementation of the Shell Sort Algorithm)

    #About the time performance of the Insertion Sort vs Shell Sort on a large unsorted List:
    #Notice that the Insertion Sort took much longer than the Shell Sort, which is proof that Shell Sort is a more
    #effective sorting algorithm and is an improved variation of the Insertion Sort



    #Testing the 3 functions on a large (using a large list so can see a noticable time performance difference from
    #the 'time_it' decorator) sorted list:
    large_sorted_list = [i for i in range(10001)]
    insertion_sort(large_sorted_list)

    large_sorted_list2 = [i for i in range(10001)]
    shell_sort(large_sorted_list2)

    large_sorted_list3 = [i for i in range(10001)]
    my_implementation_of_shell_sort(large_sorted_list2)

    #Output:
        # insertion_sort took 1.4710426330566406 milliseconds
        # shell_sort took 19.41990852355957 milliseconds
        # my_implementation_of_shell_sort took 19.716501235961914 milliseconds

    #(Notice that the 'shell_sort' function and 'my_implementation_of_shell_sort' function both takes roughly the 
    #same amount of time to execute the sorting process. Since 'shell_sort' function is guranteed to be implementing
    #the Shell Sort Algorithm, this is also proof that the ''my_implementation_of_shell_sort' function is an 
    #implementation of the Shell Sort Algorithm)

    #About the time performance of the Insertion Sort vs Shell Sort on a large sorted List:
    #Notice that surprisingly, when sorting a large sorted List, the Shell Sort took much longer than the Insertion
    #Sort.
      
    #The reason for this occurance is that sorting a (large) sorted List is a best sorting testcase,
    #-> and the Big O Notation of Time Complexity for a best case testcase for Insertion Sort is O(n), since if the 
    #   list to be sorted is already pre-sorted, then Insertion Sort will just need to iterate through the list once,
    #   without making any comparisons and shifting/swapping)
    #-> while that for Shell Sort is O(n log n) (a bit more complex to explain why exactly it is O(n log n), but 
    #   Shell Sort's Big O Notation of Time Complexity is definitely larger than O(n) due to the additional gap-ed 
    #   Insertion Sort iterations, on top of the last gap (1) iteration of the standard Insertion Sort in Shell 
    #   Sort, which will already by itself have a Big O Notation of Time Complexity of O(n))
     
     
    #Conclusion:
    #If a list is already pre-sorted, or have most of the larger elements already at the back of the unsorted List, 
    #the standard Insertion Sort will beat Shell Sort. 

    #However, in real life scenarios, unsorted input data are more likely to have their larger elements split 
    #evenly across the unsorted List like the larger unsorted List above, which is where Shell Sort proves to be
    #more time efficient than Insertion Sort
