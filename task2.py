# original_list = [1,2,3,4,5,6,7,8,9,10]
original_list = list(range(1,11))

new_list = original_list[:5]

reversed_new_list = new_list.copy()
reversed_new_list.reverse()

print('original list: ',original_list)
print("Extracted first five element: ",new_list)
print("Reversed extracted elements",reversed_new_list)
