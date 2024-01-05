import re

def split_into_syllables(word):
    # Define regular expressions for vowels and consonants
    vowels = 'ae'
    consonants = 'bcd'

    # Define patterns for syllables (CV or CVC)
    cv_pattern = f"([{consonants}][{vowels}])"
    cvc_pattern = f"[{consonants}][{vowels}][{consonants}]"

    # Combine patterns to match either CV or CVC syllables
    syllable_pattern = f"({cv_pattern}|{cvc_pattern})"

    # Use regex to find syllables in the word
    syllables = re.findall(syllable_pattern, word)

    # Join syllables with dots to represent boundaries
    result = '.'.join(syllables)

    return result

# Example usage
word = "bacedbab"
syllables_result = split_into_syllables(word)
print(syllables_result)
