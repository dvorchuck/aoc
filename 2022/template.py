import os

DAY = os.path.basename(__file__).replace('.py', '')
input = open(f"input_{DAY}.txt").read()

input_v2 = input.split('\n')
input_size = {
    "rows": len(input_v2),
    "cols": len(input_v2[0])
}


