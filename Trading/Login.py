# from delta_rest_client import DeltaRestClient
from enum import Enum

class OrderSide(Enum):
          BUY   = 'buy'
          SELL  = 'sell'

def Login(DI_URL,DIHED_KEY,DIHED_SECRET):
          from delta_rest_client import DeltaRestClient
          delta_client = DeltaRestClient(
                    base_url          =         DI_URL,
                    api_key           =         DIHED_KEY,
                    api_secret        =         DIHED_SECRET
                    )
          return delta_client


def PlacemarketOrder(delta_client , product_id,lots,side,limit_price = 0):
          from delta_rest_client        import OrderType

          if limit_price == 0:
                  order_type            =         OrderType.MARKET;
          else:
                  order_type            =         OrderType.LIMIT;
                  
          
          order_response = delta_client.place_order(
                              product_id          =         product_id,
                              size                =         lots,
                              side                =         side,
                              limit_price         =         limit_price,
                              order_type          =         order_type
                    );
          return order_response;
# PlacemarketOrder(delta_client,product_id,1,OrderSide.BUY.value);

def SquareOffOrder(delta_client,product_id, lots = 0):
          from delta_rest_client        import OrderType
          order_type                    =         OrderType.MARKET;
          
          response = delta_client.get_position(product_id); # {'entry_price': '95890.00000000', 'size': 1}
          print(response)
          ## running
          if response['size'] == 0:
                  return 'No Entry Positions';

          if response['size'] > 0:
                    side      = OrderSide.SELL.value;
          else:
                    side      = OrderSide.BUY.value;
          
          if lots == 0 or lots > response['size']:
                  lots = response['size'];

          LastRest = PlacemarketOrder(delta_client,product_id,lots,side);
          return LastRest;



