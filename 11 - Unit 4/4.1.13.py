def metasearch():
    import re
    p=re.compile('sing+')
    search1=re.match(p,'Some singers sing well')
    if search1:
        match=search1.group()
        index=search1.start()
        lindex=search1.end()
        print "matched", match, "at index", index ,"ending at", lindex
    else:
        print "No match found"
