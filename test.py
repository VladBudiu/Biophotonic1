# Import the raytracing library (assuming it's properly installed or the extracted path is accessible)
import sys
sys.path.append('/mnt/data/raytracing_library')

from raytracing import *

TITLE = "Virtual image at -f with object at f/2"
DESCRIPTION = """
With an object midway between the focus and the lens, we obtain a virtual 
image at the front focal plane (d=-f to the left of the lens).
The exact position can be obtained with path.forwardConjugate(), which
will return the distance (from the end of the path) and the transfer matrix
to that point. That transfer matrix is necessarily an imaging matrix (B=0).
"""

def exampleCode(comments=None):
    path = ImagingPath()
    path.label = TITLE
    path.append(Space(d=100))
    path.append(Lens(f=50))
    path.append(Space(d=200))
    distance, transferMatrix = path.forwardConjugate()
    print(distance, transferMatrix)
    path.display(comments=comments)

# Call the exampleCode function
exampleCode()
