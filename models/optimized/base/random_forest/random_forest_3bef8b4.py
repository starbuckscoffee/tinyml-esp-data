def add_vectors(v1, v2):
    return [sum(i) for i in zip(v1, v2)]
def mul_vector_number(v1, num):
    return [i * num for i in v1]
def score(input):
    if (input[68]) <= (14.246695041656494):
        if (input[55]) <= (3.5063085556030273):
            if (input[179]) <= (-2.75190806388855):
                if (input[251]) <= (-2.900763511657715):
                    var0 = [1.0, 0.0, 0.0, 0.0]
                else:
                    if (input[199]) <= (0.27892449498176575):
                        var0 = [0.0, 1.0, 0.0, 0.0]
                    else:
                        if (input[233]) <= (22.958014488220215):
                            var0 = [1.0, 0.0, 0.0, 0.0]
                        else:
                            var0 = [0.0, 0.0, 0.0, 1.0]
            else:
                var0 = [1.0, 0.0, 0.0, 0.0]
        else:
            var0 = [0.0, 0.0, 1.0, 0.0]
    else:
        var0 = [0.0, 0.0, 0.0, 1.0]
    if (input[48]) <= (-3.9444470405578613):
        var1 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[178]) <= (0.8396946489810944):
            if (input[126]) <= (-5.281608819961548):
                var1 = [0.0, 1.0, 0.0, 0.0]
            else:
                if (input[145]) <= (-1.7357965111732483):
                    var1 = [0.0, 1.0, 0.0, 0.0]
                else:
                    var1 = [1.0, 0.0, 0.0, 0.0]
        else:
            if (input[103]) <= (-1.8363524675369263):
                var1 = [0.0, 0.0, 1.0, 0.0]
            else:
                if (input[72]) <= (4.34547632932663):
                    if (input[144]) <= (-0.6907271444797516):
                        var1 = [0.0, 0.0, 1.0, 0.0]
                    else:
                        var1 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var1 = [0.0, 1.0, 0.0, 0.0]
    if (input[120]) <= (2.6587610244750977):
        if (input[31]) <= (1.1611875295639038):
            if (input[36]) <= (0.9959878921508789):
                if (input[85]) <= (3.9755719900131226):
                    var2 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var2 = [0.0, 0.0, 1.0, 0.0]
            else:
                if (input[290]) <= (10.218454837799072):
                    var2 = [0.0, 1.0, 0.0, 0.0]
                else:
                    var2 = [1.0, 0.0, 0.0, 0.0]
        else:
            if (input[210]) <= (-0.03232169896364212):
                var2 = [1.0, 0.0, 0.0, 0.0]
            else:
                var2 = [0.0, 0.0, 1.0, 0.0]
    else:
        var2 = [0.0, 0.0, 0.0, 1.0]
    if (input[62]) <= (14.189235210418701):
        if (input[109]) <= (-3.031059503555298):
            var3 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[144]) <= (-2.968809962272644):
                var3 = [0.0, 1.0, 0.0, 0.0]
            else:
                if (input[60]) <= (3.1328131556510925):
                    if (input[133]) <= (-5.585672497749329):
                        var3 = [0.0, 0.0, 1.0, 0.0]
                    else:
                        var3 = [1.0, 0.0, 0.0, 0.0]
                else:
                    if (input[82]) <= (-0.5916030406951904):
                        var3 = [0.0, 0.0, 1.0, 0.0]
                    else:
                        var3 = [0.0, 1.0, 0.0, 0.0]
    else:
        var3 = [0.0, 0.0, 0.0, 1.0]
    if (input[134]) <= (5.585672616958618):
        var4 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[263]) <= (5.709923505783081):
            if (input[19]) <= (0.490811288356781):
                if (input[108]) <= (-1.9021929502487183):
                    var4 = [0.0, 1.0, 0.0, 0.0]
                else:
                    if (input[158]) <= (10.11071491241455):
                        if (input[67]) <= (0.21547814458608627):
                            var4 = [0.0, 1.0, 0.0, 0.0]
                        else:
                            if (input[60]) <= (-0.02394205331802368):
                                var4 = [0.0, 0.0, 1.0, 0.0]
                            else:
                                var4 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        if (input[216]) <= (0.1496376022696495):
                            var4 = [1.0, 0.0, 0.0, 0.0]
                        else:
                            if (input[87]) <= (-6.225192755460739):
                                var4 = [1.0, 0.0, 0.0, 0.0]
                            else:
                                var4 = [0.0, 0.0, 1.0, 0.0]
            else:
                if (input[47]) <= (-20.343509674072266):
                    var4 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var4 = [0.0, 0.0, 1.0, 0.0]
        else:
            var4 = [1.0, 0.0, 0.0, 0.0]
    return mul_vector_number(add_vectors(add_vectors(add_vectors(add_vectors(var0, var1), var2), var3), var4), 0.2)
