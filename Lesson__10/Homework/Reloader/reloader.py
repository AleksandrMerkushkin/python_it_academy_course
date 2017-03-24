

def importOrReload(module_name, *names):
    import sys
    if module_name in sys.modules:
        reload(sys.modules[module_name])
    else:
        __import__(module_name, fromlist=names)


if __name__=="__main__":
    import sys
    from reloader import importOrReload
    importOrReload("test2")
    sys.modules["test2"].A


