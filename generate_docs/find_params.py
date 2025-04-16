def print_param_info(func, func_name, f):  # Add file parameter
    try:
        func()
        f.write("%s() takes exactly 0 arguments\n" % func_name)
        return
    except TypeError, e:
        err = str(e)
        if "takes exactly" in err:
            num_params = int(err.split("takes exactly")[1].split("argument")[0].strip())
            f.write("%s() takes exactly %d arguments\n" % (func_name, num_params))
        else:
            print(err)
            f.write("%s() takes unknown arguments\n" % func_name)
            return

    for i in range(num_params):
        args = [0] * num_params
        args[i] = None
        try:
            func(*args)
        except TypeError, e:
            err = str(e).lower()
            if "integer is required" in err or "int" in err:
                f.write("%s() argument %d must be int\n" % (func_name, i + 1))
            elif "string is required" in err or "str" in err:
                f.write("%s() argument %d must be str\n" % (func_name, i + 1))
            elif "float is required" in err:
                f.write("%s() argument %d must be float\n" % (func_name, i + 1))
            else:
                f.write("%s() argument %d must be %s \n" % (func_name, i + 1, err))


# Add file opening before the loop
try:
    import osl
    osl.initGfx()
    img = osl.Image((10, 10), osl.IN_VRAM, osl.PF_5551)
    print(dir(img))
    f = open('osl_params.txt', 'w')
    for attr_name in dir(img):
        print(attr_name)
        attr = getattr(img, attr_name)
        if hasattr(attr, '__call__'):
            print_param_info(attr, attr_name, f)  # Pass file to function
    # attr_name = "printxy"
    # attr = getattr(osl, attr_name)            
    # print_param_info(attr, attr_name, f)
except ImportError:
    f = open('osl_params.txt', 'w')
    f.write("Error: osl module not available\n")
