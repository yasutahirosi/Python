'''!rm -rf latexify_py

!git clone https://github.com/odashi/latexify_py -b develop

!pip install -e latexify_py'''

import math
import latexify

@latexify.with_latex
def solve(a,b,c):
    return (-b+math.sqrt(b**2-4*a*c))/(2*a)

print(solve(1,4,3))
print(solve)
print()
solve
