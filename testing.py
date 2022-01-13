import colorama
from colorama import Fore


def colored_alphabet(hits: set[str], misses: set[str]) -> str:
        """ 
        Returns a string of letters of alphabet, color coded by hit, 
        miss or unknown
        """
        def color_and_char(ascii_code: int) -> str:
            char = chr(ascii_code)
            color = Fore.GREEN if char in hits \
                else Fore.RED if char in misses \
                else Fore.LIGHTBLACK_EX
            return color + char
        return ''.join(color_and_char(ascii_code) for ascii_code in 
            range(ord('A'), ord('Z') + 1))

print(colored_alphabet)