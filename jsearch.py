#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
args = sys.argv



def highlightprint(string,col=(33,40)):
    #print a string with highlight, no newline
    ca,cb=col
    print("\033[1;"+str(ca)+";"+str(cb)+"m"+string+"\033[0m",end="")

def casechk(string,ignorecase):
    if ignorecase:
        return string.lower()
    else:
        return string

def highlightsubstring(mainstring,substring,ignorecase=False,col=(33,40),on=True):
    #print string with substring highlighted
    if not on:
        print(mainstring)
        return
    if casechk(substring,ignorecase) in casechk(mainstring,ignorecase):
        start = casechk(mainstring,ignorecase).find(casechk(substring,ignorecase))
        end = start+len(substring)
        print(mainstring[:start],end="")
        highlightprint(mainstring[start:end],col=col)
        highlightsubstring(mainstring[end:],substring,ignorecase=ignorecase,col=col)
    else:
        print(mainstring)

def paramchk(params,flag,noval=False, defvalue=None):
    #check is flag is in params, and return value
    value = defvalue
    if flag in params:
        pindex = params.index(flag)
        if not noval:
            if pindex+1 < len(params):
                value = params[pindex+1]
                params.pop(pindex+1)
        else:
            value = True        
        params.pop(pindex)
    return value

def usage():
    print("Usage:")
    print("{} -f <json_file> -s <search_string> [-i] [-h] [-k]".format(args[0]))
    print("{} -j <json_text> -s <search_string> [-i] [-h] [-k]".format(args[0]))
    print("-i ignore case")
    print("-h highlight search string")
    print("-k keys only")

def json_pathfind(jdata, searchstr, ignorecase=False, path="", highlight=False, keysonly=False):
    ic=ignorecase
    if isinstance(jdata,dict):
        for key in jdata:
            if casechk(searchstr,ic) in casechk(key,ic):
                highlightsubstring(path+"."+key,searchstr,ignorecase=ic, col=(32,40), on=highlight)
                json_pathfind(jdata[key], searchstr, ignorecase=ic, path=path+"."+key, highlight=highlight, keysonly=keysonly)
            else:
                json_pathfind(jdata[key], searchstr, ignorecase=ic, path=path+"."+key, highlight=highlight, keysonly=keysonly)
    elif isinstance(jdata,list):
        for i in range(len(jdata)):
            json_pathfind(jdata[i], searchstr, ignorecase=ic, path=path+"["+str(i)+"]", highlight=highlight, keysonly=keysonly)
    else: #if not list or dict assume it's a value, check as string.
        if not keysonly:
            if casechk(searchstr,ic) in casechk(str(jdata),ic):
                highlightsubstring(path+"="+str(jdata),searchstr,ignorecase=ic, on=highlight)


if __name__=="__main__":
    if len(args) < 2:
        print("needs args!")
        usage()
        sys.exit(1)
    
    infile=paramchk(args,"-f")
    if not infile:
        jtext=paramchk(args,"-j")
        if jtext:
            jdata = json.loads(jtext)
    else:
        with open(infile,"r") as f:
            jdata = json.load(f)
    
    if not jdata:
        usage()
        sys.exit(1)

    stringsearch=paramchk(args,"-s")
    if not stringsearch:
        usage()
        sys.exit(1)
    
    ignorecase=paramchk(args,"-i",noval=True,defvalue=False)
    highlight=paramchk(args,"-h",noval=True,defvalue=False)
    keysonly=paramchk(args,"-k",noval=True,defvalue=False)

    #at this point, jdata is our json to work on
    #stringsearch is the string to search for

    json_pathfind(jdata,stringsearch,ignorecase=ignorecase,highlight=highlight,keysonly=keysonly)
