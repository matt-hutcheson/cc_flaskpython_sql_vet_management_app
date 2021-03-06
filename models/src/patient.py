from models.src.date_changer import check_checked_in

class Patient():
    def __init__(self, name, dob, type, breed, gender, status, vet=None, client=None, check_in_date=None, check_out_date=None, id=None):
        self.name = name
        self.dob = dob
        self.type = type
        self.breed = breed
        self.gender = gender
        self.status = status
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.checked_in = check_checked_in(check_in_date, check_out_date)
        self.id =id
        self.vet= vet
        self.client = client
        # self.treatments = []


    # def dob to age()

    # def age to dob()