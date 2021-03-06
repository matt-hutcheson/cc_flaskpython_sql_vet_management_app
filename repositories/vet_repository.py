from db.run_sql import run_sql

from models.src.vet import Vet
from models.src.patient import Patient
from models.src.client import Client

def save(vet):
    sql = "INSERT INTO vets (first_name, last_name, job_title) VALUES (%s, %s, %s) RETURNING *"
    values = [vet.first_name, vet.last_name, vet.job_title]
    results = run_sql(sql, values)
    if results is not None:
        vet.id = results[0]['id']
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    if results is not None:
        for row in results:
            vet = Vet(row["first_name"], row["last_name"], row["job_title"], row["id"])
            vets.append(vet)
    return vets

def select(id):
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results is not None:
        result = results[0]
        vet = Vet(result["first_name"], result["last_name"], result["job_title"], result["id"])
    return vet

def select_patients(vet_id):
    import repositories.client_repository as client_repository
    patients = []
    sql = "SELECT * FROM patients WHERE vet_id = %s"
    values = [vet_id]
    results = run_sql(sql, values)
    if results is not None:
        for row in results:
            vet = select(vet_id)
            client = client_repository.select(row['client_id'])
            patient = Patient(row['name'], row['dob'], row['type'], row['breed'], row['gender'], row['status'], vet, client, row['check_in_date'], row['check_out_date'], row['id'])
            patients.append(patient)
    return patients

def select_clients(vet_id):
    clients = []
    sql = "SELECT * FROM clients WHERE vet_id = %s"
    values = [vet_id]
    results = run_sql(sql, values)
    if results is not None:
        for row in results:
            vet = select(vet_id)
            client = Client(row['first_name'], row['last_name'], row['phone_number'], row['address'], row['registered'], vet, row['id'])
            clients.append(client)
    return clients

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(vet):
    sql = "UPDATE vets SET (first_name, last_name, job_title) = (%s, %s, %s) WHERE id = %s"
    values = [vet.first_name, vet.last_name, vet.job_title, vet.id]
    run_sql(sql, values)

# select_clients(id)

# select_patients(id)
