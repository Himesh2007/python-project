# Define a list of jumbled words for different fruits.
jumbled_list = [["oongoam", "angom", "mmanggo"], ["orrngea", "rangeo", "oorange"], ["anabaaa", "baanaaa", "ananab"]]

# Define a list of correctly spelled fruits.
correct_list = ["mango", "orange", "banana"]

# Iterate over the indices of the correct_list.
for i in range(len(correct_list)):
    # Get the correct fruit name for the current index.
    correct_item = correct_list[i]
    
    # Get the sublist of jumbled words corresponding to the current fruit.
    sublist = jumbled_list[i]
    
    # Iterate over each jumbled word in the sublist.
    for item in sublist:
        # Check if the length of the correct fruit name matches the length of the jumbled word.
        if len(correct_item) == len(item):
            # Check if the sorted characters of the correct fruit name match the sorted characters of the jumbled word.
            if sorted(correct_item) == sorted(item):
                # Print the correct fruit name and the matching jumbled word.
                print(correct_item, item)
                break  # Exit the loop once a match is found and move to the next correct fruit name.