def add_vectors(v1, v2):
    return [sum(i) for i in zip(v1, v2)]
def mul_vector_number(v1, num):
    return [i * num for i in v1]
def score(input):
    if (input[6]) <= (-1.5478515028953552):
        if (input[39]) <= (-40.73282432556152):
            var0 = [0.0, 0.0, 0.0, 1.0]
        else:
            var0 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[43]) <= (-3.645172119140625):
            var0 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[54]) <= (-3.4296940565109253):
                var0 = [0.0, 1.0, 0.0, 0.0]
            else:
                if (input[37]) <= (2.773682415485382):
                    if (input[53]) <= (14.862594604492188):
                        var0 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        if (input[43]) <= (1.720233976840973):
                            if (input[42]) <= (-14.955379962921143):
                                var0 = [0.0, 1.0, 0.0, 0.0]
                            else:
                                var0 = [1.0, 0.0, 0.0, 0.0]
                        else:
                            var0 = [0.0, 1.0, 0.0, 0.0]
                else:
                    if (input[38]) <= (10.66137981414795):
                        var0 = [0.0, 0.0, 1.0, 0.0]
                    else:
                        var0 = [0.0, 1.0, 0.0, 0.0]
    if (input[6]) <= (-1.5478515028953552):
        if (input[26]) <= (7.443572998046875):
            var1 = [0.0, 0.0, 0.0, 1.0]
        else:
            var1 = [1.0, 0.0, 0.0, 0.0]
    else:
        if (input[43]) <= (-3.897760033607483):
            var1 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[18]) <= (0.5027822852134705):
                if (input[42]) <= (1.5011644959449768):
                    if (input[45]) <= (-3.3664119243621826):
                        if (input[48]) <= (-2.5737670063972473):
                            var1 = [0.0, 1.0, 0.0, 0.0]
                        else:
                            var1 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        var1 = [1.0, 0.0, 0.0, 0.0]
                else:
                    if (input[7]) <= (0.3040636032819748):
                        var1 = [0.0, 1.0, 0.0, 0.0]
                    else:
                        var1 = [0.0, 0.0, 1.0, 0.0]
            else:
                if (input[23]) <= (-7.709923028945923):
                    var1 = [1.0, 0.0, 0.0, 0.0]
                else:
                    if (input[40]) <= (13.503816843032837):
                        var1 = [0.0, 1.0, 0.0, 0.0]
                    else:
                        var1 = [1.0, 0.0, 0.0, 0.0]
    if (input[18]) <= (3.1376015543937683):
        if (input[31]) <= (1.4820110201835632):
            if (input[34]) <= (-0.9274809807538986):
                var2 = [1.0, 0.0, 0.0, 0.0]
            else:
                if (input[3]) <= (-0.6793892979621887):
                    if (input[9]) <= (1.1221371293067932):
                        if (input[31]) <= (0.23582889884710312):
                            var2 = [0.0, 1.0, 0.0, 0.0]
                        else:
                            if (input[19]) <= (0.42018238455057144):
                                if (input[50]) <= (9.4930100440979):
                                    var2 = [0.0, 1.0, 0.0, 0.0]
                                else:
                                    var2 = [1.0, 0.0, 0.0, 0.0]
                            else:
                                var2 = [0.0, 0.0, 1.0, 0.0]
                    else:
                        var2 = [1.0, 0.0, 0.0, 0.0]
                else:
                    if (input[48]) <= (-2.7210104167461395):
                        var2 = [0.0, 1.0, 0.0, 0.0]
                    else:
                        var2 = [1.0, 0.0, 0.0, 0.0]
        else:
            var2 = [0.0, 0.0, 1.0, 0.0]
    else:
        var2 = [0.0, 0.0, 0.0, 1.0]
    if (input[25]) <= (-2.3271644711494446):
        if (input[7]) <= (-0.020350754261016846):
            var3 = [1.0, 0.0, 0.0, 0.0]
        else:
            var3 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[31]) <= (1.8171990513801575):
            if (input[36]) <= (4.377797901630402):
                if (input[44]) <= (10.465054988861084):
                    var3 = [1.0, 0.0, 0.0, 0.0]
                else:
                    if (input[59]) <= (11.103055000305176):
                        var3 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        if (input[55]) <= (-3.5158849954605103):
                            var3 = [0.0, 0.0, 1.0, 0.0]
                        else:
                            var3 = [1.0, 0.0, 0.0, 0.0]
            else:
                var3 = [0.0, 1.0, 0.0, 0.0]
        else:
            var3 = [0.0, 0.0, 1.0, 0.0]
    return mul_vector_number(add_vectors(add_vectors(add_vectors(var0, var1), var2), var3), 0.25)
