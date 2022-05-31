def make_car(manufacturer, model_no, **car_info):
    carinfo = {}
    carinfo['Manufacturer'] = manufacturer
    carinfo['Model'] = model_no
    for key, value in car_info.items():
        carinfo[key] = value
    return carinfo



car = make_car("Mercedes-Benz", "Maybach GLS600 4MATIC", engine='4.0L Twin-Turbo V8 Gas', Transmission='9-Speed Automatic', Price='$160,500')
print(car)