AppNameSpace = []

def getCustAttr(p_id, p_attrName):
  v_key = 'cust' + ':' + p_id + ':' + p_attrName
  return(AppNameSpace[v_key])


def setCustAttr(p_id, p_attrName, p_value):
  v_key = 'cust' + ':' + p_id + ':' + p_attrName
  AppNameSpace[v_key] = p_value


