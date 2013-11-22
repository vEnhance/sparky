import cmd
import display
import parser
import traceback

def get_options(parser, arg):
	# arg = "ls -a", for example
	if arg == '':
		return parser.parse_args([])
	else:
		return parser.parse_args(arg.split(' '))
def convert_outcome(n):
	assert n in (-1,0,1), "Bad outcome value"
	if n == 0: return False
	if n == 1: return True
	if n == -1: return None

class SparkyTerminal(cmd.Cmd):
	finished = False
	def postcmd(self, stop, line):
		return self.finished
	def emptyline(self):
		pass
	prompt = display.PROMPT_TEXT
	def set_manager(self, manager):
		self.manager = manager
	def run(self):
		print(display.WELCOME_STRING)
		while 1:
			try:
				self.cmdloop()
				break
			except KeyboardInterrupt:
				print("^C")
			except SystemExit:
				pass
			except:
				traceback.print_exc()
		print("\n" + display.GOODBYE_STRING)

	def do_EOF(self, arg):
		"""Ends the interactive session. One can also use ^D."""
		self.finished = True
	do_exit = do_EOF
	do_quit = do_EOF

	def do_add(self, arg):
		"""Adds a bet.  See add -h for syntax."""
		opts = get_options(parser.parser_add, arg)
		if opts is None: return
		kwargs = {}
		kwargs['name'] = ' '.join(opts.broken_name)
		kwargs['weight'] = opts.weight
		if opts.outcome is not None:
			kwargs['outcome'] = convert_outcome(opts.outcome)
		self.manager.add_bet(**kwargs)
		print(display.format_bet(self.manager.bets[-1]))
	do_bet = do_add
	def do_res(self, arg):
		"""Resolves a bet.  See res -h for syntax."""
		opts = get_options(parser.parser_res, arg)
		if opts is None: return
		outcome = convert_outcome(opts.outcome)
		index = opts.index
		self.manager.resolve_bet(index = index, outcome = outcome)
		print(display.format_bet(self.manager.bets[index]))
	do_resolve = do_res
	def do_ls(self, arg):
		"""Lists existing bets.  See ls -h for syntax."""
		opts = get_options(parser.parser_ls, arg)
		if opts is None: return
		weight = opts.weight
		display.print_bets(self.manager.bets, weight = weight,
				display_resolved = opts.display_resolved,
	 			display_open = opts.display_open,
				limit = opts.limit)
	def do_stat(self, arg):
		"""Prints statistics.  See stat -h for syntax."""
		opts = get_options(parser.parser_stat, arg)
		if opts is None: return
		display.print_stats(
				self.manager.provide_stats(limit = opts.limit))
	do_stats = do_stat
	def do_rm(self, arg):
		"""Deletes a bet.  See rm -h for syntax."""
		opts = get_options(parser.parser_rm, arg)
		if opts is None: return
		for index in reversed(sorted(opts.indices)):
			self.manager.rm_bet(index)
	do_del = do_rm
	def do_edit(self, arg):
		"""Edits the (text of) a bet.  See edit -h for syntax."""
		opts = get_options(parser.parser_edit, arg)
		name = ' '.join(opts.broken_name)
		index = opts.index
		self.manager.edit_bet(index = index, name = name)
		print(display.format_bet(self.manager.bets[index]))
