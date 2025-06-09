def process_characters(char1, char2, char3, char4='d', char5='e'):
    print("Received characters:")
    print(f"Char1: {char1}")
    print(f"Char2: {char2}")
    print(f"Char3: {char3}")
    print(f"Char4: {char4}")
    print(f"Char5: {char5}")

print("Calling with 3 characters (c1, c2, c3):")
process_characters('a', 'b', 'c')

print("\nCalling with 4 characters (c1, c2, c3, c4):")
process_characters('x', 'y', 'z', 'w')

print("\nCalling with 5 characters (c1, c2, c3, c4, c5):")
process_characters('p', 'q', 'r', 's', 't')

