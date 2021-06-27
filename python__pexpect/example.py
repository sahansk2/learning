import pexpect

# pexpect: 
#   create a process, automate text input and read text output
#   knows nothing about processes (ex. doesn't capture program exit codes) but can serve well otherwise

# TLDR on how to use:
#   Declare .expect (when to stop listening to text stream)
#   Do something with
#       - child.after (what text did the expect regex match?)
#       - child.before (what was read before the expect regex?)
#   Based on result, use sendline/send (send new input)
#   Declare .expect
#   Repeat...


# Create a process
child = pexpect.spawn("python3 ./interactive-program.py")

# .expect(what): After reading *what* should the shell try to inject text?
child.expect(r'\(Cmd\) ')

# sendline: Send text appended with a newline, as if a person did it
child.sendline('greet')

# Will probably have side effects and output text...
# ...when should the program try to inject text/take other actions again? Use .expect again
child.expect(r'\(Cmd\) ')

# child.before: Everything up to before the expect pattern from the last run
print(child.before) # prints out the input text AND the result of the greeting command 

# send: Send text only
child.sendline('help\n')

child.expect(r'\(C.d\)')

print(child.before) # prints out help information
# child.after: Everything that *matched* the expect pattern
print(child.after) # Will have (Cmd) 

