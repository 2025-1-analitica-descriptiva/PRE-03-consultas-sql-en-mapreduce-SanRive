"""Taller evaluable"""

# pylint: disable=broad-exception-raised
# pylint: disable=import-error
from .mapreduce import run_mapreduce_job 


def mapperQuery1(sequence):
    """Mapper"""
    map = []
    for index, (_, row) in enumerate(sequence): 
        if index == 0: 
            map.append((index, row.strip() + ",tip_rate"))
        else:
            row_values = row.strip().split(",")
            total_bill = float(row_values[0])
            tip = float(row_values[1])
            tip_rate = tip / total_bill
            map.append((index, row.strip() + "," + str(tip_rate)))
    return map


def reducerQuery1(sequence):
    return sequence

# SELECT *
# FROM tips:
# WHERE time = 'Dinner';

def mapperQuery2(sequence):
    map = []
    for index, (_, row) in enumerate(sequence): 
        if index == 0: #for column names
            map.append((index, row.strip()))
        else:
            row_values = row.strip().split(",")
            if row_values[-2] == "Dinner":
                map.append((index, row.strip()))

    return map


def reducerQuery2(sequence):
    return sequence

# SELECT *
# FROM tips:
# WHERE time = 'Dinner' and tips > 5.0;

def mapperQuery3(sequence):
    map = []
    for index, (_, row) in enumerate(sequence): 
        if index == 0: #for column names
            map.append((index, row.strip()))
        else:
            row_values = row.strip().split(",")
            if row_values[-2] == "Dinner" and float(row_values[1]) > 5.0:
                map.append((index, row.strip()))

    return map


def reducerQuery3(sequence):
    return sequence


#
# SELECT *
# FROM tips:
# WHERE size >= 5 or total_bills > 45;
#

def mapperQuery4(sequence):
    map = []
    for index, (_, row) in enumerate(sequence): 
        if index == 0: #for column names
            map.append((index, row.strip()))
        else:
            row_values = row.strip().split(",")
            if float(row_values[-1]) >= 5 or float(row_values[0]) > 45:
                map.append((index, row.strip()))

    return map


def reducerQuery4(sequence):
    return sequence

# SELECT sex, count(*)
# FROM tips:
# GROUP BY sex;

def mapperQuery5(sequence):
    map = []
    for index, (_, row) in enumerate(sequence): 
        if index == 0: #for column names
            pass
        else:
            row_values = row.strip().split(",")
            if row_values[2] == "Male" or row_values[2] == "Female":
                map.append((row_values[2], 1))
    return map


def reducerQuery5(sequence):
    redux = {}
    for sex, count in sequence:
        if sex not in redux: redux[sex] = 1
        else: redux[sex] += 1
    return sequence

# ORQUESTADOR:

def run():
    """Orquestador"""
    run_mapreduce_job(mapperQuery1, reducerQuery1, "files/input", "files/query_1")
    run_mapreduce_job(mapperQuery2, reducerQuery2, "files/input", "files/query_2")
    run_mapreduce_job(mapperQuery3, reducerQuery3, "files/input", "files/query_3")
    run_mapreduce_job(mapperQuery4, reducerQuery4, "files/input", "files/query_4")
    run_mapreduce_job(mapperQuery5, reducerQuery5, "files/input", "files/query_5")


if __name__ == "__main__":
    run()