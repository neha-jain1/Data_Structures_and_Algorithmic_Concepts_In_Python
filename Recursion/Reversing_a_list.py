
class reverse:
    def __init__(self):
        print("Reverse Class Object Created")

    def reverse_list(self,arr):

        #Base Case
        if(arr == []):
            return []

        #Calling the same function for a smaller array
        tmp_result = self.reverse_list(arr[1:])

        #Extracting the first element of the array
        first_element = arr[0:1]

        #Adding first element to the result returned
        result = tmp_result + first_element

        #Return Result
        return result

rev_obj = reverse()

arr = [1,2,3]
final_result = rev_obj.reverse_list(arr)
print(final_result)
    
        
        
