import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser # Import the EarleyChartParser class from nltk.parse

# Define a simple CFG for theoretical computer science notation
cfg_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> DT NN | DT NN PP
    PP -> IN NP
    DT -> 'a' | 'the'
    NN -> 'machine' | 'algorithm' | 'state' | 'system'
    IN -> 'in' | 'with'
    VP -> V NP | V PP
    V -> 'is' | 'uses'
""")

def parse_sentence(sentence, parser):
    tokens = word_tokenize(sentence.lower())
    try:
        parses = list(parser.parse(tokens))
        return parses
    except ValueError:
        return []

def correct_sentence(sentence, parser):
    parses = parse_sentence(sentence, parser)
    if parses:
        return sentence  # If parsing succeeds, no correction is needed
    else:
        # Simple correction: return a default message for invalid sentences
        return "Syntax error detected. Please check the sentence structure."

def main():
    parser = EarleyChartParser(cfg_grammar) # Use EarleyChartParser instead of EarleyParser
    
    # Example usage
    input_sentence = "the machine is with algorithm"
    corrected_sentence = correct_sentence(input_sentence, parser)
    
    print("Original sentence:", input_sentence)
    print("Corrected sentence:", corrected_sentence)

if _name_ == "_main_":
  main()
