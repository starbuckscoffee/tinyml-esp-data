def add_vectors(v1, v2):
    return [sum(i) for i in zip(v1, v2)]
def mul_vector_number(v1, num):
    return [i * num for i in v1]
def score(input):
    if (input[75]) <= (-59.87022590637207):
        var0 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[43]) <= (1.5693994760513306):
            if (input[109]) <= (0.09816226921975613):
                if (input[36]) <= (0.5949591398239136):
                    if (input[91]) <= (0.780509740114212):
                        var0 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        if (input[113]) <= (-4.580152690410614):
                            var0 = [1.0, 0.0, 0.0, 0.0]
                        else:
                            var0 = [0.0, 1.0, 0.0, 0.0]
                else:
                    if (input[15]) <= (37.721368715167046):
                        var0 = [0.0, 1.0, 0.0, 0.0]
                    else:
                        var0 = [1.0, 0.0, 0.0, 0.0]
            else:
                if (input[70]) <= (22.992369651794434):
                    var0 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var0 = [0.0, 0.0, 0.0, 1.0]
        else:
            if (input[7]) <= (0.047884028404951096):
                var0 = [0.0, 1.0, 0.0, 0.0]
            else:
                var0 = [0.0, 0.0, 1.0, 0.0]
    if (input[18]) <= (-3.7900209426879883):
        var1 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[84]) <= (-0.591367781162262):
            if (input[54]) <= (3.9061397910118103):
                var1 = [1.0, 0.0, 0.0, 0.0]
            else:
                var1 = [0.0, 1.0, 0.0, 0.0]
        else:
            if (input[71]) <= (-9.572516441345215):
                if (input[43]) <= (2.1188685297966003):
                    if (input[68]) <= (9.689334392547607):
                        var1 = [0.0, 1.0, 0.0, 0.0]
                    else:
                        var1 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var1 = [0.0, 0.0, 1.0, 0.0]
            else:
                if (input[67]) <= (-4.940435528755188):
                    var1 = [0.0, 0.0, 1.0, 0.0]
                else:
                    if (input[79]) <= (-8.565256834030151):
                        var1 = [0.0, 0.0, 1.0, 0.0]
                    else:
                        var1 = [1.0, 0.0, 0.0, 0.0]
    if (input[42]) <= (9.537301301956177):
        if (input[61]) <= (-3.2273834943771362):
            if (input[80]) <= (9.97424602508545):
                var2 = [0.0, 1.0, 0.0, 0.0]
            else:
                var2 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[61]) <= (2.249352514743805):
                if (input[36]) <= (0.4321534037590027):
                    if (input[49]) <= (6.708551645278931):
                        var2 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        var2 = [0.0, 0.0, 1.0, 0.0]
                else:
                    if (input[10]) <= (2.625954031944275):
                        var2 = [0.0, 1.0, 0.0, 0.0]
                    else:
                        var2 = [1.0, 0.0, 0.0, 0.0]
            else:
                var2 = [0.0, 0.0, 1.0, 0.0]
    else:
        if (input[29]) <= (21.545801401138306):
            var2 = [0.0, 1.0, 0.0, 0.0]
        else:
            var2 = [0.0, 0.0, 0.0, 1.0]
    if (input[18]) <= (-2.8898014426231384):
        var3 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[49]) <= (2.9879640340805054):
            if (input[61]) <= (-0.5793967843055725):
                if (input[42]) <= (1.6723496913909912):
                    var3 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var3 = [0.0, 1.0, 0.0, 0.0]
            else:
                if (input[36]) <= (0.6332663297653198):
                    var3 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var3 = [0.0, 1.0, 0.0, 0.0]
        else:
            if (input[64]) <= (-4.465649127960205):
                var3 = [0.0, 1.0, 0.0, 0.0]
            else:
                var3 = [0.0, 0.0, 1.0, 0.0]
    return mul_vector_number(add_vectors(add_vectors(add_vectors(var0, var1), var2), var3), 0.25)
