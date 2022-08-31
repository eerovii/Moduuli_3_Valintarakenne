sukupuoli = input("Anna biologinen sukupuolesi: ")
hemoglobim = int(input("Anna hemoglobiiniarvosi: "))
if sukupuoli == "Mies":


    if  hemoglobim<134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobim>=134:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoglobim<=195:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoglobim>195:
        print("Hemoglobiiniarvosi on korkea.")

else:

     if hemoglobim<117:
        print("Hemoglobiiniarvosi on alhainen.")
     elif hemoglobim>=117:
        print("Hemoglobiiniarvosi on normaali.")
     elif hemoglobim<=175:
        print("Hemoglobiiniarvosi on normaali.")
     elif hemoglobim>175:
        print("Hemoglobiiniarvosi on korkea.")
