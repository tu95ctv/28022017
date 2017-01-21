def create_a_list_from_row_string(string):
    outs = string.split('\n')
    out_put = ','.join(['"' + x +'"' for x in outs if len(x)>0])
    return '[' + out_put + ']'
    

    
if __name__=="__main__":
    input = '''furnished
partly_furnished
unfurnished
'''
print create_a_list_from_row_string(input) 