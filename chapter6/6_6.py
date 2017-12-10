def days_in_month(mname):
    if mname=="January" or mname=="March"or mname=="May"or mname=="July" or mname=="August"or mname=="Octber"or mname=="December":
        return 31
    elif mname=="Feburary":
        return 28
    else:
        return 30