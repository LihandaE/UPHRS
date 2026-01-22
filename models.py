import uuid

class Patient:
    def __init__(self, name, dob, gender):
        self.id = str(uuid.uuid1())
        self.name = name
        self.dob = dob
        self.gender = gender

class Medical_Record:
    def __init__(self, patient_id, diagnosis, date_of_visit, facility):
        self.patient_id = patient_id
        self.diagnosis = diagnosis
        self.date_of_visit = date_of_visit
        self.facility =facility

class Medication:
    def __init__(self, patient_id, drug_name, dosage, start_date, end_date):
        self.patient_id =patient_id
        self.drug_name =drug_name
        self.dosage = dosage
        self.start_date =start_date
        self.end_date =end_date
