def add_vectors(v1, v2):
    return [sum(i) for i in zip(v1, v2)]
def mul_vector_number(v1, num):
    return [i * num for i in v1]
def score(input):
    if (input[229]) <= (-3.192668080329895):
        if (input[305]) <= (-47.02289867401123):
            var0 = [0.0, 0.0, 0.0, 1.0]
        else:
            var0 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[126]) <= (1.410184919834137):
            if (input[253]) <= (-2.5151090025901794):
                if (input[22]) <= (1.748091459274292):
                    var0 = [0.0, 0.0, 1.0, 0.0]
                else:
                    var0 = [0.0, 0.0, 0.0, 1.0]
            else:
                var0 = [1.0, 0.0, 0.0, 0.0]
        else:
            if (input[64]) <= (0.5610686987638474):
                var0 = [0.0, 0.0, 1.0, 0.0]
            else:
                var0 = [0.0, 1.0, 0.0, 0.0]
    if (input[156]) <= (3.671508550643921):
        if (input[121]) <= (2.5605984926223755):
            if (input[84]) <= (-3.162740468978882):
                var1 = [0.0, 0.0, 0.0, 1.0]
            else:
                var1 = [1.0, 0.0, 0.0, 0.0]
        else:
            if (input[495]) <= (-1.6717554926872253):
                var1 = [0.0, 0.0, 0.0, 1.0]
            else:
                var1 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[214]) <= (-41.034350633621216):
            var1 = [0.0, 0.0, 0.0, 1.0]
        else:
            if (input[446]) <= (10.21007490158081):
                var1 = [0.0, 1.0, 0.0, 0.0]
            else:
                var1 = [0.0, 0.0, 1.0, 0.0]
    if (input[241]) <= (-2.2002710700035095):
        if (input[339]) <= (-14.534354269504547):
            var2 = [0.0, 0.0, 0.0, 1.0]
        else:
            var2 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[258]) <= (-3.519476532936096):
            var2 = [0.0, 1.0, 0.0, 0.0]
        else:
            if (input[97]) <= (1.8507174253463745):
                if (input[270]) <= (5.012261092662811):
                    var2 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var2 = [0.0, 1.0, 0.0, 0.0]
            else:
                var2 = [0.0, 0.0, 1.0, 0.0]
    if (input[235]) <= (-1.318008005619049):
        if (input[351]) <= (-11.545801520347595):
            var3 = [0.0, 0.0, 0.0, 1.0]
        else:
            if (input[132]) <= (5.67545485496521):
                if (input[291]) <= (-0.9694656431674957):
                    var3 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var3 = [0.0, 0.0, 1.0, 0.0]
            else:
                var3 = [0.0, 1.0, 0.0, 0.0]
    else:
        if (input[216]) <= (-1.0678139925003052):
            if (input[94]) <= (2.824427545070648):
                var3 = [0.0, 1.0, 0.0, 0.0]
            else:
                var3 = [1.0, 0.0, 0.0, 0.0]
        else:
            if (input[103]) <= (2.2134395241737366):
                if (input[162]) <= (6.357802510261536):
                    var3 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var3 = [0.0, 1.0, 0.0, 0.0]
            else:
                var3 = [0.0, 0.0, 1.0, 0.0]
    return mul_vector_number(add_vectors(add_vectors(add_vectors(var0, var1), var2), var3), 0.25)
