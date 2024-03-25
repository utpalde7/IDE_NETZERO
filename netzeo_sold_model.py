var = 'Year,BUSINESS_ENTITY,Theatre,COUNTRY'
print(list(var.split(',')))
list_of_CAGRs_wanted= '0.06,0.05'
print([float(item) for item in list_of_CAGRs_wanted.split(',')])
 
print(bool('True'))