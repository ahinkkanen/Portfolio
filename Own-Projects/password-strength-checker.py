import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Salasanasi on liian lyhyt tai se ei vastaa standardeja (vähintään 8 merkkiä).")
    elif len(password) >= 12:
        score += 2
        feedback.append("Salasanan pituus on erinomainen!")
    else:
        score += 1
        feedback.append("Pituus on riittävä, mutta 12+ merkkiä olisi parempi.")

    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Sisältää isoja kirjaimia: hyvä!")
    else:
        feedback.append("Lisää vielä isoja kirjaimia.")

    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Sisältää pieniä kirjaimia: hyvä!")
    else:
        feedback.append("Lisää pieniä kirjaimia.")

    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("Sisältää numeroita: hyvä!")
    else:
        feedback.append("Lisää numeroita.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("Sisältää erikoismerkkejä: hyvä!")
    else:
        feedback.append("Lisää erikoismerkkejä.")

    if password.lower() in ["salasana", "123456", "qwerty", "password"]:
        score = 0
        feedback.append("Salasana on liian yleinen ja turvaton!")

    if score >= 5:
        strength = "Vahva"
    elif score >= 3:
        strength = "Keskivahva"
    else:
        strength = "Heikko"

    return {"strength": strength, "score": score, "feedback": feedback}

password = input("Syötä salasana: ")
result = check_password_strength(password)

print(f"\nSalasanan vahvuus: {result['strength']}")
print(f"Pisteet: {result['score']}/6")
print("Palaute:")
for comment in result['feedback']:
    print(f"- {comment}")
