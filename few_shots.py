few_shots = [
    {'Question' : "What is the price per case of Sprite 300ml CAN?",
     'SQLQuery' : "SELECT price_per_case FROM `tbl_product` WHERE product_name = 'Sprite' AND variant = '300ml CAN'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "750.0"},
    {'Question': "show unique product names",
     'SQLQuery':"SELECT DISTINCT product_name FROM tbl_product",
     'SQLResult': "Result of the SQL query",
     'Answer': "DIET COKE, FANTA, SPRITE, COCA-COLA, LIMCA, SCHWEPPES G ALE, SCHSODA, THUMS UP, TUP CH, KINLEY WATER"},
    {'Question': "What will be the price of 10 cases of Kinley water 1L?" ,
     'SQLQuery' : "SELECT (price_per_case * 10) as final_price FROM `tbl_product` WHERE product_name = 'Kinley water' AND variant='1L PET'",
     'SQLResult': "Result of the SQL query",
     'Answer': "1100.0"} ,
     {'Question' : "Which are all the varients available for product Fanta?",
      'SQLQuery': "SELECT variant FROM tbl_product WHERE product_name='Fanta'",
      'SQLResult': "Result of the SQL query",
      'Answer' : "300ML CAN, 300ML PET, 600ML PET, 1.25L PET, 2L PET"},
    {'Question': "i  want to buy 100 loose bottles of sprite 600 ml , how much amount should i have to pay?",
     'SQLQuery' : "SELECT (100 / no_of_pcs_per_case) * price_per_case AS amount_to_pay FROM tbl_product WHERE product_name = 'SPRITE' AND variant ='600ML PET'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "2583.33333292"
     },
    {'Question': "What are the promotions available for coca cola 600 ml having discount greater than 10 %?",
     'SQLQuery' : "SELECT op.promotion_info FROM tbl_order_promotion AS op INNER JOIN tbl_product AS p ON op.brand_id=p.brand_id WHERE p.product_name = 'COCA-COLA' AND p.variant ='600ML PET' AND op.discount >'10'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "Coca-Cola 1 Ltr PET X12, Coca-Cola 500 ml Pet X24"
     }

]

