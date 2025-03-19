# give an input and return output increasing ascending order


class sorted_numbers:
    """ check for negative and positive number and merge the two list"""

    def sorted_squares(self, arr:list):
       negatives = [x for x in arr if x < 0]
       non_negatives = [x for x in arr if x >= 0]

       negatives_square_sorted = [x ** 2 for x in reversed(negatives)]
       non_negatives_square_sorted = [x ** 2 for x in non_negatives]

       return self.merge_list(negatives_square_sorted, non_negatives_square_sorted)


    def merge_list(self, negative:list, non_negative:list):

        """ Have pointer for each list and the element if it is smaller than 
        other element in second list"""

        l1 = l2=0

        res = []

        while l1 < len(negative) and l2< len(non_negative):

            if negative[l1] < non_negative[l2]:

                res.append(negative[l1])

                l1 += 1
            elif negative[l1] > non_negative[l2]:
                res.append(non_negative[l2])
                l2 += 1
            else:
                res.append(negative[l1])
                res.append(non_negative[l2])
                l1 += 1
                l2 += 1
        
        res.extend(negative[l1:])
        res.extend(non_negative[l2:])

        return res
input_str = input("Please enter a sorted array of integers (e.g. -9 -2 0 2 3): ")

arr = list(map(int, input_str.split()))
numbers = sorted_numbers()

print(numbers.sorted_squares(arr))

