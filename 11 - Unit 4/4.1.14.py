def find():
    import re
    p=re.compile('sing+')
    search1=p.findall('Some singer sing well')
    print search1
