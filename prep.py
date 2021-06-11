from datetime import datetime
def time():
    now=datetime.now()
    # now.strftime("%c")
    print(now.strftime("%c"))
time()
#Exception... syntax is correct but execution is impossible.