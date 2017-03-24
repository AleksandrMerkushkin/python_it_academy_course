

def importOrReload(module_name, *names):
    import sys
    if module_name in sys.modules:
        reload(sys.modules[module_name])
    else:
        __import__(module_name, fromlist=names)


# if __name__=="__main__":
#     import sys
#     from reloader import importOrReload
#     importOrReload("test2")
#     sys.modules["test2"].A














    # for name in names:
    #     globals()[name] = getattr(sys.modules[module_name], name)

# use instead of: from dfly_parser import parseMessages
#importOrReload("test2", "f")
