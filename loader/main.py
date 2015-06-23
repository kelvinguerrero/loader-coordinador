from loadercoordinador import estudiantes
import os
import argparse
__author__ = 'kelvin'


def main(**kwargs):
    if kwargs['load'] == "estudiantes":
        estudiantes.cargar_estudiantes_general()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--load', default='', type=str, help='Type of load to do.')
    parser.add_argument('-f','--ofile', default='', type=str, help='File to load the project.')
    #parser.add_argument('-u','--utestlink', action="store_true", default=False, help='Should it be uploaded to TestLink?')
    args = parser.parse_args()
    print(args)
    main(**vars(args))