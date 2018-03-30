def get_contents():
    contents = []
    while True:
        data = input("(Enter to quit)>")
        if not data:
            break
        contents.append(data)
    return contents

def format(lines):
    width = 48
    print ("*%s*" % ('*' * width))
    for line in lines:
        sp_wid,extra = divmod((width - len(line)),2)
        print ("*%s%s%s*" % (' ' * sp_wid,line,' ' * (sp_wid + extra)))
    print ("*%s*" % ('*' * width))