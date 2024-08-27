a = int( input("enter marks : "))

class InvalidMarks(Exception):
    def __init__(self,message):
        self.message= message


try:
    if 0 <= a <= 100:
        print(a)
    else:
        raise InvalidMarks("invalid Marks") 


except InvalidMarks as e:
    print(f"{e}")

except Exception as e:
    print(f"{e}")

finally:
    print("completed")

