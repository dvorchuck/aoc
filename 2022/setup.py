import sys

n = int(sys.argv[1])

print(n)

with open("template.py", "r") as template:
    # Read the contents of the template file
    template_contents = template.read()

# Open a new file for writing
with open(f"{n}.py", "w") as example:
    # Write the contents of the template file to the new file
    example.write(template_contents)


open(f"input_{n}.txt","w")