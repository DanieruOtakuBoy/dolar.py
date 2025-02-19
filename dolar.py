import requests

import locale

from mastodon import Mastodon

locale.setlocale(locale.LC_ALL, 'es_VE.UTF-8')

access_token = 'QgpYOrKAZWYZbROlc1O-NWPs5xw8ee1OzMrSv5Mt4AU'
mastodon_url = 'https://vzla.masto.host/'

mastodon = Mastodon(
	access_token=access_token,
	api_base_url=mastodon_url
)

response1 = requests.get('https://pydolarve.org/api/v1/dollar?page=alcambio&monitor=bcv')
response2 = requests.get('https://pydolarve.org/api/v1/dollar?page=alcambio&monitor=enparalelovzla')
response3 = requests.get('https://pydolarve.org/api/v1/euro?page=criptodolar&monitor=bcv')
response4 = requests.get('https://pydolarve.org/api/v1/euro?page=criptodolar&monitor=enparalelovzla')

if response1.status_code & response2.status_code & response3.status_code & response4.status_code == 200:
	
	data1 = response1.json()
	data2 = response2.json()
	data3 = response3.json()
	data4 = response4.json()
	
	for item in data1:
		dolar_bcv = locale.format_string("%.2f", data1['price'], grouping=True)
		
	for item in data2:
		dolar_par = locale.format_string("%.2f", data2['price'], grouping=True)

	for item in data3:
		euro_bcv = locale.format_string("%.2f", data3['price'], grouping=True)
		
	for item in data4:
		euro_par = locale.format_string("%.2f", data4['price'], grouping=True)

		mensaje = (f"¡Hola, Fediverso!\n\nTipo de cambio en #Venezuela para el día de hoy.\n\n"
				f"Dólar = {dolar_bcv} Bs (BCV), {dolar_par} Bs (paralelo).\n"
				f"Euro = {euro_bcv} Bs (BCV), {euro_par} Bs (paralelo).\n"
				f"\nEsto es todo por ahora, hasta la próxima actualización.")

		mastodon.toot(mensaje)

		print("Toot enviado con éxito.")
		
		break
			
else:
	
	print("Error al obtener los datos de la API.")	
	
	