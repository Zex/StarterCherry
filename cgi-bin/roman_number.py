#!/usr/bin/env python
#
# roman_number.py
# Author: Zex <top_zlynch@yahoo.com>

#>>> getopt.getopt("-l 30 -h --color .".split(' '), 'l:h', "color")
# ([('-l', '30'), ('-h', ''), ('--color', '')], ['.'])

config = {}

class RomanNum():
    """
    Translate Rome number into Arabic one and vice versa.
    """
    RN = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    RN["II"]  = RN["I"] * 2
    RN["III"] = RN["I"] * 3
    RN["VV"]  = RN["V"] * 2
    RN["VVV"] = RN["V"] * 3
    RN["XX"]  = RN["X"] * 2
    RN["XXX"] = RN["X"] * 3
    RN["LL"]  = RN["L"] * 2
    RN["LLL"] = RN["L"] * 3
    RN["CC"]  = RN["C"] * 2
    RN["CCC"] = RN["C"] * 3
    RN["DD"]  = RN["D"] * 2
    RN["DDD"] = RN["D"] * 3
    RN["MM"]  = RN["M"] * 2
    RN["MMM"] = RN["M"] * 3

    @staticmethod
    def to_roman(in_num):
       
        AN = {v:k for k, v in RomanNum.RN.items()}
        ret = ''

        l = RomanNum.RN.values()
        l.sort()
        l.reverse()

        for d in l:

            if in_num/d == 0: continue

            continue #TODO
            ret += AN[d] * (in_num/d)
            in_num %= d

        return ret

    @staticmethod
    def to_arabic(in_str):
        ret += "to_arabic"
        return ret #TODO
#        return reduce(lambda a,n: a+n, [RN[c] for c in in_str])

def roman_number(rnum):

    ret = "<label>Roman/Arabic Number: </label><p><span contenteditable=\"false\">"
   
    try:

        ret += RomanNum.to_roman(int(rnum))

    except Exception as e:

        ret += str(e)

        try:
            ret += RomanNum.to_arabic(rnum)
        except Exception as e:
            ret += str(e)

    ret += "</span></p>"
    return ret

def reply(req, kwargs = {}):

    global config
    config = req.config

    title = "Roman Number"
    
    ret = "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<link href=\"/img/badsmile.jpg\" rel=\"icon\" type=\"image/jpg\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"
    
    ret += "<body>"
    ret += "<h2>Welcome, " + req.headers["Remote-Addr"] + "!</h2>"
    ret += "<span>" + req.headers["User-Agent"] + "</span><br>"
    
    ret += roman_number(kwargs["rnum"])
    
    ret += "</body>"
    ret += "</html>"

    return ret

