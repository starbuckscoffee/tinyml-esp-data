def add_vectors(v1, v2):
    return [sum(i) for i in zip(v1, v2)]
def mul_vector_number(v1, num):
    return [i * num for i in v1]
def score(input):
    if (input[75]) <= (-59.87022590637207):
        var0 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[72]) <= (5.287594437599182):
            if (input[12]) <= (-0.038307225331664085):
                if (input[66]) <= (-0.6907271444797516):
                    if (input[46]) <= (1.358778476715088):
                        var0 = [0.0, 0.0, 1.0, 0.0]
                    else:
                        var0 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var0 = [1.0, 0.0, 0.0, 0.0]
            else:
                if (input[14]) <= (10.122684955596924):
                    if (input[61]) <= (5.731718480587006):
                        var0 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        var0 = [0.0, 0.0, 1.0, 0.0]
                else:
                    if (input[122]) <= (10.086774826049805):
                        var0 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        if (input[67]) <= (2.232593387365341):
                            var0 = [1.0, 0.0, 0.0, 0.0]
                        else:
                            var0 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[45]) <= (1.8549616746604443):
                var0 = [0.0, 1.0, 0.0, 0.0]
            else:
                var0 = [0.0, 0.0, 0.0, 1.0]
    if (input[18]) <= (-3.7900209426879883):
        var1 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[91]) <= (-2.583343505859375):
            var1 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[66]) <= (2.050634026527405):
                var1 = [1.0, 0.0, 0.0, 0.0]
            else:
                if (input[46]) <= (0.606870174407959):
                    var1 = [0.0, 0.0, 1.0, 0.0]
                else:
                    var1 = [0.0, 1.0, 0.0, 0.0]
    if (input[42]) <= (6.155491232872009):
        if (input[61]) <= (1.4820110201835632):
            if (input[54]) <= (0.5626373887062073):
                if (input[66]) <= (3.5745434165000916):
                    if (input[87]) <= (1.90076345205307):
                        var2 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        if (input[49]) <= (1.0295066237449646):
                            var2 = [1.0, 0.0, 0.0, 0.0]
                        else:
                            var2 = [0.0, 0.0, 1.0, 0.0]
                else:
                    var2 = [0.0, 1.0, 0.0, 0.0]
            else:
                if (input[108]) <= (-0.1280898004770279):
                    var2 = [0.0, 1.0, 0.0, 0.0]
                else:
                    if (input[78]) <= (6.846220523118973):
                        var2 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        var2 = [0.0, 1.0, 0.0, 0.0]
        else:
            var2 = [0.0, 0.0, 1.0, 0.0]
    else:
        var2 = [0.0, 0.0, 0.0, 1.0]
    if (input[18]) <= (-2.8898014426231384):
        var3 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[91]) <= (-4.071340084075928):
            var3 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[31]) <= (0.09217675775289536):
                if (input[70]) <= (-1.458014965057373):
                    var3 = [1.0, 0.0, 0.0, 0.0]
                else:
                    if (input[116]) <= (10.190920352935791):
                        if (input[56]) <= (10.058039665222168):
                            var3 = [1.0, 0.0, 0.0, 0.0]
                        else:
                            var3 = [0.0, 1.0, 0.0, 0.0]
                    else:
                        var3 = [1.0, 0.0, 0.0, 0.0]
            else:
                if (input[61]) <= (0.9241617918014526):
                    if (input[96]) <= (-2.1320366263389587):
                        var3 = [0.0, 0.0, 1.0, 0.0]
                    else:
                        var3 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var3 = [0.0, 0.0, 1.0, 0.0]
    return mul_vector_number(add_vectors(add_vectors(add_vectors(var0, var1), var2), var3), 0.25)
