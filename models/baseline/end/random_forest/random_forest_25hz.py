def add_vectors(v1, v2):
    return [sum(i) for i in zip(v1, v2)]
def mul_vector_number(v1, num):
    return [i * num for i in v1]
def score(input):
    if (input[68]) <= (5.029020547866821):
        var0 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[67]) <= (1.039083480834961):
            if (input[120]) <= (-2.5737670063972473):
                var0 = [0.0, 1.0, 0.0, 0.0]
            else:
                if (input[96]) <= (-0.6117185354232788):
                    if (input[153]) <= (0.7137402594089508):
                        if (input[29]) <= (-56.43512010574341):
                            var0 = [1.0, 0.0, 0.0, 0.0]
                        else:
                            var0 = [0.0, 0.0, 1.0, 0.0]
                    else:
                        var0 = [1.0, 0.0, 0.0, 0.0]
                else:
                    if (input[12]) <= (0.008379704784601927):
                        var0 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        if (input[121]) <= (-3.2202008962631226):
                            var0 = [0.0, 0.0, 1.0, 0.0]
                        else:
                            var0 = [1.0, 0.0, 0.0, 0.0]
        else:
            if (input[33]) <= (-9.805343627929688):
                var0 = [1.0, 0.0, 0.0, 0.0]
            else:
                var0 = [0.0, 0.0, 1.0, 0.0]
    if (input[62]) <= (6.321889400482178):
        var1 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[78]) <= (1.3407530188560486):
            if (input[54]) <= (0.10534487664699554):
                if (input[85]) <= (4.841075658798218):
                    var1 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var1 = [0.0, 0.0, 1.0, 0.0]
            else:
                if (input[139]) <= (-0.15562312118709087):
                    var1 = [1.0, 0.0, 0.0, 0.0]
                else:
                    if (input[94]) <= (-1.1984731554985046):
                        var1 = [1.0, 0.0, 0.0, 0.0]
                    else:
                        var1 = [0.0, 0.0, 1.0, 0.0]
        else:
            if (input[67]) <= (0.8295910060405731):
                if (input[17]) <= (-8.236639022827148):
                    var1 = [1.0, 0.0, 0.0, 0.0]
                else:
                    var1 = [0.0, 1.0, 0.0, 0.0]
            else:
                var1 = [0.0, 0.0, 1.0, 0.0]
    if (input[58]) <= (-46.01144886016846):
        var2 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[76]) <= (-0.645038079470396):
            var2 = [1.0, 0.0, 0.0, 0.0]
        else:
            if (input[114]) <= (-5.020640969276428):
                if (input[90]) <= (3.6439752876758575):
                    var2 = [0.0, 0.0, 1.0, 0.0]
                else:
                    var2 = [0.0, 1.0, 0.0, 0.0]
            else:
                if (input[54]) <= (-0.06224924139678478):
                    if (input[127]) <= (-2.5318684577941895):
                        var2 = [0.0, 0.0, 1.0, 0.0]
                    else:
                        var2 = [1.0, 0.0, 0.0, 0.0]
                else:
                    if (input[76]) <= (3.5305346250534058):
                        if (input[89]) <= (-20.465649604797363):
                            if (input[141]) <= (41.58778864145279):
                                var2 = [0.0, 1.0, 0.0, 0.0]
                            else:
                                var2 = [1.0, 0.0, 0.0, 0.0]
                        else:
                            var2 = [0.0, 0.0, 1.0, 0.0]
                    else:
                        var2 = [1.0, 0.0, 0.0, 0.0]
    if (input[91]) <= (1.539471983909607):
        if (input[25]) <= (1.7298104763031006):
            if (input[114]) <= (-1.0869677662849426):
                if (input[2]) <= (10.245989799499512):
                    var3 = [0.0, 1.0, 0.0, 0.0]
                else:
                    var3 = [0.0, 0.0, 0.0, 1.0]
            else:
                var3 = [1.0, 0.0, 0.0, 0.0]
        else:
            var3 = [0.0, 0.0, 0.0, 1.0]
    else:
        if (input[55]) <= (0.17956510186195374):
            if (input[8]) <= (10.131064891815186):
                var3 = [0.0, 0.0, 0.0, 1.0]
            else:
                var3 = [0.0, 1.0, 0.0, 0.0]
        else:
            var3 = [0.0, 0.0, 1.0, 0.0]
    return mul_vector_number(add_vectors(add_vectors(add_vectors(var0, var1), var2), var3), 0.25)
