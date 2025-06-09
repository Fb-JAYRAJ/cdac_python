def toggle_char_case(character):
    if 'a' <= character <= 'z':
        
        return chr(ord(character) - 32)
    elif 'A' <= character <= 'Z':
        
        return chr(ord(character) + 32)
    else: 
        return character 
    
char_input_q6 = input("Enter a single character to toggle its case: ")
if len(char_input_q6) == 1:
    toggled_char = toggle_char_case(char_input_q6)
    print(f"Original character: '{char_input_q6}', Toggled character: '{toggled_char}'")
else:
    print("Please enter only a single character.")
