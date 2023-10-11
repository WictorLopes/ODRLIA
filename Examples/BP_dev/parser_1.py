import json
with open('C:\\Users\\amal\\Google Drive\\Projet Business Process\\project\\Credit applicat\\exam\\exam.json') as f:
  data = json.load(f)
if " permission " in data :
    if " includedIn " in data[" permission "][0][" action "][0]:
        print("exist")
        print(data[" permission "][0][" action "][0][" includedIn "])
        nb_BU = len((data[" permission "][0][" action "][0][" includedIn "]))
        print(nb_BU)
        for i in list(range(nb_BU)):
            print(i)
            print(range(nb_BU - 1))
            fich = "C:\\Users\\amal\\Google Drive\\Projet Business Process\\project\\Credit applicat\\exam\\BU_" + str(i) + ".bnf"
            with open(fich, "w") as fichier:
                fichier.write("{\"uid\": ")
                fichier.write(fich)
                fichier.write("\n")
                fichier.write("\"res\":")
                target = data[" permission "][0][" target "]
                fichier.write("[{")
                fichier.write(target)
                fichier.write("}]")
                fichier.write("\n")
                fichier.write("\"ext-op\": [{")
                fichier.write("\n")

                fichier.write('    "name":')
                nameop = str(data[" permission "][0][" action "][0][" includedIn "][i][" rdf : value "][" @id "])
                name_op = nameop.replace(" odrl : ", "")
                fichier.write(name_op)



                if " refinement " in data[" permission "][0][" action "][0][" includedIn "][i]:
                    fichier.write(',')
                    fichier.write("\n")
                    fichier.write('    " pre ": " cond ": [{')
                    # constraint

                    loprd = data[" permission "][0][" action "][0][" includedIn "][i][" refinement "][0][" leftOperand "]
                    opd = data[" permission "][0][" action "][0][" includedIn "][i][" refinement "][0][" operator "]
                    roprd = data[" permission "][0][" action "][0][" includedIn "][i][" refinement "][0][" rightOperand "][" @value "]

                    if str(loprd) == " timeInterval ":
                        fichier.write(' timeInterval ')
                    if str(loprd) == " spatial ":
                        fichier.write(' location ')
                    if str(loprd) == " payAmount ":
                        fichier.write(' budget ')
                    if str(loprd) == " dateTime ":
                        fichier.write(' time ')
                    if str(loprd) == " count " or str(loprd) == " delayPeriod ":
                        fichier.write(' frequency ')
                    # terminer ici les autres left operande ODRl
                    if str(opd) == " eq ":
                        fichier.write(' = ')
                    if str(opd) == " iteq ":
                        fichier.write(' <= ')
                    if str(opd) == " gteq ":
                        fichier.write(' >= ')
                    if str(opd) == " gt ":
                        fichier.write(' > ')
                    if str(opd) == " it ":
                        fichier.write(' < ')

                    fichier.write(str(roprd))

                    for j in list(range(1, len(data[" permission "][0][" action "][0][" includedIn "][i][" refinement "]))):
                        fichier.write(" and ")
                        leftopr = data[" permission "][0][" action "][0][" includedIn "][i][" refinement "][j][" leftOperand "]
                        oper = data[" permission "][0][" action "][0][" includedIn "][i][" refinement "][j][" operator "]
                        rightopr = data[" permission "][0][" action "][0][" includedIn "][i][" refinement "][j][" rightOperand "][" @value "]
                        print(leftopr)
                        print(oper)
                        print(rightopr)

                        if str(leftopr) == " timeInterval ":
                            fichier.write(' timeInterval ')


                        if str(leftopr) == " spatial ":
                            fichier.write('location')
                        if str(leftopr) == " payAmount ":
                            fichier.write('budget')
                        if str(leftopr) == " dateTime ":
                            fichier.write('time')
                        if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                            fichier.write('frequency')
                        # terminer ici les autres left operande ODRl
                        if str(oper) == " eq ":
                            fichier.write(' = ')
                        if str(oper) == " iteq ":
                            fichier.write(' <= ')
                        if str(oper) == " gteq ":
                            fichier.write(' >= ')
                        if str(oper) == " gt ":
                            fichier.write(' > ')
                        if str(oper) == "it":
                            fichier.write(' < ')

                        fichier.write(str(rightopr))
                    if " constraint " in data[" permission "][0]:
                        for j in list(range(len(data[" permission "][0][" constraint "]))):
                            fichier.write(" and ")
                            leftopr = data[" permission "][0][" constraint "][j][" leftOperand "]
                            oper = data[" permission "][0][" constraint "][j][" operator "]
                            rightopr = data[" permission "][0][" constraint "][j][" rightOperand "][" @value "]
                            print(leftopr)
                            print(oper)
                            print(rightopr)

                            if str(leftopr) == " timeInterval ":
                                fichier.write(' timeInterval ')

                            if str(leftopr) == " spatial ":
                                fichier.write(' location ')
                            if str(leftopr) == " payAmount ":
                                fichier.write(' budget ')
                            if str(leftopr) == " dateTime ":
                                fichier.write(' time ')
                            if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                                fichier.write(' frequency ')
                            # terminer ici les autres left operande ODRl
                            if str(oper) == " eq ":
                                fichier.write(' = ')
                            if str(oper) == " iteq ":
                                fichier.write(' <= ')
                            if str(oper) == " gteq ":
                                fichier.write(' >= ')
                            if str(oper) == " gt ":
                                fichier.write(' > ')
                            if str(oper) == "it":
                                fichier.write(' < ')

                            fichier.write(str(rightopr))
                    fichier.write("}]")  # fermeture de pre:cond de constraint
                else: # pas de refinement
                    if " constraint " in data[" permission "][0]:
                        print("yeeeeeeeeeeesss")
                        fichier.write(',')
                        fichier.write("\n")

                        fichier.write('    " pre ": " cond ": [{')
                        # constraint

                        leftopr = data[" permission "][0][" constraint "][0][" leftOperand "]
                        oper = data[" permission "][0][" constraint "][0][" operator "]
                        rightopr = data[" permission "][0][" constraint "][0][" rightOperand "][" @value "]
                        print(leftopr)
                        print(oper)
                        print(rightopr)

                        if str(leftopr) == " timeInterval ":
                            fichier.write(' timeInterval ')
                        if str(leftopr) == " spatial ":
                            fichier.write('location')
                        if str(leftopr) == " payAmount ":
                            fichier.write('budget')
                        if str(leftopr) == " dateTime ":
                            fichier.write('time')
                        if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                            fichier.write('frequency')
                        # terminer ici les autres left operande ODRl
                        if str(oper) == " eq ":
                            fichier.write(' = ')
                        if str(oper) == " iteq ":
                            fichier.write(' <= ')
                        if str(oper) == " gteq ":
                            fichier.write(' >= ')
                        if str(oper) == " gt ":
                            fichier.write(' > ')
                        if str(oper) == " it ":
                            fichier.write(' < ')

                        fichier.write(str(rightopr))

                        for j in list(range(1, len(data[" permission "][0][" constraint "]))):
                            fichier.write(" and ")
                            leftopr = data[" permission "][0][" constraint "][j][" leftOperand "]
                            oper = data[" permission "][0][" constraint "][j][" operator "]
                            rightopr = data[" permission "][0][" constraint "][j][" rightOperand "][" @value "]
                            print(leftopr)
                            print(oper)
                            print(rightopr)

                            if str(leftopr) == " timeInterval ":
                                fichier.write(' timeInterval ')


                            if str(leftopr) == " spatial ":
                                fichier.write(' location ')
                            if str(leftopr) == " payAmount ":
                                fichier.write(' budget ')
                            if str(leftopr) == " dateTime ":
                                fichier.write(' time ')
                            if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                                fichier.write('frequency')
                            # terminer ici les autres left operande ODRl
                            if str(oper) == " eq ":
                                fichier.write(' = ')
                            if str(oper) == " iteq ":
                                fichier.write(' <= ')
                            if str(oper) == " gteq ":
                                fichier.write(' >= ')
                            if str(oper) == " gt ":
                                fichier.write(' > ')
                            if str(oper) == " it ":
                                fichier.write(' < ')

                            fichier.write(str(rightopr))
                        fichier.write("}]")  # fermeture de pre:cond de constraint

                fichier.write(",")  # fermeture de pre:cond
                fichier.write("\n")
                fichier.write('    " rel ": [{')
                fichier.write("\n")
                fichier.write('      "type ": precedes,')
                fichier.write("\n")
                fichier.write('      "op": [{')
                fichier.write("\n")
                fichier.write('          " name ":')
                nameopint = str(data[" permission "][0][" action "][0][" rdf : value "][" @id "])
                name_opint = nameopint.replace(" odrl : ", "")
                fichier.write(name_opint)

                # s'il y a des refinement
                if " refinement " in data[" permission "][0][" action "][0]:
                    fichier.write(',')
                    fichier.write("\n")
                    fichier.write('          " pre ": " cond ": [{')
                    # constraint

                    loprd = data[" permission "][0][" action "][0][" refinement "][0][" leftOperand "]
                    opd = data[" permission "][0][" action "][0][" refinement "][0][" operator "]
                    roprd = data[" permission "][0][" action "][0][" refinement "][0][" rightOperand "][" @value "]

                    if str(loprd) == " timeInterval ":
                        fichier.write(' timeInterval ')
                    if str(loprd) == " spatial ":
                        fichier.write('location')
                    if str(loprd) == " payAmount ":
                        fichier.write('budget')
                    if str(loprd) == " dateTime ":
                        fichier.write('time')
                    if str(loprd) == " count " or str(loprd) == " delayPeriod ":
                        fichier.write('frequency')
                    # terminer ici les autres left operande ODRl
                    if str(opd) == " eq ":
                        fichier.write(' = ')
                    if str(opd) == " iteq ":
                        fichier.write(' <= ')
                    if str(opd) == " gteq ":
                        fichier.write(' >= ')
                    if str(opd) == " gt ":
                        fichier.write(' > ')
                    if str(opd) == " it ":
                        fichier.write(' < ')

                    fichier.write(str(roprd))

                    for j in list(range(1, len(data[" permission "][0][" action "][0][" refinement "]))):
                        fichier.write(" and ")
                        leftopr = data[" permission "][0][" action "][0][" refinement "][j][" leftOperand "]
                        oper = data[" permission "][0][" action "][0][" refinement "][j][" operator "]
                        rightopr = data[" permission "][0][" action "][0][" refinement "][j][" rightOperand "][" @value "]
                        print(leftopr)
                        print(oper)
                        print(rightopr)
                        if str(leftopr) == " timeInterval ":
                            fichier.write(' timeInterval ')
                        if str(leftopr) == " spatial ":
                            fichier.write('location')
                        if str(leftopr) == " payAmount ":
                            fichier.write('budget')
                        if str(leftopr) == " dateTime ":
                            fichier.write('time')
                        if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                            fichier.write('frequency')
                        # terminer ici les autres left operande ODRl
                        if str(oper) == " eq ":
                            fichier.write(' = ')
                        if str(oper) == " iteq ":
                            fichier.write(' <= ')
                        if str(oper) == " gteq ":
                            fichier.write(' >= ')
                        if str(oper) == " gt ":
                            fichier.write(' > ')
                        if str(oper) == "it":
                            fichier.write(' < ')

                        fichier.write(str(rightopr))





















                fichier.write("}]")  # fermeture de op:
                fichier.write("\n")
                fichier.write("}]")  # fermeture de rel:
                fichier.write("\n")
                fichier.write("}]")  # fermeture de ext-op
                fichier.write("\n")
                fichier.write("}")  # fermeture de la premi�re accolade













    else:  #s'il n' y a pas des op exter il n'y a pas l'elet IncludeIn
        print("Pas d'operation externe")
        fich = "C:\\Users\\amal\\Google Drive\\Projet Business Process\\project\\Credit applicat\\exam\\BU.bnf"
        print("je suis la !!")
        with open(fich, "w") as fichier:
            fichier.write("{\"uid\": ")
            fichier.write(fich)
            fichier.write("\n")
            fichier.write("\"res\":")
            target = data[" permission "][0][" target "]
            fichier.write("[{")
            fichier.write(target)
            fichier.write("}]")
            fichier.write("\n")
            fichier.write("\" ext-op \": [{")
            fichier.write("\n")
            fichier.write('    " name ": ')
            print(data[" permission "][0][" action "][0])
            if " refinement " in data[" permission "][0][" action "][0] or " includedIn " in data[" permission "][0][" action "][0]:
                nameop = str(data[" permission "][0][" action "][0][" rdf : value "][" @id "])
                name_op = nameop.replace(" odrl : ", "")
                print(name_op)
                fichier.write(name_op)
            else:
                nameop = str(data[" permission "][0][" action "])
                nameop = nameop.replace("[{' rdf : value ': {' @id ': ' odrl :", "", 1)
                nameop = nameop.replace("'}}]", "", 1)

                print(nameop)
                fichier.write(nameop)
            if " refinement " in data[" permission "][0][" action "][0]:
                fichier.write(',')
                fichier.write("\n")
                fichier.write('    " pre ": " cond ": [{')
                # constraint

                loprd = data[" permission "][0][" action "][0][" refinement "][0][" leftOperand "]
                opd = data[" permission "][0][" action "][0][" refinement "][0][" operator "]
                roprd = data[" permission "][0][" action "][0][" refinement "][0][" rightOperand "][" @value "]
                if str(loprd) == " timeInterval ":
                    fichier.write(' timeInterval ')
                if str(loprd) == " spatial ":
                    fichier.write('location')
                if str(loprd) == " payAmount ":
                    fichier.write('budget')
                if str(loprd) == " dateTime ":
                    fichier.write('time')
                if str(loprd) == " count " or str(loprd) == " delayPeriod ":
                    fichier.write('frequency')
                # terminer ici les autres left operande ODRl
                if str(opd) == " eq ":
                    fichier.write(' = ')
                if str(opd) == " iteq ":
                    fichier.write(' <= ')
                if str(opd) == " gteq ":
                    fichier.write(' >= ')
                if str(opd) == " gt ":
                    fichier.write(' > ')
                if str(opd) == " it ":
                    fichier.write(' < ')

                fichier.write(str(roprd))

                for j in list(range(1, len(data[" permission "][0][" action "][0][" refinement "]))):
                    fichier.write(" and ")
                    leftopr = data[" permission "][0][" action "][0][" refinement "][j][" leftOperand "]
                    oper = data[" permission "][0][" action "][0][" refinement "][j][" operator "]
                    rightopr = data[" permission "][0][" action "][0][" refinement "][j][" rightOperand "][" @value "]
                    print(leftopr)
                    print(oper)
                    print(rightopr)
                    if str(leftopr) == " timeInterval ":
                        fichier.write(' timeInterval ')
                    if str(leftopr) == " spatial ":
                        fichier.write('location')
                    if str(leftopr) == " payAmount ":
                        fichier.write('budget')
                    if str(leftopr) == " dateTime ":
                        fichier.write('time')
                    if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                        fichier.write('frequency')
                    # terminer ici les autres left operande ODRl
                    if str(oper) == " eq ":
                        fichier.write(' = ')
                    if str(oper) == " iteq ":
                        fichier.write(' <= ')
                    if str(oper) == " gteq ":
                        fichier.write(' >= ')
                    if str(oper) == " gt ":
                        fichier.write(' > ')
                    if str(oper) == "it":
                        fichier.write(' < ')

                    fichier.write(str(rightopr))
                if " constraint " in data[" permission "][0]:
                    for j in list(range(len(data[" permission "][0][" constraint "]))):
                        fichier.write(" and ")
                        leftopr = data[" permission "][0][" constraint "][j][" leftOperand "]
                        oper = data[" permission "][0][" constraint "][j][" operator "]
                        rightopr = data[" permission "][0][" constraint "][j][" rightOperand "][" @value "]
                        print(leftopr)
                        print(oper)
                        print(rightopr)

                        if str(leftopr) == " timeInterval ":
                            fichier.write(' timeInterval ')

                        if str(leftopr) == " spatial ":
                            fichier.write(' location ')
                        if str(leftopr) == " payAmount ":
                            fichier.write(' budget ')
                        if str(leftopr) == " dateTime ":
                            fichier.write(' time ')
                        if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                            fichier.write(' frequency ')
                        # terminer ici les autres left operande ODRl
                        if str(oper) == "eq":
                            fichier.write(' = ')
                        if str(oper) == "iteq":
                            fichier.write(' <= ')
                        if str(oper) == "gteq":
                            fichier.write(' >= ')
                        if str(oper) == "gt":
                            fichier.write(' > ')
                        if str(oper) == "it":
                            fichier.write(' < ')

                        fichier.write(str(rightopr))







                fichier.write("}]")  # fermeture de pre:cond de refinment action inter



            else: # s'il n' y a pas de refinment dans action
                if " constraint " in data[" permission "][0]:
                    print("yeeeeeeeeeeesss")
                    fichier.write(',')
                    fichier.write("\n")

                    fichier.write('    " pre ": " cond ": [{')
                    # constraint

                    leftopr = data[" permission "][0][" constraint "][0][" leftOperand "]
                    oper = data[" permission "][0][" constraint "][0][" operator "]
                    rightopr = data[" permission "][0][" constraint "][0][" rightOperand "][" @value "]
                    print(leftopr)
                    print(oper)
                    print(rightopr)
                    if str(leftopr) == " timeInterval ":
                        fichier.write(' timeInterval ')
                    if str(leftopr) == " spatial ":
                        fichier.write('location')
                    if str(leftopr) == " payAmount ":
                        fichier.write('budget')
                    if str(leftopr) == " dateTime ":
                        fichier.write('time')
                    if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                        fichier.write('frequency')
                    # terminer ici les autres left operande ODRl
                    if str(oper) == "eq":
                        fichier.write(' = ')
                    if str(oper) == "iteq":
                        fichier.write(' <= ')
                    if str(oper) == "gteq":
                        fichier.write(' >= ')
                    if str(oper) == "gt":
                        fichier.write(' > ')
                    if str(oper) == "it":
                        fichier.write(' < ')

                    fichier.write(str(rightopr))

                    for j in list(range(1, len(data[" permission "][0][" constraint "]))):
                        fichier.write(" and ")
                        leftopr = data[" permission "][0][" constraint "][j][" leftOperand "]
                        oper = data[" permission "][0][" constraint "][j][" operator "]
                        rightopr = data[" permission "][0][" constraint "][j][" rightOperand "][" @value "]
                        print(leftopr)
                        print(oper)
                        print(rightopr)

                        if str(leftopr) == " timeInterval ":
                            fichier.write(' timeInterval ')
                        if str(leftopr) == " spatial ":
                            fichier.write(' location ')
                        if str(leftopr) == " payAmount ":
                            fichier.write(' budget ')
                        if str(leftopr) == " dateTime ":
                            fichier.write(' time ')
                        if str(leftopr) == " count " or str(leftopr) == " delayPeriod ":
                            fichier.write('frequency')
                        if str(oper) == "eq":
                            fichier.write(' = ')
                        if str(oper) == "iteq":
                            fichier.write(' <= ')
                        if str(oper) == "gteq":
                            fichier.write(' >= ')
                        if str(oper) == "gt":
                            fichier.write(' > ')
                        if str(oper) == "it":
                            fichier.write(' < ')

                        fichier.write(str(rightopr))
                    fichier.write("}]")  # fermeture de pre:cond de constraint



            fichier.write("\n")
            fichier.write("    }]") # fermeture de ext-op
            fichier.write("\n")
            fichier.write("}")  # fermeture de la premi�re accolade







# **************   Fin des permission    *******















# **************   Pour les  obligations (duty rule)    *******


if " obligation " in data :
    if " includedIn " in data[" obligation "][0][" action "][0]: #s'il y a des op exter // il y a l'�let IncludeIn
        print("exist")
        print(data[" obligation "][0][" action "][0][" includedIn "])
        nb_BU = len((data[" obligation "][0][" action "][0][" includedIn "]))
        print(nb_BU)


        for i in list( range(nb_BU)):
            print(i)
            print(range(nb_BU - 1))
            fich = "C:\\Users\\amal\\Google Drive\\Projet Business Process\\project\\Credit applicat\\exam\\BU_Obl" + str(i) + ".bnf"

            with open(fich, "w") as fichier:
                fichier.write("{\"uid\": ")
                fichier.write(fich)
                fichier.write("\n")
                fichier.write("\"res\":")
                target = data[" obligation "][0][" target "]
                fichier.write("[{")
                fichier.write(target)
                fichier.write("}]")
                fichier.write("\n")
                fichier.write("\"ext-op\": [{")
                fichier.write("\n")

                fichier.write('    "name":')
                nameop = str(data[" obligation "][0][" action "][0][" includedIn "][i][" rdf : value "][" @id "])
                name_op = nameop.replace(" odrl : ", "")
                fichier.write(name_op)



                if " refinement " in data[" obligation "][0][" action "][0][" includedIn "][i]:
                    fichier.write(',')
                    fichier.write("\n")
                    fichier.write('    " pre ": " cond ": [{')
                    # constraint

                    loprd = data[" obligation "][0][" action "][0][" includedIn "][i][" refinement "][0][" leftOperand "]
                    opd = data[" obligation "][0][" action "][0][" includedIn "][i][" refinement "][0][" operator "]
                    roprd = data[" obligation "][0][" action "][0][" includedIn "][i][" refinement "][0][" rightOperand "][" @value "]
                    if str(loprd) == " spatial ":
                        fichier.write(' location ')
                    if str(loprd) == " payAmount ":
                        fichier.write(' budget ')
                    if str(loprd) == " dateTime ":
                        fichier.write(' time ')
                    if str(loprd) == " count " or str(loprd) == " delayPeriod ":
                        fichier.write(' frequency ')
                    if str(loprd) == " timeInterval ":
                        fichier.write(' timeInterval ')
                    # terminer ici les autres left operande ODRl
                    if str(opd) == " eq ":
                        fichier.write(' = ')
                    if str(opd) == " iteq ":
                        fichier.write(' <= ')
                    if str(opd) == " gteq ":
                        fichier.write(' >= ')
                    if str(opd) == " gt ":
                        fichier.write(' > ')
                    if str(opd) == " it ":
                        fichier.write(' < ')

                    fichier.write(str(roprd))

                    for j in list(range(1, len(data[" obligation "][0][" action "][0][" includedIn "][i][" refinement "]))):
                        fichier.write(" and ")
                        leftopr = data[" obligation "][0][" action "][0][" includedIn "][i][" refinement "][j][" leftOperand "]
                        oper = data[" obligation "][0][" action "][0][" includedIn "][i][" refinement "][j][" operator "]
                        rightopr = data[" obligation "][0][" action "][0][" includedIn "][i][" refinement "][j][" rightOperand "][" @value "]
                        print(leftopr)
                        print(oper)
                        print(rightopr)

                        if str(leftopr) == " spatial ":
                            fichier.write('location')
                        if str(leftopr) == " payAmount ":
                            fichier.write('budget')
                        if str(leftopr) == " dateTime ":
                            fichier.write('time')
                        if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                            fichier.write('frequency')
                        if str(leftopr) == " timeInterval ":
                            fichier.write(' timeInterval ')
                        # terminer ici les autres left operande ODRl
                        if str(oper) == " eq ":
                            fichier.write(' = ')
                        if str(oper) == " iteq ":
                            fichier.write(' <= ')
                        if str(oper) == " gteq ":
                            fichier.write(' >= ')
                        if str(oper) == " gt ":
                            fichier.write(' > ')
                        if str(oper) == "it":
                            fichier.write(' < ')

                        fichier.write(str(rightopr))
                    if " constraint " in data[" obligation "][0]:
                        for j in list(range(len(data[" obligation "][0][" constraint "]))):
                            fichier.write(" and ")
                            leftopr = data[" obligation "][0][" constraint "][j][" leftOperand "]
                            oper = data[" obligation "][0][" constraint "][j][" operator "]
                            rightopr = data[" obligation "][0][" constraint "][j][" rightOperand "][" @value "]
                            print(leftopr)
                            print(oper)
                            print(rightopr)

                            if str(leftopr) == " spatial ":
                                fichier.write(' location ')
                            if str(leftopr) == " payAmount ":
                                fichier.write(' budget ')
                            if str(leftopr) == " dateTime ":
                                fichier.write(' time ')
                            if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                                fichier.write(' frequency ')
                            if str(leftopr) == " timeInterval ":
                                fichier.write(' timeInterval ')
                            # terminer ici les autres left operande ODRl
                            if str(oper) == "eq":
                                fichier.write(' = ')
                            if str(oper) == "iteq":
                                fichier.write(' <= ')
                            if str(oper) == "gteq":
                                fichier.write(' >= ')
                            if str(oper) == "gt":
                                fichier.write(' > ')
                            if str(oper) == "it":
                                fichier.write(' < ')

                            fichier.write(str(rightopr))
                    fichier.write("}]")  # fermeture de pre:cond de constraint
                else: # pas de refinement
                    if " constraint " in data[" obligation "][0]:
                        print("yeeeeeeeeeeesss")
                        fichier.write(',')
                        fichier.write("\n")

                        fichier.write('    " pre ": " cond ": [{')
                        # constraint

                        leftopr = data[" obligation "][0][" constraint "][0][" leftOperand "]
                        oper = data[" obligation "][0][" constraint "][0][" operator "]
                        rightopr = data[" obligation "][0][" constraint "][0][" rightOperand "][" @value "]
                        print(leftopr)
                        print(oper)
                        print(rightopr)

                        if str(leftopr) == " spatial ":
                            fichier.write('location')
                        if str(leftopr) == " payAmount ":
                            fichier.write('budget')
                        if str(leftopr) == " dateTime ":
                            fichier.write('time')
                        if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                            fichier.write('frequency')
                        if str(leftopr) == " timeInterval ":
                            fichier.write(' timeInterval ')
                        # terminer ici les autres left operande ODRl
                        if str(oper) == "eq":
                            fichier.write(' = ')
                        if str(oper) == "iteq":
                            fichier.write(' <= ')
                        if str(oper) == "gteq":
                            fichier.write(' >= ')
                        if str(oper) == "gt":
                            fichier.write(' > ')
                        if str(oper) == "it":
                            fichier.write(' < ')

                        fichier.write(str(rightopr))

                        for j in list(range(1, len(data[" obligation "][0][" constraint "]))):
                            fichier.write(" and ")
                            leftopr = data[" obligation "][0][" constraint "][j][" leftOperand "]
                            oper = data[" obligation "][0][" constraint "][j][" operator "]
                            rightopr = data[" obligation "][0][" constraint "][j][" rightOperand "][" @value "]
                            print(leftopr)
                            print(oper)
                            print(rightopr)

                            if str(leftopr) == " spatial ":
                                fichier.write(' location ')
                            if str(leftopr) == " payAmount ":
                                fichier.write(' budget ')
                            if str(leftopr) == " dateTime ":
                                fichier.write(' time ')
                            if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                                fichier.write('frequency')
                            if str(leftopr) == " timeInterval ":
                                fichier.write(' timeInterval ')
                            # terminer ici les autres left operande ODRl
                            if str(oper) == "eq":
                                fichier.write(' = ')
                            if str(oper) == "iteq":
                                fichier.write(' <= ')
                            if str(oper) == "gteq":
                                fichier.write(' >= ')
                            if str(oper) == "gt":
                                fichier.write(' > ')
                            if str(oper) == "it":
                                fichier.write(' < ')

                            fichier.write(str(rightopr))
                        fichier.write("}]")  # fermeture de pre:cond de constraint

                fichier.write(",")  # fermeture de pre:cond
                fichier.write("\n")
                fichier.write('    " rel ": [{')
                fichier.write("\n")
                fichier.write('      "type ": precedes,')
                fichier.write("\n")
                fichier.write('      "op": [{')
                fichier.write("\n")
                fichier.write('          " name ":')
                nameopint = str(data[" obligation "][0][" action "][0][" rdf : value "][" @id "])
                name_opint = nameopint.replace(" odrl : ", "")
                fichier.write(name_opint)

                # s'il y a des refinement
                if " refinement " in data[" obligation "][0][" action "][0]:
                    fichier.write(',')
                    fichier.write("\n")
                    fichier.write('          " pre ": " cond ": [{')
                    # constraint

                    loprd = data[" obligation "][0][" action "][0][" refinement "][0][" leftOperand "]
                    opd = data[" obligation "][0][" action "][0][" refinement "][0][" operator "]
                    roprd = data[" obligation "][0][" action "][0][" refinement "][0][" rightOperand "][" @value "]
                    if str(loprd) == " spatial ":
                        fichier.write('location')
                    if str(loprd) == " payAmount ":
                        fichier.write('budget')
                    if str(loprd) == " dateTime ":
                        fichier.write('time')
                    if str(loprd) == " count " or str(loprd) == " delayPeriod ":
                        fichier.write('frequency')
                    if str(loprd) == " timeInterval ":
                        fichier.write(' timeInterval ')
                    # terminer ici les autres left operande ODRl
                    if str(opd) == " eq ":
                        fichier.write(' = ')
                    if str(opd) == " iteq ":
                        fichier.write(' <= ')
                    if str(opd) == " gteq ":
                        fichier.write(' >= ')
                    if str(opd) == " gt ":
                        fichier.write(' > ')
                    if str(opd) == " it ":
                        fichier.write(' < ')

                    fichier.write(str(roprd))

                    for j in list(range(1, len(data[" obligation "][0][" action "][0][" refinement "]))):
                        fichier.write(" and ")
                        leftopr = data[" obligation "][0][" action "][0][" refinement "][j][" leftOperand "]
                        oper = data[" obligation "][0][" action "][0][" refinement "][j][" operator "]
                        rightopr = data[" obligation "][0][" action "][0][" refinement "][j][" rightOperand "][" @value "]
                        print(leftopr)
                        print(oper)
                        print(rightopr)

                        if str(leftopr) == " spatial ":
                            fichier.write('location')
                        if str(leftopr) == " payAmount ":
                            fichier.write('budget')
                        if str(leftopr) == " dateTime ":
                            fichier.write('time')
                        if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                            fichier.write('frequency')
                        if str(leftopr) == " timeInterval ":
                            fichier.write(' timeInterval ')
                        # terminer ici les autres left operande ODRl
                        if str(oper) == " eq ":
                            fichier.write(' = ')
                        if str(oper) == " iteq ":
                            fichier.write(' <= ')
                        if str(oper) == " gteq ":
                            fichier.write(' >= ')
                        if str(oper) == " gt ":
                            fichier.write(' > ')
                        if str(oper) == "it":
                            fichier.write(' < ')

                        fichier.write(str(rightopr))





















                fichier.write("}]")  # fermeture de op:
                fichier.write("\n")
                fichier.write("}]")  # fermeture de rel:
                fichier.write("\n")
                fichier.write("}]")  # fermeture de ext-op
                fichier.write("\n")
                fichier.write("}")  # fermeture de la premi�re accolade













    else:  #s'il n' y a pas des op exter il n'y a pas l'elet IncludeIn
        print("Pas d'operation externe")
        fich = "C:\\Users\\amal\\Google Drive\\Projet Business Process\\project\\Credit applicat\\exam\\BU.bnf"

        with open(fich, "w") as fichier:
            fichier.write("{\"uid\": ")
            fichier.write(fich)
            fichier.write("\n")
            fichier.write("\"res\":")
            target = data[" obligation "][0][" target "]
            fichier.write("[{")
            fichier.write(target)
            fichier.write("}]")
            fichier.write("\n")
            fichier.write("\" ext-op \": [{")
            fichier.write("\n")
            fichier.write('    " name ": ')
            print(data[" obligation "][0][" action "][0])
            nameop = str(data[" obligation "][0][" action "][0][" rdf : value "][" @id "])
            name_op = nameop.replace(" odrl : ", "")
            print(name_op)
            fichier.write(name_op)

            if " refinement " in data[" obligation "][0][" action "][0]:
                fichier.write(',')
                fichier.write("\n")
                fichier.write('    " pre ": " cond ": [{')
                # constraint

                loprd = data[" obligation "][0][" action "][0][" refinement "][0][" leftOperand "]
                opd = data[" obligation "][0][" action "][0][" refinement "][0][" operator "]
                roprd = data[" obligation "][0][" action "][0][" refinement "][0][" rightOperand "][" @value "]
                if str(loprd) == " spatial ":
                    fichier.write('location')
                if str(loprd) == " payAmount ":
                    fichier.write('budget')
                if str(loprd) == " dateTime ":
                    fichier.write('time')
                if str(loprd) == " count " or str(loprd) == " delayPeriod ":
                    fichier.write('frequency')
                if str(loprd) == " timeInterval ":
                    fichier.write(' timeInterval ')
                if str(loprd) == " resolution ":
                    fichier.write(' resolution ')
                if str(loprd) == " event ":
                    fichier.write(' event ')
                # terminer ici les autres left operande ODRl
                if str(opd) == " eq ":
                    fichier.write(' = ')
                if str(opd) == " iteq ":
                    fichier.write(' <= ')
                if str(opd) == " gteq ":
                    fichier.write(' >= ')
                if str(opd) == " gt ":
                    fichier.write(' > ')
                if str(opd) == " it ":
                    fichier.write(' < ')

                fichier.write(str(roprd))

                for j in list(range(1, len(data[" obligation "][0][" action "][0][" refinement "]))):
                    fichier.write(" and ")
                    leftopr = data[" obligation "][0][" action "][0][" refinement "][j][" leftOperand "]
                    oper = data[" obligation "][0][" action "][0][" refinement "][j][" operator "]
                    rightopr = data[" obligation "][0][" action "][0][" refinement "][j][" rightOperand "][" @value "]
                    print(leftopr)
                    print(oper)
                    print(rightopr)

                    if str(leftopr) == " spatial ":
                        fichier.write('location')
                    if str(leftopr) == " payAmount ":
                        fichier.write('budget')
                    if str(leftopr) == " dateTime ":
                        fichier.write('time')
                    if str(leftopr) == " count " or str(leftopr) == " delayPeriod ":
                        fichier.write('frequency')
                    if str(leftopr) == " timeInterval ":
                        fichier.write(' timeInterval ')
                    if str(leftopr) == " event ":
                        fichier.write(' event ')
                    # terminer ici les autres left operande ODRl
                    if str(oper) == " eq ":
                        fichier.write(' = ')
                    if str(oper) == " iteq ":
                        fichier.write(' <= ')
                    if str(oper) == " gteq ":
                        fichier.write(' >= ')
                    if str(oper) == " gt ":
                        fichier.write(' > ')
                    if str(oper) == "it":
                        fichier.write(' < ')

                    fichier.write(str(rightopr))
                if " constraint " in data[" obligation "][0]:
                    for j in list(range(len(data[" obligation "][0][" constraint "]))):
                        fichier.write(" and ")
                        leftopr = data[" obligation "][0][" constraint "][j][" leftOperand "]
                        oper = data[" obligation "][0][" constraint "][j][" operator "]
                        rightopr = data[" obligation "][0][" constraint "][j][" rightOperand "][" @value "]
                        print(leftopr)
                        print(oper)
                        print(rightopr)

                        if str(leftopr) == " timeInterval ":
                            fichier.write(' timeInterval ')


                        if str(leftopr) == " spatial ":
                            fichier.write(' location ')
                        if str(leftopr) == " payAmount ":
                            fichier.write(' budget ')
                        if str(leftopr) == " dateTime ":
                            fichier.write(' time ')
                        if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                            fichier.write(' frequency ')
                        # terminer ici les autres left operande ODRl
                        if str(oper) == "eq":
                            fichier.write(' = ')
                        if str(oper) == "iteq":
                            fichier.write(' <= ')
                        if str(oper) == "gteq":
                            fichier.write(' >= ')
                        if str(oper) == "gt":
                            fichier.write(' > ')
                        if str(oper) == "it":
                            fichier.write(' < ')

                        fichier.write(str(rightopr))







                fichier.write("}]")  # fermeture de pre:cond de refinment action inter



            else: # s'il n' y a pas de refinment dans action
                if " constraint " in data[" obligation "][0]:
                    print("yeeeeeeeeeeesss")
                    fichier.write(',')
                    fichier.write("\n")

                    fichier.write('    " pre ": " cond ": [{')
                    # constraint

                    leftopr = data[" obligation "][0][" constraint "][0][" leftOperand "]
                    oper = data[" obligation "][0][" constraint "][0][" operator "]
                    rightopr = data[" obligation "][0][" constraint "][0][" rightOperand "][" @value "]
                    print(leftopr)
                    print(oper)
                    print(rightopr)

                    if str(leftopr) == " spatial ":
                        fichier.write('location')
                    if str(leftopr) == " payAmount ":
                        fichier.write('budget')
                    if str(leftopr) == " dateTime ":
                        fichier.write('time')
                    if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                        fichier.write('frequency')
                    if str(leftopr) == " timeInterval ":
                        fichier.write(' timeInterval ')
                    # terminer ici les autres left operande ODRl
                    if str(oper) == "eq":
                        fichier.write(' = ')
                    if str(oper) == "iteq":
                        fichier.write(' <= ')
                    if str(oper) == "gteq":
                        fichier.write(' >= ')
                    if str(oper) == "gt":
                        fichier.write(' > ')
                    if str(oper) == "it":
                        fichier.write(' < ')

                    fichier.write(str(rightopr))

                    for j in list(range(1, len(data[" obligation "][0][" constraint "]))):
                        fichier.write(" and ")
                        leftopr = data[" obligation "][0][" constraint "][j][" leftOperand "]
                        oper = data[" obligation "][0][" constraint "][j][" operator "]
                        rightopr = data[" obligation "][0][" constraint "][j][" rightOperand "][" @value "]
                        print(leftopr)
                        print(oper)
                        print(rightopr)

                        if str(leftopr) == " timeInterval ":
                            fichier.write(' timeInterval ')

                        if str(leftopr) == " spatial ":
                            fichier.write(' location ')
                        if str(leftopr) == " payAmount ":
                            fichier.write(' budget ')
                        if str(leftopr) == " dateTime ":
                            fichier.write(' time ')
                        if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
                            fichier.write('frequency')
                        # terminer ici les autres left operande ODRl
                        if str(oper) == " eq ":
                            fichier.write(' = ')
                        if str(oper) == " iteq ":
                            fichier.write(' <= ')
                        if str(oper) == " gteq ":
                            fichier.write(' >= ')
                        if str(oper) == " gt ":
                            fichier.write(' > ')
                        if str(oper) == " it ":
                            fichier.write(' < ')

                        fichier.write(str(rightopr))
                    fichier.write("}]")  # fermeture de pre:cond de constraint



            fichier.write("\n")
            fichier.write("    }]") # fermeture de ext-op
            fichier.write("\n")
            fichier.write("}")  # fermeture de la premi�re accolade






# **************   Fin des  obligations (duty rule)    *******
# **************   Pour les prohibition    *******

# """if " prohibition " in data :
#     if " includedIn " in data[" prohibition "][0][" action "][0]: #s'il y a des op exter // il y a l'�let IncludeIn
#         print("exist")
#         print(data[" prohibition "][0][" action "][0][" includedIn "])
#         nb_BU = len((data[" prohibition "][0][" action "][0][" includedIn "]))
#         print(nb_BU)


#         for i in list( range(nb_BU)):
#             print(i)
#             print(range(nb_BU - 1))
#             fich = "C:\\Users\\amal\\Desktop\\project\\BU_Pro" + str(i) + ".bnf"

#             with open(fich, "w") as fichier:
#                 fichier.write("{\"uid\": ")
#                 fichier.write(fich)
#                 fichier.write("\n")
#                 fichier.write("\"res\":")
#                 target = data[" prohibition "][0][" target "]
#                 fichier.write("[{")
#                 fichier.write(target)
#                 fichier.write("}]")
#                 fichier.write("\n")
#                 fichier.write("\"ext-op\": [{")
#                 fichier.write("\n")
#                 fichier.write('    "name":')


#                 nameop = str(data[" prohibition "][0][" action "][0][" includedIn "][i][" rdf : value "][" @id "])
#                 name_op = nameop.replace(" odrl : ", "")
#                 fichier.write(name_op)



#                 if " refinement " in data[" prohibition "][0][" action "][0][" includedIn "][i]:
#                     fichier.write(',')
#                     fichier.write("\n")
#                     fichier.write('    " pre ": " cond ": [{')
#                     # constraint

#                     loprd = data[" prohibition "][0][" action "][0][" includedIn "][i][" refinement "][0][" leftOperand "]
#                     opd = data[" prohibition "][0][" action "][0][" includedIn "][i][" refinement "][0][" operator "]
#                     roprd = data[" prohibition "][0][" action "][0][" includedIn "][i][" refinement "][0][" rightOperand "][" @value "]
#                     if str(loprd) == " timeInterval ":
#                         fichier.write(' timeInterval ')
#                     if str(loprd) == " spatial ":
#                         fichier.write(' location ')
#                     if str(loprd) == " payAmount ":
#                         fichier.write(' budget ')
#                     if str(loprd) == " dateTime ":
#                         fichier.write(' time ')
#                     if str(loprd) == " count " or str(loprd) == " delayPeriod ":
#                         fichier.write(' frequency ')
#                     # terminer ici les autres left operande ODRl
#                     if str(opd) == " eq ":
#                         fichier.write(' = ')
#                     if str(opd) == " iteq ":
#                         fichier.write(' <= ')
#                     if str(opd) == " gteq ":
#                         fichier.write(' >= ')
#                     if str(opd) == " gt ":
#                         fichier.write(' > ')
#                     if str(opd) == " it ":
#                         fichier.write(' < ')

#                     fichier.write(str(roprd))

#                     for j in list(range(1, len(data[" prohibition "][0][" action "][0][" includedIn "][i][" refinement "]))):
#                         fichier.write(" and ")
#                         leftopr = data[" prohibition "][0][" action "][0][" includedIn "][i][" refinement "][j][" leftOperand "]
#                         oper = data[" prohibition "][0][" action "][0][" includedIn "][i][" refinement "][j][" operator "]
#                         rightopr = data[" prohibition "][0][" action "][0][" includedIn "][i][" refinement "][j][" rightOperand "][" @value "]
#                         print(leftopr)
#                         print(oper)
#                         print(rightopr)

#                         if str(leftopr) == " timeInterval ":
#                             fichier.write(' timeInterval ')
#                         if str(leftopr) == " spatial ":
#                             fichier.write('location')
#                         if str(leftopr) == " payAmount ":
#                             fichier.write('budget')
#                         if str(leftopr) == " dateTime ":
#                             fichier.write('time')
#                         if str(leftopr) == " count " or str(loprd) == " delayPeriod ":
#                             fichier.write('frequency')
#                         # terminer ici les autres left operande ODRl
#                         if str(oper) == " eq ":
#                             fichier.write(' = ')
#                         if str(oper) == " iteq ":
#                             fichier.write(' <= ')
#                         if str(oper) == " gteq ":
#                             fichier.write(' >= ')
#                         if str(oper) == " gt ":
#                             fichier.write(' > ')
#                         if str(oper) == "it":
#                             fichier.write(' < ')

#                         fichier.write(str(rightopr))
#                     if " constraint " in data[" prohibition "][0]:
#                         for j in list(range(len(data[" prohibition "][0][" constraint "]))):
#                             fichier.write(" and ")
#                             leftopr = data[" prohibition "][0][" constraint "][j][" leftOperand "]
#                             oper = data[" prohibition "][0][" constraint "][j][" operator "]
#                             rightopr = data[" prohibition "][0][" constraint "][j][" rightOperand "][" @value "]
#                             print(leftopr)
#                             print(oper)
#                             print(rightopr)

#                             if str(leftopr) == " timeInterval ":
#                                 fichier.write(' timeInterval ')
#                             if str(leftopr) == " spatial ":
#                                 fichier.write(' location ')
#                             if str(leftopr) == " payAmount ":
#                                 fichier.write(' budget ')
#                             if str(leftopr) == " dateTime ":
#                                 fichier.write(' time ')
#                             if str(leftopr) == " count ":
#                                 fichier.write(' frequency ')
#                             # terminer ici les autres left operande ODRl
#                             if str(oper) == "eq":
#                                 fichier.write(' = ')
#                             if str(oper) == "iteq":
#                                 fichier.write(' <= ')
#                             if str(oper) == "gteq":
#                                 fichier.write(' >= ')
#                             if str(oper) == "gt":
#                                 fichier.write(' > ')
#                             if str(oper) == "it":
#                                 fichier.write(' < ')

#                             fichier.write(str(rightopr))
#                     fichier.write("}]")  # fermeture de pre:cond de constraint
#                 else: # pas de refinement
#                     if " constraint " in data[" prohibition "][0]:
#                         print("yeeeeeeeeeeesss")
#                         fichier.write(',')
#                         fichier.write("\n")

#                         fichier.write('    " pre ": " cond ": [{')
#                         # constraint

#                         leftopr = data[" prohibition "][0][" constraint "][0][" leftOperand "]
#                         oper = data[" prohibition "][0][" constraint "][0][" operator "]
#                         rightopr = data[" prohibition "][0][" constraint "][0][" rightOperand "][" @value "]
#                         print(leftopr)
#                         print(oper)
#                         print(rightopr)

#                         if str(leftopr) == " spatial ":
#                             fichier.write('location')
#                         if str(leftopr) == " payAmount ":
#                             fichier.write('budget')
#                         if str(leftopr) == " dateTime ":
#                             fichier.write('time')
#                         if str(leftopr) == " count ":
#                             fichier.write('frequency')
#                         if str(leftopr) == " timeInterval ":
#                             fichier.write(' timeInterval ')
#                         # terminer ici les autres left operande ODRl
#                         if str(oper) == "eq":
#                             fichier.write(' = ')
#                         if str(oper) == "iteq":
#                             fichier.write(' <= ')
#                         if str(oper) == "gteq":
#                             fichier.write(' >= ')
#                         if str(oper) == "gt":
#                             fichier.write(' > ')
#                         if str(oper) == "it":
#                             fichier.write(' < ')

#                         fichier.write(str(rightopr))

#                         for j in list(range(1, len(data[" prohibition "][0][" constraint "]))):
#                             fichier.write(" and ")
#                             leftopr = data[" prohibition "][0][" constraint "][j][" leftOperand "]
#                             oper = data[" prohibition "][0][" constraint "][j][" operator "]
#                             rightopr = data[" prohibition "][0][" constraint "][j][" rightOperand "][" @value "]
#                             print(leftopr)
#                             print(oper)
#                             print(rightopr)

#                             if str(leftopr) == " spatial ":
#                                 fichier.write(' location ')
#                             if str(leftopr) == " payAmount ":
#                                 fichier.write(' budget ')
#                             if str(leftopr) == " dateTime ":
#                                 fichier.write(' time ')
#                             if str(leftopr) == " count ":
#                                 fichier.write('frequency')
#                             if str(leftopr) == " timeInterval ":
#                                 fichier.write(' timeInterval ')
#                             # terminer ici les autres left operande ODRl
#                             if str(oper) == "eq":
#                                 fichier.write(' = ')
#                             if str(oper) == "iteq":
#                                 fichier.write(' <= ')
#                             if str(oper) == "gteq":
#                                 fichier.write(' >= ')
#                             if str(oper) == "gt":
#                                 fichier.write(' > ')
#                             if str(oper) == "it":
#                                 fichier.write(' < ')

#                             fichier.write(str(rightopr))
#                         fichier.write("}]")  # fermeture de pre:cond de constraint

#                 fichier.write(",")  # fermeture de pre:cond
#                 fichier.write("\n")
#                 fichier.write('    " rel ": [{')
#                 fichier.write("\n")
#                 fichier.write('      "type ": precedes,')
#                 fichier.write("\n")
#                 fichier.write('      "op": [{')
#                 fichier.write("\n")
#                 fichier.write('          " name ":')
#                 nameopint = str(data[" prohibition "][0][" action "][0][" rdf : value "][" @id "])
#                 name_opint = nameopint.replace(" odrl : ", "")
#                 fichier.write(name_opint)

#                 # s'il y a des refinement
#                 if " refinement " in data[" prohibition "][0][" action "][0]:
#                     fichier.write(',')
#                     fichier.write("\n")
#                     fichier.write('          " pre ": " cond ": [{')
#                     # constraint

#                     loprd = data[" prohibition "][0][" action "][0][" refinement "][0][" leftOperand "]
#                     opd = data[" prohibition "][0][" action "][0][" refinement "][0][" operator "]
#                     roprd = data[" prohibition "][0][" action "][0][" refinement "][0][" rightOperand "][" @value "]
#                     if str(loprd) == " spatial ":
#                         fichier.write('location')
#                     if str(loprd) == " payAmount ":
#                         fichier.write('budget')
#                     if str(loprd) == " dateTime ":
#                         fichier.write('time')
#                     if str(loprd) == " count ":
#                         fichier.write('frequency')
#                     if str(loprd) == " timeInterval ":
#                         fichier.write(' timeInterval ')
#                     # terminer ici les autres left operande ODRl
#                     if str(opd) == " eq ":
#                         fichier.write(' = ')
#                     if str(opd) == " iteq ":
#                         fichier.write(' <= ')
#                     if str(opd) == " gteq ":
#                         fichier.write(' >= ')
#                     if str(opd) == " gt ":
#                         fichier.write(' > ')
#                     if str(opd) == " it ":
#                         fichier.write(' < ')

#                     fichier.write(str(roprd))

#                     for j in list(range(1, len(data[" prohibition "][0][" action "][0][" refinement "]))):
#                         fichier.write(" and ")
#                         leftopr = data[" prohibition "][0][" action "][0][" refinement "][j][" leftOperand "]
#                         oper = data[" prohibition "][0][" action "][0][" refinement "][j][" operator "]
#                         rightopr = data[" prohibition "][0][" action "][0][" refinement "][j][" rightOperand "][" @value "]
#                         print(leftopr)
#                         print(oper)
#                         print(rightopr)

#                         if str(leftopr) == " spatial ":
#                             fichier.write('location')
#                         if str(leftopr) == " payAmount ":
#                             fichier.write('budget')
#                         if str(leftopr) == " dateTime ":
#                             fichier.write('time')
#                         if str(leftopr) == " count ":
#                             fichier.write('frequency')
#                         if str(leftopr) == " timeInterval ":
#                             fichier.write(' timeInterval ')
#                         # terminer ici les autres left operande ODRl
#                         if str(oper) == " eq ":
#                             fichier.write(' = ')
#                         if str(oper) == " iteq ":
#                             fichier.write(' <= ')
#                         if str(oper) == " gteq ":
#                             fichier.write(' >= ')
#                         if str(oper) == " gt ":
#                             fichier.write(' > ')
#                         if str(oper) == "it":
#                             fichier.write(' < ')

#                         fichier.write(str(rightopr))





















#                 fichier.write("}]")  # fermeture de op:
#                 fichier.write("\n")
#                 fichier.write("}]")  # fermeture de rel:
#                 fichier.write("\n")
#                 fichier.write("}]")  # fermeture de ext-op
#                 fichier.write("\n")
#                 fichier.write("}")  # fermeture de la premi�re accolade













#     else:  #s'il n' y a pas des op exter il n'y a pas l'elet IncludeIn
#         print("Pas d'operation externe")
#         fich = "C:\\Users\\amal\\Google Drive\\Projet Business Process\\project\\expl3\\BU_PRO.bnf"

#         with open(fich, "w") as fichier:
#             fichier.write("{\"uid\": ")
#             fichier.write(fich)
#             fichier.write("\n")
#             fichier.write("\"res\":")
#             target = data[" prohibition "][0][" target "]
#             fichier.write("[{")
#             fichier.write(target)
#             fichier.write("}]")
#             fichier.write("\n")
#             fichier.write("\" ext-op \": [{")
#             fichier.write("\n")
#             fichier.write('    " name ": ')
#             print(data[" prohibition "][0][" action "][0])
#             if " refinement " in data[" prohibition "][0][" action "][0] or " includedIn " in data[" prohibition "][0][" action "][0]:
#                 nameop = str(data[" prohibition "][0][" action "][0][" rdf : value "][" @id "])
#                 name_op = nameop.replace(" odrl : ", "")
#                 print(name_op)
#                 fichier.write(name_op)
#             else:
#                 nameop = str(data[" prohibition "][0][" action "])
#                 print(nameop)
#                 fichier.write(nameop)




#             if " refinement " in data[" prohibition "][0][" action "][0]:
#                 fichier.write(',')
#                 fichier.write("\n")
#                 fichier.write('    " pre ": " cond ": [{')
#                 # constraint

#                 loprd = data[" prohibition "][0][" action "][0][" refinement "][0][" leftOperand "]
#                 opd = data[" prohibition "][0][" action "][0][" refinement "][0][" operator "]
#                 roprd = data[" prohibition "][0][" action "][0][" refinement "][0][" rightOperand "][" @value "]
#                 if str(loprd) == " spatial ":
#                     fichier.write('location')
#                 if str(loprd) == " payAmount ":
#                     fichier.write('budget')
#                 if str(loprd) == " dateTime ":
#                     fichier.write('time')
#                 if str(loprd) == " count ":
#                     fichier.write('frequency')
#                 if str(loprd) == " timeInterval ":
#                     fichier.write(' timeInterval ')
#                 if str(loprd) == " resolution ":
#                     fichier.write(' resolution ')
#                 # terminer ici les autres left operande ODRl
#                 if str(opd) == " eq ":
#                     fichier.write(' = ')
#                 if str(opd) == " iteq ":
#                     fichier.write(' <= ')
#                 if str(opd) == " gteq ":
#                     fichier.write(' >= ')
#                 if str(opd) == " gt ":
#                     fichier.write(' > ')
#                 if str(opd) == " it ":
#                     fichier.write(' < ')

#                 fichier.write(str(roprd))

#                 for j in list(range(1, len(data[" prohibition "][0][" action "][0][" refinement "]))):
#                     fichier.write(" and ")
#                     leftopr = data[" prohibition "][0][" action "][0][" refinement "][j][" leftOperand "]
#                     oper = data[" prohibition "][0][" action "][0][" refinement "][j][" operator "]
#                     rightopr = data[" prohibition "][0][" action "][0][" refinement "][j][" rightOperand "][" @value "]
#                     print(leftopr)
#                     print(oper)
#                     print(rightopr)

#                     if str(leftopr) == " spatial ":
#                         fichier.write('location')
#                     if str(leftopr) == " payAmount ":
#                         fichier.write('budget')
#                     if str(leftopr) == " dateTime ":
#                         fichier.write('time')
#                     if str(leftopr) == " count ":
#                         fichier.write('frequency')
#                     if str(leftopr) == " timeInterval ":
#                         fichier.write(' timeInterval ')
#                     # terminer ici les autres left operande ODRl
#                     if str(oper) == " eq ":
#                         fichier.write(' = ')
#                     if str(oper) == " iteq ":
#                         fichier.write(' <= ')
#                     if str(oper) == " gteq ":
#                         fichier.write(' >= ')
#                     if str(oper) == " gt ":
#                         fichier.write(' > ')
#                     if str(oper) == "it":
#                         fichier.write(' < ')

#                     fichier.write(str(rightopr))
#                 if " constraint " in data[" prohibition "][0]:
#                     for j in list(range(len(data[" prohibition "][0][" constraint "]))):
#                         fichier.write(" and ")
#                         leftopr = data[" prohibition "][0][" constraint "][j][" leftOperand "]
#                         oper = data[" prohibition "][0][" constraint "][j][" operator "]
#                         rightopr = data[" prohibition "][0][" constraint "][j][" rightOperand "][" @value "]
#                         print(leftopr)
#                         print(oper)
#                         print(rightopr)

#                         if str(leftopr) == " timeInterval ":
#                             fichier.write(' timeInterval ')

#                         if str(leftopr) == " spatial ":
#                             fichier.write(' location ')
#                         if str(leftopr) == " payAmount ":
#                             fichier.write(' budget ')
#                         if str(leftopr) == " dateTime ":
#                             fichier.write(' time ')
#                         if str(leftopr) == " count ":
#                             fichier.write(' frequency ')
#                         # terminer ici les autres left operande ODRl
#                         if str(oper) == "eq":
#                             fichier.write(' = ')
#                         if str(oper) == "iteq":
#                             fichier.write(' <= ')
#                         if str(oper) == "gteq":
#                             fichier.write(' >= ')
#                         if str(oper) == "gt":
#                             fichier.write(' > ')
#                         if str(oper) == "it":
#                             fichier.write(' < ')

#                         fichier.write(str(rightopr))







#                 fichier.write("}]")  # fermeture de pre:cond de refinment action inter



#             else: # s'il n' y a pas de refinment dans action
#                 if " constraint " in data[" prohibition "][0]:
#                     print("yeeeeeeeeeeesss")
#                     fichier.write(',')
#                     fichier.write("\n")

#                     fichier.write('    " pre ": " cond ": [{')
#                     # constraint

#                     leftopr = data[" prohibition "][0][" constraint "][0][" leftOperand "]
#                     oper = data[" prohibition "][0][" constraint "][0][" operator "]
#                     rightopr = data[" prohibition "][0][" constraint "][0][" rightOperand "][" @value "]
#                     print(leftopr)
#                     print(oper)
#                     print(rightopr)

#                     if str(leftopr) == " spatial ":
#                         fichier.write('location')
#                     if str(leftopr) == " payAmount ":
#                         fichier.write('budget')
#                     if str(leftopr) == " dateTime ":
#                         fichier.write('time')
#                     if str(leftopr) == " count ":
#                         fichier.write('frequency')
#                     if str(leftopr) == " timeInterval ":
#                         fichier.write(' timeInterval ')
#                     # terminer ici les autres left operande ODRl
#                     if str(oper) == "eq":
#                         fichier.write(' = ')
#                     if str(oper) == "iteq":
#                         fichier.write(' <= ')
#                     if str(oper) == "gteq":
#                         fichier.write(' >= ')
#                     if str(oper) == "gt":
#                         fichier.write(' > ')
#                     if str(oper) == "it":
#                         fichier.write(' < ')

#                     fichier.write(str(rightopr))

#                     for j in list(range(1, len(data[" prohibition "][0][" constraint "]))):
#                         fichier.write(" and ")
#                         leftopr = data[" prohibition "][0][" constraint "][j][" leftOperand "]
#                         oper = data[" prohibition "][0][" constraint "][j][" operator "]
#                         rightopr = data[" prohibition "][0][" constraint "][j][" rightOperand "][" @value "]
#                         print(leftopr)
#                         print(oper)
#                         print(rightopr)

#                         if str(leftopr) == " timeInterval ":
#                             fichier.write(' timeInterval ')


#                         if str(leftopr) == " spatial ":
#                             fichier.write(' location ')
#                         if str(leftopr) == " payAmount ":
#                             fichier.write(' budget ')
#                         if str(leftopr) == " dateTime ":
#                             fichier.write(' time ')
#                         if str(leftopr) == " count ":
#                             fichier.write('frequency')
#                         # terminer ici les autres left operande ODRl
#                         if str(oper) == "eq":
#                             fichier.write(' = ')
#                         if str(oper) == "iteq":
#                             fichier.write(' <= ')
#                         if str(oper) == "gteq":
#                             fichier.write(' >= ')
#                         if str(oper) == "gt":
#                             fichier.write(' > ')
#                         if str(oper) == "it":
#                             fichier.write(' < ')

#                         fichier.write(str(rightopr))
#                     fichier.write("}]")  # fermeture de pre:cond de constraint



#             fichier.write("\n")
#             fichier.write("    }]") # fermeture de ext-op
#             fichier.write("\n")
#             fichier.write("}")  # fermeture de la premi�re accolade





# # **************   Fin des prohibition    *******

