import json

def new_filter(filter_,column_name,value):
    filter_ = json.loads(filter_)
    if isinstance(filter_,dict):
        filter_[column_name] = value
    else:
        filter2 ={}
        filter2['0'] = filter_
        filter2[column_name] = value
        filter_ = filter2
    return  json.dumps(filter_)