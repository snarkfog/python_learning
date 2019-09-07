# is_ready = True
is_ready = False

if is_ready:
    state_msg = "Ready"
else:
    state_msg = "Not ready yet"

print(state_msg)

# and/or
is_ready = True
#is_ready = False

state_msg = is_ready and "Ready" or "Not ready yet"

print(state_msg)

# Тернарный оператор
# is_ready = True
is_ready = False

state_msg = "Ready" if is_ready else "Not ready yet"

print(state_msg)

# Тернарный оператор, вариант №2
is_ready = True
# is_ready = False

print("Ready" if is_ready else "Not ready yet")
