def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal1 spam"
    
    def do_global():
        global spam
        spam = "global spam 1"
    spam = "test spam"
    do_local()
    # local nên không thể thay đổi giá trị của spam nên vẫn dữ nguyên giá trị của spam là test spam
    print("After local assignment:", spam)
    # nonlocal thay đổi giá trị của spam từ test spam thành nonlocal1 spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    #sau khi thực hiện do_global thì giá trị của spam đã thay đổi từ nonlocal1 spam thành global spam 1 và nó in ra giá trị này
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)