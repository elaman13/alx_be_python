userWeather = input("What\'s the weather like today? (sunny/rainy/cold): ")

if userWeather == 'sunny':
    print('Wear a t-shirt and sunglasses.')
elif userWeather == 'rainy':
    print('Don\'t forget your umbrella and raincoat')
elif userWeather == 'cold':
    print('Make sure to wear a warm coat and scarf.')
else:
    print('Sorry, I don\'t have recommendations for this weather.')