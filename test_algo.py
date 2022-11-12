
import joblib


def prediction(business_location,business_nature,business_product,filename='model.sav'):
    def clean(x):
        x = x.lower()
        x = x.strip('.')
        x = x.strip(' ')
        return x
    loaded_model = joblib.load('model.sav')

    sample = ['0', 'automative', 'automotive', 'balakong', 'bandar sunway', 'beauty',
           'damansara', 'direct sales', 'food & beverages',
           'household manufacturer', 'ipoh', 'johor', 'kajang', 'kedah',
           'kelana jaya', 'kelantan', 'kepong', 'klang', 'kuala lumpur',
           'kuala pumpur', 'pahang', 'pandan indah', 'penang', 'perak',
           'personal care manufacturer', 'pet food', 'pharmaceutical', 'puchong',
           'pulau pinang', 'rawang', 'selangor', 'seremban', 'seri kembangan',
           'setia alam', 'shah alam', 'subang jaya', 'trading', 'unknown',
           'Business product']
    print('Sample',len(sample))


    s1 = {}
    for i in sample:
        s1[f'{i}'] = 0
    print(s1)


    business_product = int(business_product)
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
    print('Prediction: ',loaded_model.predict(test_data))
    return loaded_model.predict(test_data)


if __name__ == '__main__':
    prediction()

# selangor, pet food, 3 # ['B002061']
# klang, beauty, 2 # ['B002079']
# klang, direct sales, 1 # ['CP01708']

