import argparse

# adding the program description
parser = argparse.ArgumentParser(description='Calculadora, '
                                             'suma/resta/multiplica a y b')

# adding positional parameters, type of variables, help about parameters and
# discrete values
parser.add_argument('-a', '--number_a', type=int, help='Parameter a')
parser.add_argument('-b', '--number_b', type=int, help='Parameter b')
parser.add_argument('-o', '--operation', type=str, choices=['suma', 'resta',
                    'multiplicacion'], default='suma', required=False,
                    help='Operación a realize con a y b')

# Passing the arguments
args = parser.parse_args()
variables = vars(args)
print(variables)

if args.operation == 'suma':
    print(args.number_a + args.number_b)
elif args.operation == 'resta':
    print(args.number_a - args.number_b)
elif args.operation == 'multiplicacion':
    print(args.number_a * args.number_b)


