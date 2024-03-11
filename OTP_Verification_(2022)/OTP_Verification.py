import math
import random

def generateOTP():
    digits = "0123456789"
    OTP = ""

    for i in range(5):
        OTP += digits[math.floor(random.random()*10)]
    return OTP

if __name__ == "__main__":
    print("OTP of 5 digits :",generateOTP())


