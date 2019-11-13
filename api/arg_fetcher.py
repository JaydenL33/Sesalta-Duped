# Helper function to extract the value of an arg from the given args.
# Params:
# args: all args
# param_name: the name of the argument to be returned
# required: determines whether an exception will be raised if the argument
# is not found.


def get_arg(args, param_name, required=False, default=None):
    if param_name in args:
        return args[param_name]
    elif required == True:
        raise ParameterNotFoundError(param_name, args)
    else:
        return None
