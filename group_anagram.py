class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create an anagram dictionary 
        anagram_dict = {}
        
        # 1. Convert the string to sorted strings
        # 2. For the sorted strings check if they exists in the dictionary or not (create a value of list type for that string if it doesnt exists)
        # 3. If the string element already exists add it to the list of values
        for string_element in strs:
            # 1
            sorted_string = "".join(sorted(string_element))
            # 2
            if sorted_string not in anagram_dict:
                anagram_dict[sorted_string] = [string_element]
            # 3    
            else: 
                anagram_dict[sorted_string].append(string_element)
                
        answer_list = []
        
        # For all the values in the list of values add them to the answer list and return it    
        for values in anagram_dict.values():
            answer_list.append(values)

        return answer_list
