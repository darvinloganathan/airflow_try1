import pandas as pd
import numpy as np
import re

def check_even(x):
    if x % 2==0:
        return True
    else:
        return False
def check_even_column(data,column):
    x=data[column].apply(check_even)
    y=list(x)
    l=len(data)
    missing=data[column].isnull().sum()
    miss_per=(missing/l)*100
    unexpected_count=y.count(False)
    unexpected_percent=(unexpected_count/l)*100
    result={'result':{'element_count:': l,
                     'missing_count:': missing,
                     'missing_percent:': miss_per,
                      'unexpected_count:':unexpected_count,
                     'unexpected_percent:':unexpected_percent},
          'succes':x.all() }
    return(result)

def check_datatype(x,type1):
    if isinstance(x, (type1)):
        return True
    else:
        return False

def check_datatype_column(data,column,datatype):
    data['true']=data[column].apply(check_datatype,type1=datatype)
    y=list(data['true'])
    l=len(data)
    missing=data[column].isnull().sum()
    miss_per=(missing/l)*100
    unexpected_count=y.count(False)
    unexpected_percent=(unexpected_count/l)*100
    result={'result':{'element_count:': l,
                     'missing_count:': missing,
                     'missing_percent:': miss_per,
                      'unexpected_count:':unexpected_count,
                     'unexpected_percent:':unexpected_percent},
          'success':data['true'].all() }
    data=data[data['true'].isin([True])]
    return(result,data)

def in_range(num, s, e):
    if num >= s and num <= e:
        return True
    else:
        return False

def check_inrange_column(data,column,start,end):
    data['true']=data[column].apply(in_range,s=start,e=end)
    y=list(data['true'])
    l=len(data)
    missing=data[column].isnull().sum()
    miss_per=(missing/l)*100
    unexpected_count=y.count(False)
    unexpected_percent=(unexpected_count/l)*100
    result={'result':{'element_count:': l,
                     'missing_count:': missing,
                     'missing_percent:': miss_per,
                      'unexpected_count:':unexpected_count,
                     'unexpected_percent:':unexpected_percent},
          'success':data['true'].all() }
    data=data[data['true'].isin([True])]
    data.reset_index(inplace=True)
    data=data.drop(['true','index'],axis=1)
    return(result,data)

def is_in_list(value, lst):
    if value in lst:
        return True
    else:
        return False

def check_is_in_list_column(data,column,l1):
    data['true']=data[column].apply(is_in_list,lst=l1)
    y=list(data['true'])
    l=len(data)
    missing=data[column].isnull().sum()
    miss_per=(missing/l)*100
    unexpected_count=y.count(False)
    unexpected_percent=(unexpected_count/l)*100
    result={'result':{'element_count:': l,
                     'missing_count:': missing,
                     'missing_percent:': miss_per,
                      'unexpected_count:':unexpected_count,
                     'unexpected_percent:':unexpected_percent},
          'success':data['true'].all() }
    data=data[data['true'].isin([True])]
    data.reset_index(inplace=True)
    data=data.drop(['true','index'],axis=1)
    return(result,data)

def pattern1(x,p):
    try:
        pat = re.compile(p)
        if re.fullmatch(pat, x):
            return(True)
    except:
        return(False)

def check_pattern_column(data,column,pattern):
    data['true']=data[column].apply(pattern1,p=pattern)
    y=list(data['true'])
    l=len(data)
    missing=data[column].isnull().sum()
    miss_per=(missing/l)*100
    unexpected_count=y.count(False)
    unexpected_percent=(unexpected_count/l)*100
    result={'result':{'element_count:': l,
                     'missing_count:': missing,
                     'missing_percent:': miss_per,
                      'unexpected_count:':unexpected_count,
                     'unexpected_percent:':unexpected_percent},
          'success':data['true'].all() }
    data=data[data['true'].isin([True])]
    data.reset_index(inplace=True)
    data=data.drop(['true','index'],axis=1)
    return(result,data)

def check_duplicate_values(column):
    unique_values = set()
    result = []
    for value in column:
        if value in unique_values:
            result.append(False)
        else:
            unique_values.add(value)
            result.append(True)
    return result

def check_duplicate_col(data,columns):
    data['true']=check_duplicate_values(data[columns])
    y=list(data['true'])
    l=len(data)
    missing=data[columns].isnull().sum()
    miss_per=(missing/l)*100
    unexpected_count=y.count(False)
    unexpected_percent=(unexpected_count/l)*100
    result={'result':{'element_count:': l,
                     'missing_count:': missing,
                     'missing_percent:': miss_per,
                      'unexpected_count:':unexpected_count,
                     'unexpected_percent:':unexpected_percent},
          'success':data['true'].all() }
    data=data[data['true'].isin([True])]
    data.reset_index(inplace=True)
    data=data.drop(['true','index'],axis=1)
    return(result,data)

def check_notnull_col(data,columns):
    data['true']=data[columns].notnull()
    y=list(data['true'])
    l=len(data)
    missing=data[columns].isnull().sum()
    miss_per=(missing/l)*100
    unexpected_count=y.count(False)
    unexpected_percent=(unexpected_count/l)*100
    result={'result':{'element_count:': l,
                     'missing_count:': missing,
                     'missing_percent:': miss_per,
                      'unexpected_count:':unexpected_count,
                     'unexpected_percent:':unexpected_percent},
          'success':data['true'].all() }
    data=data[data['true'].isin([True])]
    #print(len(data))
    data.reset_index(inplace=True)
    data=data.drop(['true','index'],axis=1)
    return(result,data)

def mat_fun(x,c2,vc,fun):
    if fun=='*':
        if x*c2==vc:
            return True
        else:
            return False
    if fun=='/':
        if x/c2==vc:
            return True
        else:
            return False
    if fun=='-':
        if x-c2==vc:
            return True
        else:
            return False
    if fun=='+':
        if x+c2==vc:
            return True
        else:
            return False

def math_rule(data,column1,column2,column3,f):
    data['true']=data.apply(lambda x: mat_fun(x[column1],x[column2],x[column3],f),axis=1 )
    y=list(data['true'])
    l=len(data)
    missing=data[column3].isnull().sum()
    miss_per=(missing/l)*100
    unexpected_count=y.count(False)
    unexpected_percent=(unexpected_count/l)*100
    result={'result':{'element_count:': l,
                     'missing_count:': missing,
                     'missing_percent:': miss_per,
                      'unexpected_count:':unexpected_count,
                     'unexpected_percent:':unexpected_percent},
          'success':data['true'].all() }
    data=data[data['true'].isin([True])]
    data.reset_index(inplace=True)
    data=data.drop(['true','index'],axis=1)
    return(result,data)