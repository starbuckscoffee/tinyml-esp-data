def add_vectors(v1, v2):
    return [sum(i) for i in zip(v1, v2)]
def mul_vector_number(v1, num):
    return [i * num for i in v1]
def score(input):
    if (input[68]) <= (5.029020547866821):
        var0 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[132]) <= (0.06344634480774403):
            if (input[120]) <= (-0.9289501309394836):
                var0 = [0.0, 1.0, 0.0, 0.0]
            else:
                if (input[96]) <= (-1.933318018913269):
                    var0 = [0.0, 1.0, 0.0, 0.0]
                else:
                    var0 = [1.0, 0.0, 0.0, 0.0]
        else:
            if (input[31]) <= (0.14844050258398056):
                var0 = [1.0, 0.0, 0.0, 0.0]
            else:
                if (input[85]) <= (-2.94845911860466):
                    var0 = [0.0, 0.0, 1.0, 0.0]
                else:
                    if (input[55]) <= (10.286387205123901):
                        var0 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        var0 = [0.0, 0.0, 1.0, 0.0]
    if (input[62]) <= (7.161057472229004):
        if (input[32]) <= (10.105924129486084):
            var1 = [1.0, 0.0, 0.0, 0.0]
        else:
            var1 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[54]) <= (2.0925320386886597):
            if (input[85]) <= (-5.602432310581207):
                var1 = [0.0, 0.0, 1.0, 0.0]
            else:
                if (input[49]) <= (10.7748042345047):
                    if (input[36]) <= (0.23942014575004578):
                        var1 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        if (input[67]) <= (4.6842557191848755):
                            var1 = [1.0, 0.0, 0.0, 0.0]
                        else:
                            var1 = [0.0, 0.0, 1.0, 0.0]
                else:
                    var1 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[126]) <= (0.06344634294509888):
                var1 = [0.0, 1.0, 0.0, 0.0]
            else:
                var1 = [0.0, 0.0, 1.0, 0.0]
    if (input[58]) <= (-37.6068696975708):
        var2 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[126]) <= (-0.16639699786901474):
            if (input[114]) <= (-0.49559973180294037):
                if (input[90]) <= (-1.5023615919053555):
                    var2 = [0.0, 1.0, 0.0, 0.0]
                else:
                    var2 = [1.0, 0.0, 0.0, 0.0]
            else:
                if (input[54]) <= (1.9680339097976685):
                    var2 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var2 = [0.0, 1.0, 0.0, 0.0]
        else:
            if (input[9]) <= (-0.3206106945872307):
                if (input[55]) <= (1.8064250349998474):
                    if (input[7]) <= (-0.003591302433051169):
                        if (input[141]) <= (2.324427545070648):
                            var2 = [0.0, 1.0, 0.0, 0.0]
                        else:
                            var2 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        var2 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var2 = [0.0, 0.0, 1.0, 0.0]
            else:
                var2 = [1.0, 0.0, 0.0, 0.0]
    if (input[68]) <= (5.029020547866821):
        var3 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[79]) <= (-5.8418519496917725):
            var3 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[54]) <= (2.0925320386886597):
                if (input[97]) <= (-5.585672497749329):
                    var3 = [0.0, 0.0, 1.0, 0.0]
                else:
                    var3 = [1.0, 0.0, 0.0, 0.0]
            else:
                var3 = [0.0, 1.0, 0.0, 0.0]
    return mul_vector_number(add_vectors(add_vectors(add_vectors(var0, var1), var2), var3), 0.25)
