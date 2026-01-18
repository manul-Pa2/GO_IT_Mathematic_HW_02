from itertools import product

def check_access(is_employee, is_verified, is_premium, is_admin, is_banned):
    """
    Повертає словник доступів до секцій:
    Base, Premium, Admin, Secret
    """
    base = is_employee and is_verified and (not is_banned)

    premium = (is_employee or is_premium) and is_verified and (not is_banned)

    admin = is_admin and is_verified and (not is_banned)

    secret = (is_admin or (is_employee and is_premium)) and is_verified and (not is_banned)

    return {"Base": base, "Premium": premium, "Admin": admin, "Secret": secret}


def b(x: bool) -> int:
    """Друк булевих"""
    return int(bool(x))


def main():
    header = "Emp   Ver   Prem  Adm   Ban   | Base  Prem  Adm   Secr"
    print(header)
    print("-" * len(header))

    full_access_count = 0
    premium_not_base = []

    # (True/False)^5
    for is_employee, is_verified, is_premium, is_admin, is_banned in product([True, False], repeat=5):
        acc = check_access(is_employee, is_verified, is_premium, is_admin, is_banned)

        # Табличний рядок
        print(
            f"{b(is_employee):<5}{b(is_verified):<6}{b(is_premium):<6}{b(is_admin):<6}{b(is_banned):<6}"
            f"| {b(acc['Base']):<6}{b(acc['Premium']):<6}{b(acc['Admin']):<6}{b(acc['Secret']):<6}"
        )

        # Аналіз
        if all(acc.values()):
            full_access_count += 1

        if acc["Premium"] and not acc["Base"]:
            premium_not_base.append((is_employee, is_verified, is_premium, is_admin, is_banned, acc))

    print("\nАНАЛІЗ")
    print(f"1) Повний доступ до всіх 4 секцій: {full_access_count} випадків(в).")

    print("2) Premium=True, але Base=False — так, існує(ють) комбінація(ї):")
    for (emp, ver, prem, adm, ban, acc) in premium_not_base:
        print(
            f"   Emp={b(emp)} Ver={b(ver)} Prem={b(prem)} Adm={b(adm)} Ban={b(ban)}"
            f"  -> Base={b(acc['Base'])} Premium={b(acc['Premium'])} Admin={b(acc['Admin'])} Secret={b(acc['Secret'])}"
        )

    print("\nПояснення:")
    print("Base вимагає Emp=True (співробітник).")
    print("Premium вимагає (Emp=True АБО Prem=True).")
    print("Тому, якщо Emp=False, але Prem=True, а також Ver=True і Ban=False — Premium буде True, а Base залишиться False.")


if __name__ == "__main__":     # Дуже важке завдання, сподіваюсь ця реалізація підійде ^-^
    main()
