
def check_baggage(baggage_weight):
    try:
        if(baggage_weight >= 0 and baggage_weight < 40):
            return True
        else:
            return False
    except TypeError:
        print("INVALID baggage weight entered")
def check_immigration(expiry_year):
    try:
        if(expiry_year >= 2001 and expiry_year <= 2025):
            return True
        else:
            return False
    except TypeError:
        print("INVALID expiry year entered")
def check_security(noc_status):
    try:
        if(noc_status == 'VALID' or noc_status == 'valid'):
            return True
        else:
            return False
    except TypeError:
        print("INVALID noc_status entered")
def traveler():
    traveler_id = 1001
    traveler_name = "Jhon"
    try:
        if(check_baggage(39) and check_immigration(2019) and check_security("VALID")):
            print(traveler_id,traveler_name)
            print("Allow Traveller to Fly!")
        else:
            print(traveler_id,traveler_name)
            print("Detain Traveller for re-checking.")
    except TypeError:
        print("INVALID values entered")
    except ValueError:
        print("INVALID values entered")
traveler()


'''
OUTPUT :

1001 Jhon
Allow Traveller to Fly!

1002 Jhon
Detain Traveller for re-checking.

'''
