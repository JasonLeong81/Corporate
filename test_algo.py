loaded_model = joblib.load(filename)

sample = ['0', 'automative', 'automotive ', 'balakong', 'bandar sunway', 'beauty',
       'damansara', 'direct sales', 'food & beverages',
       'household manufacturer', 'ipoh', 'johor', 'kajang', 'kedah',
       'kelana jaya', 'kelantan', 'kepong', 'klang', 'kuala lumpur',
       'kuala pumpur', 'pahang ', 'pandan indah', 'penang', 'perak',
       'personal care manufacturer', 'pet food', 'pharmaceutical',
       'pharmaceutical ', 'puchong', 'pulau pinang', 'rawang', 'selangor',
       'selangor ', 'seremban', 'seri kembangan', 'setia alam', 'shah alam',
       'subang jaya', 'trading', 'unknown', 'Business product']

s1 = {}
for i in sample:
    s1[f'{i}'] = 0
print(s1)



business_location = input('Enter your location: ')
business_nature = input('Enter your business nature: ')
business_product = int(input('Enter your business product (0-4): '))

business_location = clean(business_location)
business_nature = clean(business_nature)


if business_location in s1:
    s1[business_location] += 1
else:
    print('Location not found, resorting to default values.')
if business_nature in s1:
    s1[business_nature] += 1
else:
    print('Business Nature not found, resorting to default values.')
if 0 <= business_product <= 4:
    s1['Business product'] = business_product
else:
    print('Business product needs to be between 0-4 (inclusive).')

test_data = [list(s1.values())]
print(loaded_model.predict(test_data))

# selangor, pet food, 3 # ['B002061']
# klang, beauty, 2 # ['B002079']
# klang, direct sales, 1 # ['CP01708']

