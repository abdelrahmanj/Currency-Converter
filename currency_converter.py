import requests

initial_currency = input("Please enter initial crrency! ")
target_currency = input("Please enter target crrency! ")
 

while True:
    try:
        amount = float(input("Please enter the amount: "))

    except:
        print("Please enter the numeric value") 
        continue

    if amount <= 0:
        print("The amount must be greater than 0")
        continue
    else:
        break 
     


url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={initial_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "91I1jX1g7w5e1hlSLsZOtdsF1YmbL3vl"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()
print(result["result"])

