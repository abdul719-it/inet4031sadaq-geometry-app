# inspiration code for Python Unit Testing Project
import math
def surfaceArea():
    pass

def volumes(rad):
    volume = (4/3)*math.pi*rad*rad*rad
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    print("\The volume of a Sphere is ", volumes(radius))

if __name__ == '__main__':
    prompt()
