from sqlalchemy import inspect
import datetime
from helpers.enum import Roles
import re

def serialize_model(obj, subitens=None):
   if obj is None:
       return None

   result = {}

   for c in inspect(obj).mapper.column_attrs:
       result[c.key] = converter_datetime(getattr(obj, c.key))
       if subitens is not None:
           for subitem in subitens:
               print(subitem)
               subitem = converter(subitem)
               if hasattr(obj, subitem):
                   result[subitem] = serialize_model(getattr(obj, subitem))

   return result


def serialize_model_list(itens, subitens=None):
   return list(map(lambda item: serialize_model(item, subitens), itens))

def converter_datetime(item):
   if isinstance(item, datetime.datetime):
       return item.__str__()
   else:
       return item

def remove_repeated(itens):
   l = []
   for i in itens:
       if i not in l:
           l.append(i)
   return l

def isNoneOrZero(value):
    return True if value == 0 or value == None else False

def check_email(email):
    email_regex = "[^@]+@[^@]+\.[^@]+"
    return re.search(email_regex, str(email)) != None

def check_cpf(cpf):
    cpf_mask_regex = "^\d{3}\.\d{3}\.\d{3}\-\d{2}$"
    cpf_no_mask_regex = "^\d{3}\d{3}\d{3}\d{2}$"
    return re.search(cpf_mask_regex, str(cpf)) != None or re.search(cpf_no_mask_regex, str(cpf)) != None
