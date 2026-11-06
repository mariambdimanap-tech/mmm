import datetime

def main():
    # Пайдаланушының атын сұрау
    esim = input("Атыңызды енгізіңіз: ").strip()
    
    # Қазіргі күн мен уақытты анықтау
    kazirgi_uakhyt = datetime.datetime.now()
    uakhyt_matini = kazirgi_uakhyt.strftime("%d.%m.%Y %H:%M:%S")
    
    # Сәлемдесу және қазіргі уақытты шығару
    print(f"\nСәлеметсіз бе, {esim}!")
    print(f"Қазіргі уақыт пен күн: {uakhyt_matini}")

if __name__ == "__main__":
    main()
