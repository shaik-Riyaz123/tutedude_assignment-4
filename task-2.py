text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")
text_to_append = input("\nEnter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
