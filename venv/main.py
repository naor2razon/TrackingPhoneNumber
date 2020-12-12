import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from Phone_Number import number

ch_number = phonenumbers.parse(number,"CH")
print("The Phone location is: ")
print(geocoder.description_for_number(ch_number,"en"))

service_number = phonenumbers.parse(number,"RO")
print("The service provider is: ")
print(carrier.name_for_number(service_number,"en"))
