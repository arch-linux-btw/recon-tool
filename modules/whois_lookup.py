import whois

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return {
            "domain": w.domain_name,
            "registrar": w.registrar,
            "creation_date": w.creation_date,
            "expiration_date": w.expiration_date,
            "name_servers": w.name_servers,
        }
    except Exception as e:
        return {"error": str(e)}