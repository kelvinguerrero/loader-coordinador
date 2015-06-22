__author__ = 'kelvin'
from loader.loadercoordinador import *
import os
import argparse

def main():
    if len(args) == 2:
        if args[0] == "estudiantes" and args[1] != None:
            if ".csv" in args[1]:
                cargar_estudiantes(args[1])
            else:
                print "Error en el formato del archivo"
        else:
            print ("Error en los parametros de entrada")
    elif len(args) ==1:
        if 'estudiantes' in args:
            cargar_estudiantes_general( )
        elif 'graduados' in args:
            cargar_estudiantes_graduados( )
        else:
            print "comando incorrecto"
    else:
        print ("Solo se aceptan uno o dos parametros de entrada")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--load', default='', type=str, help='kind of load to do.')
    parser.add_argument('-o','--ofile', default='', type=str, help='File to save the project.')
    parser.add_argument('-u','--utestlink', action="store_true", default=False, help='Should it be uploaded to TestLink?')
    parser.add_argument('-t','--testproject', default='', type=str, help='TestLink project name.')
    args = parser.parse_args()
    main()