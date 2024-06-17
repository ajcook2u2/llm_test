current_month = 1000
yoy_month = 500

spend_delta = (1000 - 500) / 500
spend_delta = round(spend_delta * 10000)
spend_delta = f'{spend_delta / 100}%'
print(spend_delta)