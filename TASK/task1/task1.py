# sp = [5,8,9,True,"Hello"]
# for i , value in enumerate(sp):
#     print(i, value)

# ________________________
# def print_sp(sp: list):
#     for i,v in enumerate(sp):
#         print(f"{i=} - {v=}")
        
# sp = [5,8,9,True,"Hello"]
# s = "Hello"
# print_sp(sp)
# print_sp(s)
# 
# -----------------
# def print_sp(sp: list):
#     if not isinstance(sp, list):
#         raise ValueError("Нужен именно список!")
#     for i,v in enumerate(sp):
#         print(f"{i=} - {v=}")
        
# sp = [5,8,9,True,"Hello"]
# s = "Hello"
# print_sp(sp)
# try:
#     print_sp(s)
# except ValueError as e:
#     print(e)
#  _________________________   
    
# def print_sp(sp: list):
#     if not isinstance(sp, list):
#         print ("Нужен именно список!")
#         return
#     for i,v in enumerate(sp):
#         print(f"{i=} - {v=}")
        
# sp = [5,8,9,True,"Hello"]
# s = "Hello"
# print_sp(sp)

# ----------------------------------

def print_sp(sp: list):
    """
    cvcbch cbcvch cbchc cncjc
    """
    if not isinstance(sp, list):
        return
    for i,v in enumerate(sp):
        print(f"{i=} - {v=}")
        
sp = [5,8,9,True,"Hello"]
s = "Hello"
print_sp(s)
print(print_sp.__doc__)
