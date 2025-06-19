# 1. Global Scope
# A variable defined outside any function or class is in the global scope.
# It can be accessed from anywhere in the module.
global_var = "I am a global variable!"

def outer_function():
    # 2. Enclosing Function Local Scope (or Nonlocal Scope for inner functions)
    # This variable 'my_var' is local to outer_function.
    # It shadows the global_var for code within outer_function and its nested functions.
    my_var = "I am an enclosing function's variable!"
    print(f"Inside outer_function: my_var = '{my_var}'")
    print(f"Inside outer_function: global_var = '{global_var}' (Accessed from global scope)")

    def inner_function():
        # 3. Local Scope
        # This variable 'my_var' is local to inner_function.
        # It shadows the 'my_var' from outer_function.
        # If 'my_var' were not defined here, Python would look for it in the enclosing scope (outer_function).
        my_var = "I am a local variable in inner_function!"
        print(f"\nInside inner_function: my_var = '{my_var}' (Local to inner_function)")

        # Accessing the variable from the enclosing scope using 'nonlocal' (if we wanted to modify it)
        # Without 'nonlocal', assigning to 'my_var' here would create a new local variable.
        # To access the 'my_var' from outer_function (enclosing scope) without modifying it,
        # we just refer to it directly if it wasn't shadowed locally.
        # However, since we *did* redefine 'my_var' locally, we need to be explicit.
        # To demonstrate accessing the enclosing 'my_var' without 'nonlocal' (if the local one didn't exist):
        # Let's add another variable to show the lookup.

        # Python's LEGB Rule in action:
        # L (Local): Python first looks for 'my_var' in the current (local) scope of inner_function.
        #            It finds "I am a local variable in inner_function!".

        # E (Enclosing function locals): If not found locally, it looks in the enclosing scope(s).
        #            If 'my_var' wasn't in inner_function, it would find "I am an enclosing function's variable!".

        # G (Global): If not found in local or enclosing scopes, it looks in the global scope.
        #            'global_var' is found directly here.
        print(f"Inside inner_function: global_var = '{global_var}' (Accessed from global scope)")

        # To specifically access the 'my_var' from the enclosing scope (outer_function) from here,
        # when it's shadowed by a local 'my_var', it's not directly possible without 'nonlocal'
        # if you want to *modify* it. To *read* it, if it wasn't shadowed, Python's LEGB would find it.
        # Since it *is* shadowed, we can't easily refer to the enclosing `my_var` without `nonlocal`
        # and if `my_var` were assigned here, it would create a new local variable.

        # Let's demonstrate accessing the enclosing variable name, if it wasn't re-declared locally
        # This block shows the LEGB rule more clearly for the 'enclosing_only_var'
        enclosing_only_var = "This var is from outer_function, seen by inner_function if not shadowed."
        print(f"Inside inner_function (trying to find enclosing_only_var): This would be found by LEGB if it wasn't shadowed.")
        # If we had:
        # # my_var = "I am an enclosing function's variable!" (in outer_function)
        # # inner_function:
        # #   print(my_var) # This would print "I am an enclosing function's variable!"

        # Let's add a variable that is only in the enclosing scope, to clearly show the E in LEGB.
        enclosing_exclusive_var = "I am exclusively in outer_function's scope."
        print(f"Inside inner_function: Accessing a variable exclusive to outer_function:")
        try:
            # This will raise an error because 'enclosing_exclusive_var' is not in inner_function's scope
            # and it's not defined at the time inner_function is *defined*. It's defined during
            # outer_function's *execution*. This is a common point of confusion.
            # Python resolves names based on where the function is DEFINED, not where it's CALLED.
            print(f"  Attempting to access enclosing_exclusive_var: {enclosing_exclusive_var}")
        except NameError as e:
            print(f"  Error accessing 'enclosing_exclusive_var' directly here: {e}")
            print(f"  Reason: 'enclosing_exclusive_var' is created during outer_function's execution,")
            print(f"  not present in the scope when inner_function is defined, thus not 'enclosing'.")
            print(f"  To truly show 'E', let's use a variable from 'outer_function' that 'inner_function' can see.")


    # Call the inner function
    inner_function()

# Call the outer function
outer_function()

print(f"\nOutside all functions: global_var = '{global_var}'")
# print(my_var) # This would cause a NameError because my_var is not in the global scope.

# How Python Follows the LEGB Rule for Variable Lookup:
# When Python tries to find the value of a variable name, it follows a specific order:
# 1.  L (Local): It first looks in the innermost scope, which is the local scope of the current function.
#     -   If the variable is assigned a value within the function (e.g., `my_var = "..."`), it's local.
# 2.  E (Enclosing function locals): If the variable isn't found in the local scope, Python checks the
#     local scopes of any enclosing (nested) functions, from innermost to outermost.
#     -   This applies to nested functions. If `inner_function` references a variable not in its
#         own scope, it will look in `outer_function`'s scope.
# 3.  G (Global): If the variable isn't found in any of the enclosing scopes, Python looks in the
#     global scope (the module level where the script is running).
#     -   Variables defined at the top level of a `.py` file are in the global scope.
# 4.  B (Built-in): Finally, if the variable isn't found in the global scope, Python checks the
#     built-in scope, which contains names like `print`, `len`, `str`, etc.
#
# If the variable is not found in any of these scopes, a `NameError` is raised.

# In this example:
# - `global_var` is found in the G (Global) scope from anywhere.
# - The `my_var` inside `outer_function` is in the E (Enclosing) scope relative to `inner_function`.
# - The `my_var` inside `inner_function` is in the L (Local) scope relative to itself,
#   and it *shadows* the `my_var` from `outer_function`. This means when `inner_function`
#   looks for `my_var`, it finds its own local version first, before checking the enclosing scope.
