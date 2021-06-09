def groceries(product1,product2):
    vegetables=[]
    fruits=[]
    salad=product1+" "+product2     #The salad only needs to add the products passed to the parameters.
    if product1=="Mango" and product2=="Potato":  #Here we are checking if both conditions are met.
        fruits.append(product1)
        vegetables.append(product2)
        print(fruits)
        print(vegetables)
    print(f"I will make a {salad} salad with my groceries,A little mayo and corriander will add spice!")
groceries("Mango","Potato")

