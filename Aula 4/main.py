#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

import argparse
import random
import time
import curses
from collections import namedtuple
from pprint import pprint

#     Para um teste de tempo máximo de 60 segundos: ./main.py -utm -mv 60
#     Para um teste de número máximo de inputs (por exemplo, 50): ./main.py -mv 50
#     Para usar palavras em vez de caracteres únicos: ./main.py -utm -mv 60 -uw

Input = namedtuple('Input', ['requested', 'received', 'duration'])

def generate_random_letter():
    return random.choice('abcdefghijklmnopqrstuvwxyz')

def generate_random_word():
    words = ['apple', 'banana', 'orange', 'grape', 'python', 'programming', 'challenge', 'keyboard']
    return random.choice(words)

def main(stdscr, args):
    stdscr.clear()
    stdscr.addstr("Pressione qualquer tecla para começar o desafio...")
    stdscr.getch()

    test_start = time.strftime('%c')

    inputs = []
    number_of_types = 0
    number_of_hits = 0
    start_time = time.time()

    while True:
        stdscr.clear()
        if args.use_words:
            requested_word = generate_random_word()
        else:
            requested_word = generate_random_letter()

        stdscr.addstr(f"Digite: {requested_word}")
        stdscr.refresh()

        start_input_time = time.time()
        received_word = stdscr.getkey()
        end_input_time = time.time()
        input_duration = end_input_time - start_input_time

        input_data = Input(requested_word, received_word, input_duration)
        inputs.append(input_data)

        number_of_types += 1
        if requested_word == received_word:
            number_of_hits += 1

        if received_word == ' ':
            break

        if args.use_time_mode:
            if time.time() - start_time > args.max_value:
                break
        else:
            if number_of_types >= args.max_value:
                break

    test_end = time.strftime('%c')
    test_duration = time.time() - start_time

    accuracy = number_of_hits / number_of_types if number_of_types > 0 else 0
    type_average_duration = test_duration / number_of_types if number_of_types > 0 else 0
    type_hit_average_duration = sum([input_data.duration for input_data in inputs if input_data.requested == input_data.received and input_data.duration > 0]) / number_of_hits if number_of_hits > 0 else 0
    type_miss_average_duration = sum([input_data.duration for input_data in inputs if input_data.requested != input_data.received and input_data.duration > 0]) / (number_of_types - number_of_hits) if (number_of_types - number_of_hits) > 0 else 0


    result_dict = {
        'test_start': test_start,
        'test_end': test_end,
        'test_duration': test_duration,
        'number_of_types': number_of_types,
        'number_of_hits': number_of_hits,
        'accuracy': accuracy,
        'type_average_duration': type_average_duration,
        'type_hit_average_duration': type_hit_average_duration,
        'type_miss_average_duration': type_miss_average_duration,
        'inputs': inputs
    }

    stdscr.clear()
    stdscr.addstr("Teste Concluído!\n\n")
    #stdscr.refresh()
    #time.sleep(1)

    pprint(result_dict)

    # Imprimindo a lista final com todos os parâmetros e valores
    final_list = [f"{key}: {value}" for key, value in result_dict.items()]
    stdscr.addstr("\nLista Final:\n")
    stdscr.addstr("\n".join(final_list))
    stdscr.refresh()

    stdscr.getch()  # Espera que o usuário pressione uma tecla antes de sair

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Definition of test mode')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', help='Max number of secs for time mode')
    parser.add_argument('-mv', '--max_value', type=int, help='Max number of seconds for time mode or maximum number of inputs for number of inputs mode.')
    parser.add_argument('-uw', '--use_words', action='store_true', help='Use word typing mode, instead of single character typing.')
    args = parser.parse_args()

    curses.wrapper(main, args)







