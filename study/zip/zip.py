days = ['Monday','Tuesday','Wednesday']
fruits = ['banana' , 'orange' , 'peach']
drinks = ['coffee', 'tea' ,"beer"]
desserts = ['tiramisu','ice cream' ,'pie','pudding']
for day , fruit , drink , dessert in zip(days ,fruits,drinks, desserts):
    print(f"{day} , {fruit} , {drink} , {dessert} ")
