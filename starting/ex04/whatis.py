import sys
try :
    len = len(sys.argv)
    assert len <= 2, "more than one argument is provided"
    if len < 2 :
        exit()
    try:
        value = int(sys.argv[1])
    except Exception as e:
        assert  False , "argument is not an integer"
    print("I'm Odd." if  (value % 2) else "I'm Even.")

except AssertionError as msg:
    print (f"AssertionError: {msg}")