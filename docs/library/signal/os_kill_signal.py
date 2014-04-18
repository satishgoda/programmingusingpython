import os
import signal


pid = ......


os.kill(pid, signal.SIGINT)

# Freezes aspp
os.kill(2152, signal.SIGSTOP)

# Unfreezes app
os.kill(2152, signal.SIGCONT)

# kill -9
os.kill(2152, signal.SIGKILL)
