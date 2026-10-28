# Question:3 :-
# If cost price and selling price of an item of an item is input throigh the keyword,
# write a program to determine whether the seller has made a profit or incurred loss or no 
# no profit or no loss. Also determine how much profiy he made or loss he incured. 

# CP=5 , SP=10 if sp>co -> profit= sp-cp , else sp<cp -> loss = cp-sp
cost_price = int(input("Enter the cost price:"))
sell_price = int(input("Enter the sell price :"))

# checking profit or loss or equal
if sell_price>cost_price:
    profit = sell_price - cost_price
    print("Profit is :", profit)
elif sell_price<cost_price:
    loss = cost_price - sell_price
    print("loss is :", loss)
else:
    print("no profit no loss")
    
# 2. conitional statement elif :- else-if :- used when there is more than one condition
        #    syntex :
        #         if condtion1 :
        #             statement 1
        #         elif condition 2:
        #              statement 2
        #         else:
        #             statment 3