import requests

url = "https://sso.ui.com/api/sso/v1/user/self/picture"
# file_path = '/Users/sheenalu/Downloads/e13f0328-1849-43fc-9273-98d2fef4671e.png'
file_path = '/Users/sheenalu/Downloads/bath_time_giphy/200w-1.gif'
with open(file_path, 'rb') as file:
    image_data = file.read()

payload = image_data
headers = {
    'Content-Type': 'image/jpeg',
    'Cookie': 'UBIC_AUTH="fjIwMjIwNjA3fHFtZzBMSWZsN1lHN2JyNVpyamo1bXZvWWdDeUJIUlloek9NcjFJdHptdVhybXo5eWI2dEh1SUh2RUEwbUl1QTd6c2RkUGNmYXJqN0lvN0o3YkhwbXlmZ1lKenFGUEx2QTk0WGRIWkRKTU5LY2h0QnFZbXJ1Sk0wY3NhUTlZUFRTV0d1cGNqK0loOVZjMm8zL0tYZzNsRERJZUxTR3ZSbUM5UXpGL2wwOWc4b0FQTWwva3EwMTZ5bzFaRHVUK2pHVWFMVHFudFVrdWZqdjVLQTd6S2JDRTFnL2Y3c2ZTN3Q3L0Z6TDZaS1hVekIxVmVEVUNsanFpZkYycmpEbGIvZDdpQkh6Nml5djRtaUJuNjNydXhwR0JjRlRuWGdiY2todWMzVGVGS01SUnJvTjJRPT18OGpNTFEzQ29hSEdxbkE3aFlvQmcxbkZqL3JRPXxkeVhoQ3VwU24xYUtsL2NEa0FKTmJnPT18VE95WWhZOXdldVgzSE9EYWdXQ3hwKzJ1NHRFPQ=="'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
print(response.text)
