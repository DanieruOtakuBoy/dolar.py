import requests
import datetime
import locale

from mastodon import Mastodon

locale.setlocale(locale.LC_ALL, 'es_VE.UTF-8')

access_token = 'token_de_mastodon'
mastodon_url = 'url_del_servidor_de_mastodon'

mastodon = Mastodon(
	access_token=access_token,
	api_base_url=mastodon_url
)

fecha = datetime.datetime.now()
dia = fecha.weekday()

if dia == 0:
    futuro = "El precio del dólar y el euro (BCV) para el día martes será de:"

if dia == 1:
    futuro = "El precio del dólar y el euro (BCV) para el día miércoles será de:"

if dia == 2:
    futuro = "El precio del dólar y el euro (BCV) para el día jueves será de:"

if dia == 3:
    futuro = "El precio del dólar y el euro (BCV) para el día viernes será de:"

if dia == 5 or dia == 6:
    futuro = "El precio del dólar y el euro (BCV) para la siguiente semana será de:"

response1 = requests.get('https://pydolarve.org/api/v1/dollar?page=criptodolar&monitor=bcv&format_date=default&rounded_price=false')
response2 = requests.get('https://pydolarve.org/api/v1/dollar?page=criptodolar&monitor=enparalelovzla&format_date=default&rounded_price=false')
response3 = requests.get('https://pydolarve.org/api/v1/euro?page=criptodolar&monitor=bcv&format_date=default&rounded_price=false')
response4 = requests.get('https://pydolarve.org/api/v1/euro?page=criptodolar&monitor=enparalelovzla')

if response1.status_code & response2.status_code & response3.status_code & response4.status_code == 200:
	
	data1 = response1.json()
	data2 = response2.json()
	data3 = response3.json()
	data4 = response4.json()

	for item in data1:
		dolar_bcv = locale.format_string("%.2f", data1['price_old'], grouping=True)
		
	for item in data2:
		dolar_par = locale.format_string("%.2f", data2['price'], grouping=True)

	for item in data3:
		euro_bcv = locale.format_string("%.2f", data3['price_old'], grouping=True)
		
	for item in data4:
		euro_par = locale.format_string("%.2f", data4['price'], grouping=True)

	for item in data2:
		time_bcv = data1['last_update']

	for item in data2:
		time_par = data4['last_update']

	for item in data1:
		tasa_d_bcv = data1['symbol']

	for item in data2:
		tasa_d_par = data2['symbol']

	for item in data3:
		tasa_e_bcv = data3['symbol']

	for item in data4:
		tasa_e_par = data4['symbol']

	for item in data1:
		dolar_fut = locale.format_string("%.2f", data1['price'], grouping=True)

	for item in data1:
		euro_fut = locale.format_string("%.2f", data3['price'], grouping=True)

		mensaje = (f"¡Hola, Fediverso!\n\nTipo de cambio en #Venezuela para el día de hoy.\n\n"
				f"Dólar = {dolar_bcv} Bs (BCV) {tasa_d_bcv} | {dolar_par} Bs (paralelo) {tasa_d_par}\n"
				f"Euro = {euro_bcv} Bs (BCV) {tasa_e_bcv} | {euro_par} Bs (paralelo) {tasa_e_par}\n"
                f"\n{futuro}\nDólar = {dolar_fut} Bs | Euro = {euro_fut} Bs.\n"
                f"\nFecha y hora de la última actualización:\nBCV = {time_bcv}\nEnParaleloVzla = {time_par}\n\nFuente: Criptodólar\n"
				f"\nEsto es todo por ahora, hasta la próxima actualización.")

		mastodon.toot(mensaje)

		print("Toot enviado con éxito.")
		
		break
			
else:
	
	print("Error al obtener los datos de la API.")	
	
