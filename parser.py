from config import WEIGHTS
from config import DEFAULT_LS_NUM, DEFAULT_STAT_NUM, MAX_NUM
import argparse

parser_add = argparse.ArgumentParser(prog="add", description="Adds a bet.")
parser_add.add_argument(
    "weight",
    type=int,
    choices=WEIGHTS,
    metavar="WEIGHT",
    help="Probability placed on bet.",
)
parser_add.add_argument(
    "broken_name",
    nargs="+",
    metavar="NAME",
    help="Description of the bet being placed (can contain spaces).",
)
parser_add.add_argument(
    "-o",
    "--outcome",
    type=int,
    choices=(-1, 0, 1),
    metavar="OUTCOME",
    help="If outcome has already been determined.",
)

parser_res = argparse.ArgumentParser(prog="resolve", description="Resolves a bet.")
parser_res.add_argument(
    "index", type=int, metavar="INDEX", help="The index of the bet being resolved."
)
parser_res.add_argument(
    "outcome",
    type=int,
    choices=(-1, 0, 1),
    metavar="RESULT",
    help="The outcome of the bet (-1,0,1).",
)

parser_ls = argparse.ArgumentParser(prog="ls", description="Lists bets and indices.")
parser_ls.add_argument(
    "-u",
    "--unresolved",
    action="store_const",
    dest="display_resolved",
    default=True,
    const=False,
    help="Lists only open bets.",
)
parser_ls.add_argument(
    "-o",
    "--open",
    action="store_const",
    dest="display_resolved",
    default=True,
    const=False,
    help="Synonym for -u.",
)
parser_ls.add_argument(
    "-r",
    "--resolved",
    action="store_const",
    dest="display_open",
    default=True,
    const=False,
    help="Lists only resolved bets.",
)
parser_ls.add_argument(
    "-w",
    "--weight",
    type=int,
    choices=WEIGHTS,
    metavar="WEIGHT",
    help="Limits displays to a given weight.",
)
parser_ls.add_argument(
    "-n",
    "--num",
    type=int,
    dest="limit",
    default=DEFAULT_LS_NUM,
    metavar="N",
    help="Limits to the last N bets.",
)
parser_ls.add_argument(
    "-a",
    "--all",
    action="store_const",
    dest="limit",
    const=MAX_NUM,
    help="Overrides -n and sets N = 2^48-1.",
)

parser_stat = argparse.ArgumentParser(prog="stat", description="Lists statistics.")
parser_stat.add_argument(
    "-n",
    "--num",
    type=int,
    dest="limit",
    default=DEFAULT_STAT_NUM,
    metavar="N",
    help="Limits to the last N bets.",
)
parser_stat.add_argument(
    "-a",
    "--all",
    action="store_const",
    dest="limit",
    const=MAX_NUM,
    help="Overrides -n and sets N = 2^48-1.",
)

parser_rm = argparse.ArgumentParser(
    prog="rm", description="Removes a bet or sequence of bets."
)
parser_rm.add_argument(
    "indices",
    type=int,
    nargs="+",
    metavar="INDEX",
    help="The indices of the bets to be removed.",
)

parser_edit = argparse.ArgumentParser(prog="edit", description="Edits a bet")
parser_edit.add_argument(
    "index", type=int, metavar="INDEX", help="The index of the bet being edited."
)
parser_edit.add_argument(
    "broken_name", nargs="+", metavar="NAME", help="New description of the bet."
)
