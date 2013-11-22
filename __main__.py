from config import DATA_PATH
import model
import term
import sys

if __name__ == "__main__":
	manager = model.Manager(DATA_PATH) # start model
	cmd = term.SparkyTerminal()
	cmd.set_manager(manager)
	if len(sys.argv) == 1:
		cmd.run() # No argument, so start interactive mode
	else:
		cmd.onecmd(' '.join(sys.argv[1:]))
