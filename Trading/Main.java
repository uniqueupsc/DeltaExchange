// Login 
import sys; sys.path.insert(0,r"E:\\DExchange\\");
from Trading.SourceData.Login import Login
from Trading.SourceData.Source import api,sec
delta_client = Login("https://api.india.delta.exchange",api,sec);
print(delta_client);


# get mark_price
product_id                    = delta_client.get_ticker("BTCUSD")['mark_price']
print(product_id)



# get product_id
product_id                    = delta_client.get_ticker("BTCUSD")['product_id']
print(product_id)

# get Assets
response = delta_client.get_assets();
response

# Order book of Assets
print(delta_client.get_l2_orderbook(product_id))


## get position of product
response = delta_client.get_position(product_id)
print(response)
#{'entry_price': '95100.00000000', 'size': -1}  --> negative means sell; Entry -- none means No Open Position; positive means Buy
# {'entry_price': None, 'size': 0}




## For placing Order using api
order_response = delta_client.place_order(
          product_id          =         product_id,
          size                =         1,
          side                =         'buy',
          limit_price         =         '92000.0',
          order_type          =         OrderType.MARKET
    )

print(order_response)



## for Placing Stop Loss 
order_response = delta_client.place_stop_order(
        product_id      =   product_id,
        size            =   1,
        side            =   'sell',
        order_type      =   OrderType.MARKET,
        stop_price      =   '95400',
    )
print(order_response)




