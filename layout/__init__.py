from data_processing import SanitizationData, DrinkingWaterData

sanitization_data = SanitizationData('data/atLeastBasicSanitizationServices_1.csv')
sanitization_data.load_data()
sanitization_df = sanitization_data.get_total_population_data()

water_data = DrinkingWaterData('data/basicDrinkingWaterServices.csv')
water_data.load_data()
water_df = water_data.get_data()
