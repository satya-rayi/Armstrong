# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
        # initialize sum
        sum = 0

        # find the sum of the cube of each digit
        temp = num
        while temp > 0:
                digit = temp % 10
                sum += digit ** 3
                temp //= 10

        # display the result
        if num == sum:
                return True
        return False
