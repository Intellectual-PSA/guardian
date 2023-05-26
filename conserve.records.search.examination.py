class Patient:
    def __init__(self, name, age, conservator, condition):
        self.name = name
        self.age = age
        self.conservator = conservator
        self.condition = condition

class Conservatorship:
    def __init__(self):
        self.patients = []

    def add_patient(self, name, age, conservator, condition):
        patient = Patient(name, age, conservator, condition)
        self.patients.append(patient)
        print(f"Patient {name} added under the conservatorship of {conservator}.")

    def find_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                print(f"Patient {name} is under the conservatorship of {patient.conservator}.")
                return
        print(f"No patient found with name {name}.")

    def find_conservator_patients(self, conservator_name):
        found_patients = [patient for patient in self.patients if patient.conservator == conservator_name]
        if not found_patients:
            print(f"No patients found under the conservatorship of {conservator_name}.")
        else:
            print(f"Patients under the conservatorship of {conservator_name}: {[patient.name for patient in found_patients]}")

# Sample usage
if __name__ == "__main__":
    conservatorship = Conservatorship()

    conservatorship.add_patient("John Doe", 45, "Jane Doe", "Schizophrenia")
    conservatorship.add_patient("Emma Smith", 32, "Robert Smith", "Bipolar Disorder")
    conservatorship.add_patient("Mike Johnson", 38, "Jane Doe", "Depression")

    conservatorship.find_patient("John Doe")
    conservatorship.find_conservator_patients("Jane Doe")
