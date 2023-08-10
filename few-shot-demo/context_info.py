import json
context_info=json.dumps({
#   "u4600091001": {
#     "name": "Nancy",
#     "age": 21,
#     "Bad record": "defrauding",
#     "country":"China",
#     "orders": [
#       {
#         "order id": "o1168913416",
#         "order time": "2023-06-20 17:19:06",
#         "status": "Refund"
#       }
#     ]
#   },
  "u4600089016": {
    "name": "Albert",
    "age": 28,
    "Bad record": "None",
    "country":"India",
    "orders": [
      {
        "order id": "o1168501616",
        "order time": "2023-07-20 16:19:06",
        "status": "Received"
      },
      {
        "order id": "o1184708249",
        "order time": "2023-07-31 15:31:20",
        "status": "In transit"
      },
      {
        "order id": "o1184508116",
        "order time": "2023-08-10 09:18:26",
        "status": "In transit"
      },
      {
        "order id": "o1184508115",
        "order time": "2023-08-10 16:18:26",
        "status": "Not shipped" 
      }
    ]
  },
  "o1184508115": {
    "product": "Philips Hair Dryer",
    "price": "198 RMB",
    "location": "",
    "logistics track": "",
    "arrived time": "2023-08-13" 
  },
  "o1168913416": {
    "product": "Philips Hair Dryer",
    "price": "198 RMB",
    "location": "",
    "logistics track": "",
    "arrived time": "2023-06-25"
  },
  "o1168501616": {
    "product": "Philips Portable Vacuum Cleaner",
    "price": "388 RMB",
    "location": "Vancouver",
    "logistics track": "Toronto->Calgary->Vancouver",
    "arrived time": "2023-07-25"
  },
  "o1184708249": {
    "product": "Picasso Fountain Pen",
    "price": "198 RMB",
    "location": "Montreal",
    "logistics track": "Quebec City->Montreal",
    "estimated arrival time": "2023-08-09"
  },
  "o1184508116": {
    "product": "10Pcs/Set Fine Thin Hook Line Nylon Pen Paint Brush Drawing Art",
    "price": "598 RMB",
    "location": "Ottawa",
    "logistics track": "Winnipeg->Ottawa",
    "estimated arrival time": "2023-08-11"
  }


})