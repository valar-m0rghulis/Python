

def check_baggage(baggage_weight):
    if baggage_weight >= 0 or baggage_weight <= 40:
        return True
    else:
        return False

def check_immigration(expiry_year):
    if expiry_year >= 2001 or expiry_year <= 2025:
        return True
    else:
        return False

def check_security(noc_status):
    if noc_status == "valid" or noc_status == "VALID":
        return True
    else:
        return False


traveler_id  = 1001
traveler_name = "Jim"
baggage_weight = 35
expiry_year = 2000
noc_status = "VALID"



if check_baggage(baggage_weight)is True and check_immigration(expiry_year)is True and check_security(noc_status)is True:
       print("Id =",traveler_id)
       print("Name = ",traveler_name)
       print("Allow Traveler to fly!")
else:
       print("Id =",traveler_id)
       print("Name = ",traveler_name)
       print("Detain Traveler for Re-checking!")
    

'''
OUTPUT :

Id = 1001
Name =  Jim
Allow Traveler to fly!

'''



