#!/usr/bin/env python
#
# roman_number.py
# Author: Zex <top_zlynch@yahoo.com>

#>>> getopt.getopt("-l 30 -h --color .".split(' '), 'l:h', "color")
# ([('-l', '30'), ('-h', ''), ('--color', '')], ['.'])

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
        print "to_arabic"
        pass #TODO
#        return reduce(lambda a,n: a+n, [RN[c] for c in in_str])

def roman_number(rnum):

    print "<label>Roman/Arabic Number: </label><p><span contenteditable=\"false\">"
   
    try:

        RomanNum.to_roman(int(rnum))

    except Exception as e:

        print e

        try:
            RomanNum.to_arabic(rnum)
        except Exception as e:
            print e

    print "</span></p>"


def reply():
    import cgi
    fields = cgi.FieldStorage()
    title = "Roman Number"
    
    print "Content-Type: text/html\n\n"
    print "<!DOCTYPE html>"
    print "<html>"
    
    print "<head>"
    print "<title>", title, "</title>"
    print "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    print "<meta charset=\"UTF-8\">"
    print "</head>"
    
    print "<body>"
    
    roman_number(fields["rnum"])
    
    print "</body>"
    print "</html>"

reply()
