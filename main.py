from pyscript import document

def check_country(e):
    country = {
        'ph': 'Philippines',
        'swtz': 'Switzerland',
        'jp': 'Japan',
        'usa': 'United States of America',
        'fr': 'France',
        'ger': 'Germany',
        'sg': 'Singapore',
        'cn': 'China'
    }
    
    country_code = document.getElementById('countries').value.lower().strip()
    country['ca'] = 'Canada'
    
    output_element = document.getElementById('output1')
    output_element.innerHTML = country.get(country_code, 'Country code not found')

def country_fidelity(e):
    fidelity = {
        'ph': 'Philippine',
        'swtz': 'Swiss',
        'jp': 'Japan',
        'usa': 'American',
        'fr': 'French',
        'ger': 'German',
        'sg': 'Singaporean',
        'cn': 'Chinese',
        'ca': 'Canadian'
    }
    
    country_code = document.getElementById('countries').value.lower().strip()
    output_element = document.getElementById('output1')
    output_element.innerHTML = fidelity.get(country_code, 'Nationality code not found')
