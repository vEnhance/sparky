import datetime
import config

# Color names {{{
TERM_COLOR = {}
TERM_COLOR["NORMAL"] = ""
TERM_COLOR["RESET"] = "\033[m"
TERM_COLOR["BOLD"] = "\033[1m"
TERM_COLOR["RED"] = "\033[31m"
TERM_COLOR["GREEN"] = "\033[32m"
TERM_COLOR["YELLOW"] = "\033[33m"
TERM_COLOR["BLUE"] = "\033[34m"
TERM_COLOR["MAGENTA"] = "\033[35m"
TERM_COLOR["CYAN"] = "\033[36m"
TERM_COLOR["BOLD_RED"] = "\033[1;31m"
TERM_COLOR["BOLD_GREEN"] = "\033[1;32m"
TERM_COLOR["BOLD_YELLOW"] = "\033[1;33m"
TERM_COLOR["BOLD_BLUE"] = "\033[1;34m"
TERM_COLOR["BOLD_MAGENTA"] = "\033[1;35m"
TERM_COLOR["BOLD_CYAN"] = "\033[1;36m"
TERM_COLOR["BG_RED"] = "\033[41m"
TERM_COLOR["BG_GREEN"] = "\033[42m"
TERM_COLOR["BG_YELLOW"] = "\033[43m"
TERM_COLOR["BG_BLUE"] = "\033[44m"
TERM_COLOR["BG_MAGENTA"] = "\033[45m"
TERM_COLOR["BG_CYAN"] = "\033[46m"
if config.USE_COLOR is False:
    for key in TERM_COLOR.keys():
        TERM_COLOR[key] = ""
# }}}

PROMPT_TEXT = (
    TERM_COLOR["BOLD_CYAN"]
    + "sparky"
    + TERM_COLOR["GREEN"]
    + ":) "
    + TERM_COLOR["RESET"]
)


def apply_color(color_name, s):
    return TERM_COLOR[color_name] + s + TERM_COLOR["RESET"]


WELCOME_STRING = apply_color("BOLD_YELLOW", "Welcome to Sparky!")
GOODBYE_STRING = apply_color("BOLD_YELLOW", "OK, goodbye! :D")


def is_valid(bet, **kwargs):
    """Determines whether to print a bet based on opts. Returns True or False"""
    if bet["weight"] != kwargs["weight"] and kwargs["weight"] is not None:
        return False
    if bet["outcome"] is not None and kwargs["display_resolved"] is False:
        return False
    if bet["outcome"] is None and kwargs["display_open"] is False:
        return False
    return True


def print_weight_header(w):
    print(apply_color("BOLD_BLUE", "{:=^70}".format("   {}% Bets   ".format(w))))


def print_bets(bets, **kwargs):
    if kwargs["weight"] is not None:
        print_weight_header(kwargs["weight"])
        valid_bets = [format_bet(bet) for bet in bets if is_valid(bet, **kwargs)]
        print("\n".join(valid_bets[-kwargs["limit"] :]))
    else:
        for w in config.WEIGHTS:
            valid_bets = [
                format_bet(bet)
                for bet in bets
                if is_valid(bet, **kwargs) and bet["weight"] == w
            ]
            if len(valid_bets) == 0:
                continue
            print_weight_header(w)
            print("\n".join(valid_bets[-kwargs["limit"] :]))


def format_time(t):
    return datetime.date.strftime(t, "%Y-%m-%d")


def format_bet(bet):
    if bet["outcome"] is False:
        the_outcome = apply_color("BOLD_RED", "x") + TERM_COLOR["BOLD_RED"]
    elif bet["outcome"] is True:
        the_outcome = apply_color("BOLD_GREEN", "*") + TERM_COLOR["BOLD_GREEN"]
    else:
        the_outcome = " " + TERM_COLOR["CYAN"]
    return "{ci}{i:>3}.  {outcome} {name:<50} {reset}{cdate}{date}{reset}".format(
        ci=TERM_COLOR["CYAN"],
        cdate=TERM_COLOR["MAGENTA"],
        reset=TERM_COLOR["RESET"],
        i=bet["index"],
        date=format_time(bet["birthdate"]),
        name=bet["name"],
        outcome=the_outcome,
    )


def print_stats(generator):
    for payload in generator:
        weight, accuracy, num_correct, num_incorrect = payload
        print(
            "{:>2}%   {ca}{:>7.2%}  {cc}{:>3} {cw}{:>3}{reset}".format(
                *payload,
                ca=TERM_COLOR["BOLD_MAGENTA"],
                cc=TERM_COLOR["GREEN"],
                cw=TERM_COLOR["RED"],
                reset=TERM_COLOR["RESET"],
            )
        )
