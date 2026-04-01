from modules.whois_lookup import whois_lookup
from rich.pretty import pprint

domain = input("Inserisci un dominio: ")
result = whois_lookup(domain)
pprint(result)