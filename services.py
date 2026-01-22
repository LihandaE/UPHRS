from database import get_connection

def register_patient(patient):
    conn=get_connection()
    cur= conn.cursor()

    cur.execute(
        "INSERT INTO patients VALUES (?, ?, ?, ?)",
        (patient.id, patient.name, patient.dob, patient.gender)
    )

    cur.execute(
        "INSERT INTO consent VALUES (?, ?)",
        (patient.id, 0)
    )

    conn.commit()
    conn.close()
    return patient.id


def grant_consent(patient_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE consent SET allowed = 1 WHERE patient_id = ?", (patient_id,))
    conn.commit()
    conn.close()

def add_medical_record(record):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO medical_records (patient_id, diagnosis, visit_date, facility) VALUES (?, ?, ?, ?)",
        (record.patient_id, record.diagnosis, record.visit_date, record.facility)
    )
    conn.commit()
    conn.close()

def get_patient_history(patient_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT allowed FROM consent WHERE patient_id = ?", (patient_id,))
    consent = cur.fetchone()

    if not consent or consent[0] == 0:
        return {"error": "Access denied. Patient consent required."}

    cur.execute("SELECT diagnosis, visit_date, facility FROM medical_records WHERE patient_id = ?", (patient_id,))
    records = cur.fetchall()

    cur.execute("SELECT drug_name, dosage, start_date, end_date FROM medications WHERE patient_id = ?", (patient_id,))
    meds = cur.fetchall()

    conn.close()

    return {
        "medical_records": records,
        "medications": meds}