def add_vectors(v1, v2):
    return [sum(i) for i in zip(v1, v2)]
def mul_vector_number(v1, num):
    return [i * num for i in v1]
def score(input):
    if (input[68]) <= (13.075935363769531):
        if (input[151]) <= (1.8662800192832947):
            if (input[209]) <= (31.10305404663086):
                if (input[246]) <= (-3.5769375562667847):
                    if (input[3]) <= (-0.39694660902023315):
                        var0 = [0.0, 1.0, 0.0, 0.0]
                    else:
                        var0 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var0 = [1.0, 0.0, 0.0, 0.0]
            else:
                if (input[234]) <= (-3.1471779346466064):
                    var0 = [0.0, 1.0, 0.0, 0.0]
                else:
                    var0 = [1.0, 0.0, 0.0, 0.0]
        else:
            var0 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[21]) <= (6.206106543540955):
            var0 = [0.0, 0.0, 0.0, 1.0]
        else:
            var0 = [1.0, 0.0, 0.0, 0.0]
    if (input[181]) <= (1.2138599753379822):
        if (input[174]) <= (1.9512745141983032):
            if (input[174]) <= (-2.346318006515503):
                if (input[305]) <= (-14.919846013188362):
                    var1 = [0.0, 0.0, 0.0, 1.0]
                else:
                    var1 = [0.0, 0.0, 1.0, 0.0]
            else:
                var1 = [1.0, 0.0, 0.0, 0.0]
        else:
            if (input[19]) <= (0.0790086630731821):
                var1 = [0.0, 1.0, 0.0, 0.0]
            else:
                if (input[72]) <= (3.30758935585618):
                    var1 = [0.0, 0.0, 1.0, 0.0]
                else:
                    var1 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[83]) <= (48.32061553001404):
            if (input[169]) <= (2.318784475326538):
                var1 = [0.0, 1.0, 0.0, 0.0]
            else:
                var1 = [0.0, 0.0, 1.0, 0.0]
        else:
            var1 = [0.0, 0.0, 0.0, 1.0]
    if (input[120]) <= (2.181117534637451):
        if (input[39]) <= (-0.5229008197784424):
            if (input[294]) <= (-0.06344635970890522):
                if (input[156]) <= (1.0426747351884842):
                    var2 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var2 = [0.0, 1.0, 0.0, 0.0]
            else:
                if (input[169]) <= (2.182314932346344):
                    if (input[210]) <= (2.659958004951477):
                        var2 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        var2 = [0.0, 1.0, 0.0, 0.0]
                else:
                    var2 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[198]) <= (1.4664486944675446):
                var2 = [1.0, 0.0, 0.0, 0.0]
            else:
                if (input[25]) <= (0.3543418552726507):
                    var2 = [0.0, 1.0, 0.0, 0.0]
                else:
                    var2 = [0.0, 0.0, 1.0, 0.0]
    else:
        var2 = [0.0, 0.0, 0.0, 1.0]
    if (input[112]) <= (-44.62213897705078):
        var3 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[181]) <= (4.513070583343506):
            if (input[198]) <= (3.9097315073013306):
                if (input[180]) <= (8.130707800388336):
                    var3 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var3 = [0.0, 1.0, 0.0, 0.0]
            else:
                var3 = [0.0, 1.0, 0.0, 0.0]
        else:
            var3 = [0.0, 0.0, 1.0, 0.0]
    return mul_vector_number(add_vectors(add_vectors(add_vectors(var0, var1), var2), var3), 0.25)
